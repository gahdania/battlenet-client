import pytest

from wow import WoWClient
from battlenet_client.constants import UNITED_STATES


@pytest.fixture
def cred_client(request):
    release = request.node.get_closest_marker("era")
    if release is None:
        client = WoWClient(UNITED_STATES)
    else:
        client = WoWClient(UNITED_STATES, release=release.args[0])
    yield client
    client.close()


@pytest.fixture
def oauth_client(request):
    release = request.node.get_closest_marker("era")
    if release is None:
        client = WoWClient(UNITED_STATES, scope=['wow.profile'], redirect_uri='http://localhost/')
    else:
        client = WoWClient(UNITED_STATES, release=release.args[0], scope=['wow.profile'],
                           redirect_uri='http://localhost/')
    yield client.authorization_url()
    client.close()
