import pytest

from battlenet_client.constants import HS

from hs_client.client import HSClient


@pytest.mark.usefixtures("cred_client")
class TestClient:
    def test_client(self, cred_client):
        self.assertIsInstance(cred_client, HSClient)
        self.assertEqual(cred_client.game, HS)
