import pytest
from battlenet_client.bnet.client import BattleNetClient
from battlenet_client.bnet.constants import UNITED_STATES, WOW
from decouple import config


@pytest.fixture(scope="session")
def client():
    with BattleNetClient(
        UNITED_STATES, WOW, config("CLIENT_ID"), config("CLIENT_SECRET")
    ) as client:
        yield client