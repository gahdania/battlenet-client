"""Provides access to Talent API endpoints"""
from typing import Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from wow.client import WoWClient

from wow.decorators import verify_client


class TechTalentAPI:
    
    def __init__(self, client: 'WoWClient') -> None:
        self.client = client
            
    @verify_client
    def tech_talent_tree(self, locale: str, tree_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of tech talent trees or a tech talent tree by ID
    
        Args:
            locale (str): which locale to use for the request
            tree_id (int, optional): the slug or ID of the region requested
    
        Returns:
            dict: json decoded data for the index/individual tech talent tree(s)
        """
        if tree_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'tech-talent-tree', tree_id)
        else:
            data = self.client.game_data(locale, 'static', 'tech-talent-tree', 'index')
        return data

    @verify_client
    def tech_talent(self, locale, talent_id=None) -> Dict[str, Any]:
        """Returns an index of tech talents or a tech talent by ID
    
        Args:
            locale (str): which locale to use for the request
            talent_id (int, optional): the slug or ID of the region requested
    
        Returns:
            dict: json decoded data for the index/individual tech talent(s)
        """
        if talent_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'tech-talent', talent_id)
        else:
            data = self.client.game_data(locale, 'static', 'tech-talent', 'index')
        return data

    @verify_client
    def tech_talent_media(self, locale: str, talent_id: int) -> Dict[str, Any]:
        """Returns media for a spell by ID.
    
        Args:
            locale (str): which locale to use for the request
            talent_id (int): pvp tier id
    
        Returns:
            dict: json decoded media data for the tech talent
        """
        data: Dict[str, Any] = self.client.media_data(locale, 'static', 'tech-talent', talent_id)
        return data
