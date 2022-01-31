"""Provides access to the region related API endpoint"""
from typing import Any, Dict, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from wow_api.client import WoWClient

from wow_api.decorators import verify_client


class RegionAPI:
    
    def __init__(self, client: 'WoWClient') -> None:
        self.client = client
            
    @verify_client
    def region(self, locale: str, region_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of regions, or a specific region
    
        Args:
            locale (str): which locale to use for the request
            region_id (int, optional): the region ID or the word 'index'
    
        Returns:
            dict: json decoded data for the index/individual region(s)
        """
        if region_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'dynamic', 'region', region_id)
        else:
            data = self.client.game_data(locale, 'dynamic', 'region', 'index')
        return data
