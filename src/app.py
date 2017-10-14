from sanic import Sanic
from sanic_useragent import SanicUserAgent
import views.playlist
from match import PLAYLIST_ID_MATCH

app = Sanic(__name__)
SanicUserAgent.init_app(app)

app.add_route(views.playlist.get_playlist_details, '/playlist/<id:{}>'.format(PLAYLIST_ID_MATCH))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
