from spotify import get_access_token, API_URL
import os
import requests
from urllib.parse import urljoin
import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse, Response, RedirectResponse
from starlette.routing import Route


async def redirect_to_repo(request):
    return RedirectResponse('https://github.com/realorangeone/spotify-public-proxy')


async def proxy_to_spotify(request):
    spotify_url = urljoin(API_URL, request.url.path)
    if request.query_params:
        spotify_url += "?" + str(request.query_params)
    spotify_response = requests.get(spotify_url, headers={
        'Authorization': 'Bearer {}'.format(get_access_token()),
        'Accept': 'application/json'
    })
    if spotify_response.status_code != 200:
        return Response(spotify_response.text, status_code=spotify_response.status_code)
    return JSONResponse(spotify_response.json(), status_code=spotify_response.status_code)

app = Starlette(routes=[
    Route("/", redirect_to_repo, methods=['GET']),
    Route("/(.*)", proxy_to_spotify, methods=['GET'])
])

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=os.environ.get("PORT", 5000))
