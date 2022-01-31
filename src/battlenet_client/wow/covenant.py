"""Provides access to the covenant related API end points for World of Warcraft"""
from typing import Optional, Any, TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from wow_api.client import WoWClient

from wow_api.decorators import verify_client


class CovenantAPI:

    def __init__(self, client: 'WoWClient') -> None:
        self.client = client

    @verify_client
    def covenant(self, locale: str, covenant_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of covenants, or a specific covenant
    
        Args:
            locale (str): which locale to use for the request
            covenant_id (int, optional): the ID of the covenant or the default 'index'
    
        Returns:
            dict: json decoded data for the index/individual covenant
        """
        if covenant_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'covenant', covenant_id)
        else:
            data = self.client.game_data(locale, 'static', 'covenant', 'index')
        return data
    
    @verify_client
    def covenant_media(self, locale: str, covenant_id: int) -> Dict[str, Any]:
        """Returns media for a covenant.
    
        Args:
            locale (str): which locale to use for the request
            covenant_id (int, optional): the covenant ID
    
        Returns:
            dict: json decoded media data for the covenant
        """
        data: Dict[str, Any] = self.client.media_data(locale, 'static', 'covenant', covenant_id)
        return data
    
    @verify_client
    def soulbind(self, locale: str, soulbind_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of soulbinds, or a specific soulbind
    
        Args:
            locale (str): which locale to use for the request
            soulbind_id (int, optional): the ID of the soulbind or the word of 'index'
    
        Returns:
            dict: json decoded data for the index/individual soulbind
        """
        if soulbind_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'covenant', 'soulbind', soulbind_id)
        else:
            data = self.client.game_data(locale, 'static', 'covenant', 'soulbind', 'index')
        return data
    
    @verify_client
    def conduit(self, locale: str, conduit_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of conduits, or a specific conduit
    
        Args:
            locale (str): which locale to use for the request
            conduit_id (int, optional): the ID of the conduit or the word of 'index'
    
        Returns:
            dict: json decoded data for the index/individual conduit
        """
        if conduit_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'covenant', 'conduit', conduit_id)
        else:
            data = self.client.game_data(locale, 'static', 'covenant', 'conduit', 'index')
        return data
