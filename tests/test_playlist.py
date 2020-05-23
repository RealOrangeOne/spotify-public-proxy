from src.app import app
from unittest import TestCase
from starlette.testclient import TestClient


def build_playlist(user, id):
    return "/v1/users/{}/playlists/{}".format(
        user, id
    )


class PlaylistTestCase(TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_valid_playlist(self):
        response = self.client.get(build_playlist("theorangeone97", "4SLjpGGoOoiCDhc9sgNx8w"))
        self.assertEqual(response.status_code, 200)

    def test_invalid_playlist(self):
        response = self.client.get(build_playlist("spotifyyyyy", "59ZbFPES4DQwEjBpWHzrtC"))
        self.assertEqual(response.status_code, 404)

    def test_passes_querystring(self):
        response = self.client.get(build_playlist("theorangeone97", "4SLjpGGoOoiCDhc9sgNx8w") + '?limit=10')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['tracks']['limit'], 10)
