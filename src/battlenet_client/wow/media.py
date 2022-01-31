"""Provides access to media API end points for World of Warcraft"""
from typing import Any, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from wow_api.client import WoWClient

from wow_api.decorators import verify_client


class MediaAPI:
    
    def __init__(self, client: 'WoWClient') -> None:
        self.client = client
        
    @verify_client
    def media_search(self, locale: str, field_values: Dict[str, Any]) -> Dict[str, Any]:
        """Searches the media API match the criteria
    
        Args:
            locale (str): which locale to use for the request
            field_values (dict): fields and values for the search criteria
    
        Returns:
            dict: json decoded search results that match `field_values`
        """
        data: Dict[str, Any] = self.client.search(locale, 'static', 'media', field_values)
        return data
