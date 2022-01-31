"""Provides access the WoW token API endpoint for World of Warcraft"""
from typing import Optional, Union, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from wow_api.client import WoWClient

from wow_api.decorators import verify_client
from wow_api.exceptions import WoWReleaseError


class TokenAPI:
    
    def __init__(self, client: 'WoWClient') -> None:
        self.client = client
            
    @verify_client
    def wow_token_index(self, locale: str) -> Dict[str, Any]:
        """Returns the WoW Token index.
    
        Args:
            locale (str): which locale to use for the request
    
        Returns:
            dict: json decoded data for the index/individual wow token
        """
        if self.client.release in ('classic1x', 'classic') and self.client.tag != 'cn':
            raise WoWReleaseError("WoW Token API only available on retail, and CN classic markets")

        data: Dict[str, Any] = self.client.game_data(locale, 'dynamic', 'token', 'index')
        return data
