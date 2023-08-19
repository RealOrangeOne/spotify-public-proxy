from unittest import TestCase

from starlette.testclient import TestClient

from src.app import app


class URLsTestCase(TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_healthcheck(self) -> None:
        response = self.client.get("/.health/")

        self.assertEqual(response.status_code, 200)
