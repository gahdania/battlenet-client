"""Provides access the mounts API endpoint of World of Warcraft"""
from typing import Any, Dict, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from wow_api.client import WoWClient

from wow_api.decorators import verify_client


class MountAPI:
    
    def __init__(self, client: 'WoWClient') -> None:
        self.client = client
                
    @verify_client
    def mount(self, locale: str, mount_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of mounts, or a specific mount
    
        Args:
            locale (str): which locale to use for the request
            mount_id (int, optional): the mount ID or 'index'
    
        Returns:
            dict: json decoded data for the index/individual mount(s)
        """
        if mount_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'mount', mount_id)
        else:
            data = self.client.game_data(locale, 'static', 'mount', 'index')
        return data
    
    @verify_client
    def mount_search(self, locale: str, field_values: Dict[str, Any]) -> Dict[str, Any]:
        """Searches the mount API match the criteria
    
        Args:
            locale (str): which locale to use for the request
            field_values (dict): fields and values for the search criteria
    
        Returns:
            dict: json decoded search results that match `field_values`
        """
        data: Dict[str, Any] = self.client.search(locale, 'static', 'mount', field_values)
        return data
