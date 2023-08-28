import os
from urllib.parse import urljoin

import httpx
import sentry_sdk
import uvicorn
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from spotify import API_URL, get_access_token
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Route

if sentry_dsn := os.environ.get("SENTRY_DSN"):
    sentry_sdk.init(sentry_dsn)


async def healthcheck(request: Request) -> Response:
    return Response(content="OK")


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
        Route("/.health/", healthcheck, methods=["GET"]),
        Route("/{rest_of_path:path}", proxy_to_spotify, methods=["GET"]),
    ]
)

if __name__ == "__main__":
    uvicorn.run(
        SentryAsgiMiddleware(app),
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        workers=1,
    )
