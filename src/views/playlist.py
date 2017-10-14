from sanic.response import json
from sanic.exceptions import abort
from spotify import get_playlist
from match import decode_playlist_id
from serializer import serialize_playlist


async def get_playlist_details(request, id):
    playlist_id = decode_playlist_id(id)
    playlist_data = get_playlist(**playlist_id)
    if playlist_data is None:
        return abort(404)
    return json(serialize_playlist(playlist_data))
