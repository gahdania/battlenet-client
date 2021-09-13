from decouple import config
import pytest

from battlenet_client.client import BattleNetClient
from battlenet_client.constants import UNITED_STATES, WOW
from battlenet_client import exceptions


class TestCredentialClient:

    connection = BattleNetClient(UNITED_STATES, WOW, config('CLIENT_ID'), config('CLIENT_SECRET'))

    def test_get_not_found(self):
        with pytest.raises(exceptions.BNetDataNotFoundError):
            self.connection.api_get(f'{self.connection.api_host}/data/wow/playable-class/-1', 'en_US',
                                    headers={'Battlenet-Namespace': 'static-us'})
            
    def test_get_found(self):
        data = self.connection.api_get(f'{self.connection.api_host}/data/wow/playable-class/1', 'enus',
                                       headers={'Battlenet-Namespace': 'static-us'})
        assert type(data) == dict

    def test_post_not_found(self):
        with pytest.raises(exceptions.BNetDataNotFoundError):
            self.connection.api_post(f'{self.connection.api_host}/data/wow/playable-class/-1', 'en_US',
                                     headers={'Battlenet-Namespace': 'static-us'})

    def test_post_invalid(self):
        with pytest.raises(exceptions.BNetDataNotFoundError):
            self.connection.api_post(f'{self.connection.api_host}/data/wow/playable-class/1', 'enus',
                                     headers={'Battlenet-Namespace': 'static-us'})
