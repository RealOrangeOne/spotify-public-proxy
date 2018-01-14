from src.app import app
from unittest import TestCase


def build_playlist(user, id):
    return "/v1/users/{}/playlists/{}".format(
        user, id
    )


class PlaylistTestCase(TestCase):
    def test_valid_playlist(self):
        request, response = app.test_client.get(build_playlist("spotify", "59ZbFPES4DQwEjBpWHzrtC"))
        self.assertEqual(response.status, 200)

    def test_invalid_playlist(self):
        request, response = app.test_client.get(build_playlist("spotifyyyyy", "59ZbFPES4DQwEjBpWHzrtC"))
        self.assertEqual(response.status, 404)
        self.assertIsNone(response.json)
