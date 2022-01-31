"""Provides access to the Title API endpoint"""
from typing import Optional, Union, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from wow_api.client import WoWClient

from wow_api.decorators import verify_client


class TitleAPI:
    
    def __init__(self, client: 'WoWClient') -> None:
        self.client = client
            
    @verify_client
    def title(self, locale: str, title_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of spells, or a specific spell
    
        Args:
            locale (str): which locale to use for the request
            title_id (int, optional): the slug or ID of the region requested
    
        Returns:
            dict: json decoded data for the index/individual title(s)
        """
        if title_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'title', title_id)
        else:
            data = self.client.game_data(locale, 'static', 'title', 'index')

        return data
