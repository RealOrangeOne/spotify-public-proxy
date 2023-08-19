from unittest import TestCase

from starlette.testclient import TestClient

from src.app import app


def build_playlist(user: str, playlist_id: str) -> str:
    return "/v1/users/{}/playlists/{}".format(user, playlist_id)


class PlaylistTestCase(TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_valid_playlist(self) -> None:
        response = self.client.get(
            build_playlist("theorangeone97", "4SLjpGGoOoiCDhc9sgNx8w")
        )
        self.assertEqual(response.status_code, 200)

    def test_invalid_playlist(self) -> None:
        response = self.client.get(
            build_playlist("spotifyyyyy", "59ZbFPES4DQwEjBpWHzrtC")
        )
        self.assertEqual(response.status_code, 404)

    def test_passes_querystring(self) -> None:
        response = self.client.get(
            build_playlist("theorangeone97", "4SLjpGGoOoiCDhc9sgNx8w") + "?limit=10"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["tracks"]["limit"], 10)
