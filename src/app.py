from sanic import Sanic, response
from spotify import get_access_token, API_URL
import os
import requests
from urllib.parse import urlparse, urljoin

app = Sanic(__name__)


@app.get('/')
def redirect_to_repo(request):
    return response.redirect('https://github.com/realorangeone/spotify-public-proxy')


@app.get('/<raw_url:path>', strict_slashes=False)
async def proxy_to_spotify(request, raw_url):
    parsed_url = urlparse(request.url)
    spotify_url = urljoin(API_URL, "{}?{}".format(parsed_url.path, parsed_url.query))
    spotify_response = requests.get(spotify_url, headers={
        'Authorization': 'Bearer {}'.format(get_access_token()),
        'Accept': 'application/json'
    })
    if spotify_response.status_code != 200:
        return response.text(spotify_response.text, status=spotify_response.status_code)
    return response.json(spotify_response.json(), status=spotify_response.status_code)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000))
