import re

PLAYLIST_ID_MATCH = r"spotify:user:([0-9a-zA-Z]+?):playlist:([0-9a-zA-Z]{22})"

def decode_playlist_id(playlist_id):
    result = re.search(PLAYLIST_ID_MATCH, playlist_id)
    return {
        "user": result.group(1),
        "playlist": result.group(2)
    }
