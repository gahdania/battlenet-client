import pytest

from hs_client.client import HSClient
from battlenet_client.bnet.constants import UNITED_STATES


@pytest.fixture
def cred_client(request):
    client = HSClient(UNITED_STATES)
    yield client
    client.close()
