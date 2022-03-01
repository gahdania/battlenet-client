"""Tests for the two custom exceptions

Notes:
    achievement is used since it is the first module and suitable for testing both exceptions"""
import pytest

from battlenet_client.clients import BattleNetClient
from battlenet_client.bnet.constants import UNITED_STATES, WOW
from decouple import config

from battlenet_client.wow import WoWClientError, WoWReleaseError
from battlenet_client.wow import AchievementAPI


class TestAchivementAPI:
    def test_invalid_client(self):
        client = BattleNetClient(
            UNITED_STATES,
            WOW,
            client_id=config("CLIENT_ID"),
            client_secret=config("CLIENT_SECRET"),
        )
        with pytest.raises(WoWClientError):
            AchievementAPI(client).achievement("enus", "index")
        client.close()


@pytest.mark.usefixtures("cred_client")
class TestWoWReleaseError:
    @pytest.mark.era("classic1x")
    def test_invalid_release(self, cred_client):
        with pytest.raises(WoWReleaseError):
            AchievementAPI(cred_client).achievement("enus", "index")
