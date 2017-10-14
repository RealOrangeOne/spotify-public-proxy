from src.app import app
from unittest import TestCase
from tests import fixtures
from src import match


class PlaylistTestCase(TestCase):
    def build_url(self, ident):
        return "/playlist/{}".format(ident)

    def test_invalid_playlist_id(self):
        request, response = app.test_client.get(self.build_url(fixtures.INVALID_PLAYLIST_ID))
        self.assertEqual(response.status, 404)

    def test_invalid_playlist_user(self):
        request, response = app.test_client.get(self.build_url(fixtures.INVALID_PLAYLIST_USER))
        self.assertEqual(response.status, 404)

    def test_playlist_details(self):
        request, response = app.test_client.get(self.build_url(fixtures.VALID_PLAYLIST))
        self.assertEqual(response.status, 200)
        data = response.json
        self.assertEqual(data['name'], 'United Kingdom Top 50')
        self.assertEqual(data['uri'], fixtures.VALID_PLAYLIST)
        self.assertTrue(data['description'])
        self.assertGreater(data['followers'], 0)

    def test_track_data(self):
        request, response = app.test_client.get(self.build_url(fixtures.VALID_PLAYLIST))
        self.assertEqual(response.status, 200)
        data = response.json['tracks'][0]
        self.assertEqual(type(data['duration_ms']), int)
        self.assertGreater(data['popularity'], 0)
        self.assertRegex(data['uri'], match.TRACK_ID_MATCH)

    def test_album_data(self):
        request, response = app.test_client.get(self.build_url(fixtures.VALID_PLAYLIST))
        self.assertEqual(response.status, 200)
        data = response.json['tracks'][0]['album']
        self.assertNotEqual(data['album_type'], '')
        self.assertRegex(data['uri'], match.ALBUM_ID_MATCH)
        for artist in response.json['tracks'][0]['album']['artists']:
            self.assertIn(artist, response.json['tracks'][0]['artists'])
            self.assertRegex(artist['uri'], match.ARTIST_ID_MATCH)


