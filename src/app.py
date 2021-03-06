import os
from urllib.parse import urljoin

import httpx
import uvicorn
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse, RedirectResponse, Response
from starlette.routing import Route

from spotify import API_URL, get_access_token


async def redirect_to_repo(request: Request) -> Response:
    return RedirectResponse("https://github.com/realorangeone/spotify-public-proxy")


async def proxy_to_spotify(request: Request) -> Response:
    spotify_url = urljoin(API_URL, request.url.path)
    if request.query_params:
        spotify_url += "?" + str(request.query_params)
    async with httpx.AsyncClient() as client:
        spotify_response = await client.get(
            spotify_url,
            headers={
                "Authorization": "Bearer {}".format(await get_access_token(client)),
                "Accept": "application/json",
            },
        )
        if spotify_response.status_code != 200:
            return Response(
                spotify_response.text, status_code=spotify_response.status_code
            )
        return JSONResponse(
            spotify_response.json(), status_code=spotify_response.status_code
        )


app = Starlette(
    routes=[
        Route("/", redirect_to_repo, methods=["GET"]),
        Route("/(.*)", proxy_to_spotify, methods=["GET"]),
    ]
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=os.environ.get("PORT", 5000), workers=1)
