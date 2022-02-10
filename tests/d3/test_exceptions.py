from tests.test_base import *
from src.d3_api import D3ClientError
from src.d3_api import act


class TestD3ClientError(unittest.TestCase):
    def setUp(self):
        self.client = BattleNetClient(
            UNITED_STATES,
            D3,
            client_id=config("CLIENT_ID"),
            client_secret=config("CLIENT_SECRET"),
        )

    def tearDown(self):
        self.client.close()

    def test_invalid_client(self):
        self.assertRaises(D3ClientError, lambda: act(self.client, "enus"))
