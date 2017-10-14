from sanic import Sanic
from sanic_useragent import SanicUserAgent
from sanic import response
import views.playlist
from match import PLAYLIST_ID_MATCH


def redirect_to_repo(request):
    return response.redirect('https://github.com/realorangeone/spotify-public-proxy')

app = Sanic(__name__)
SanicUserAgent.init_app(app)

app.add_route(views.playlist.get_playlist_details, '/playlist/<id:{}>'.format(PLAYLIST_ID_MATCH))
app.add_route(redirect_to_repo, '/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
