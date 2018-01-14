from sanic import Sanic
from sanic_useragent import SanicUserAgent
from sanic import response
from spotify import get_access_token, API_URL
import os
import requests

app = Sanic(__name__)
SanicUserAgent.init_app(app)


@app.get('/')
def redirect_to_repo(request):
    return response.redirect('https://github.com/realorangeone/spotify-public-proxy')


@app.get('/<url:path>', strict_slashes=False)
async def proxy_to_spotify(request, url):
    spotify_response = requests.get(os.path.join(API_URL, url), headers={
        'Authorization': 'Bearer {}'.format(get_access_token())
    })
    return response.json(spotify_response.json(), status=spotify_response.status_code)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ.get("PORT", 5000))
