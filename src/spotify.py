import base64
import os

from aiocache import Cache, cached
from httpx import AsyncClient

CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]

CLIENT_ID_ACCESS_TOKEN = base64.b64encode(
    "{}:{}".format(CLIENT_ID, CLIENT_SECRET).encode()
).decode()

API_URL = "https://api.spotify.com/"


@cached(ttl=120, cache=Cache.MEMORY, key="get_access_token")
async def get_access_token(client: AsyncClient) -> str:
    response = await client.post(
        "https://accounts.spotify.com/api/token",
        data={"grant_type": "client_credentials"},
        headers={"Authorization": "Basic {}".format(CLIENT_ID_ACCESS_TOKEN)},
    )
    return response.json()["access_token"]
