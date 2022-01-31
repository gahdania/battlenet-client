"""Provides access to the connected realm related API game_data for World of Warcraft"""
from typing import Optional, Union, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from wow.client import WoWClient

from wow.decorators import verify_client


class ConnectedRealmAPI:
    
    def __init__(self, client: 'WoWClient') -> None:
        self.client = client
            
    @verify_client
    def connected_realm(self, locale: str, connected_realm_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of connected realms, or a specific connected realm. Connected realm is a group of standard
        realms that act as one large realm
    
        Args:
            locale (str): which locale to use for the request
            connected_realm_id (int, optional): the ID of the connected realm
    
        Returns:
            dict: json decoded data for the index/individual connected realms
        """
        if connected_realm_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'dynamic', 'connected-realm', connected_realm_id)
        else:
            data = self.client.game_data(locale, 'dynamic', 'connected-realm', 'index')

        return data
    
    @verify_client
    def connected_realm_search(self, locale: str, field_values: Dict[str, Union[str, int]]) -> Dict[str, Any]:
        """Searches the connected realm API for connected realm(s) that match the criteria
    
        Args:
            locale (str): which locale to use for the request
            field_values (dict): field/value pairs
    
        Returns:
            dict: json decoded search results that match `field_values`
        """
        data: Dict[str, Any] = self.client.search(locale, 'dynamic', 'connected-realm', fields=field_values)
        return data
