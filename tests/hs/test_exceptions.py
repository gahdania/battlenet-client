import pytest


from hs_client.exceptions import HSClientError
from hs_client import card


@pytest.mark.usefixtures('cred_client')
class TestHSClientError:

    def test_invalid_client(self):
        self.assertRaises(HSClientError, lambda: card(self.client, 'enus', '52119-arch-villain-rafaam'))
