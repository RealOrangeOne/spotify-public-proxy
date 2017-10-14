

VALID_PLAYLIST = "spotify:user:spotifycharts:playlist:37i9dQZEVXbLnolsZ8PSNw"
INVALID_PLAYLIST_ID = "spotify:user:spotifycharts:playlist:37i9dQZEVXbLnolsZ8PSNq"
INVALID_PLAYLIST_USER = "spotify:user:2580582903850258350:playlist:37i9dQZEVXbLnolsZ8PSNw"


def build_playlist(user, id):
    return "spotify:user:{}:playlist:{}".format(
        user, id
    )

