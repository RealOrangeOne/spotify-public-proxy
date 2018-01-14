import requests
import base64
import os
from ratelimit import ratelimit

CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
CLIENT_SECRET = os.environ['SPOTIFY_CLIENT_SECRET']

CLIENT_ID_ACCESS_TOKEN = base64.b64encode("{}:{}".format(
    CLIENT_ID, CLIENT_SECRET
).encode()).decode()

API_URL = "https://api.spotify.com/"


@ratelimit(seconds=120)
def get_access_token():
    response = requests.post(
        "https://accounts.spotify.com/api/token",
        data={
            "grant_type": "client_credentials"
        },
        headers={
            "Authorization": "Basic {}".format(CLIENT_ID_ACCESS_TOKEN),
        }
    )
    return response.json()['access_token']
