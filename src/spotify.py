import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def regen_token():
    token = client_credentials_manager.get_access_token()
    assert token is not None


def get_playlist(user, playlist):
    regen_token()
    try:
        return sp.user_playlist(user, playlist)
    except spotipy.client.SpotifyException as e:
        if e.http_status == 404:
            return None
        raise e
