"""Provides access to the playable class API for the World of Warcraft"""
from typing import Optional, Any, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from wow.client import WoWClient

from wow.decorators import verify_client


class PlayableClassAPI:
    
    def __init__(self, client: 'WoWClient') -> None:
        self.client = client
            
    @verify_client
    def playable_class(self, locale: str, class_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of playable classes, or a specific playable class
    
        Args:
            locale (str): which locale to use for the request
            class_id (int, optional): the class ID or the word 'index'
    
        Returns:
            dict: json decoded data for the index/individual playable class(es)
        """
        if class_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'playable-class', class_id)
        else:
            data = self.client.game_data(locale, 'static', 'playable-class', 'index')
        return data
    
    @verify_client
    def playable_class_media(self, locale: str, class_id: int) -> Dict[str, Any]:
        """Returns media for a playable class by ID.
    
        Args:
            locale (str): which locale to use for the request
            class_id (int ): class id
    
        Returns:
            dict: json decoded media data for the playable class(es)
        """
        data: Dict[str, Any] = self.client.media_data(locale, 'static', 'playable-class', class_id)
        return data
    
    @verify_client
    def pvp_talent_slots(self, locale: str, class_id: int) -> Dict[str, Any]:
        """Returns the PvP talent slots for a playable class by ID.
    
        Args:
            locale (str): which locale to use for the request
            class_id (int): class id
    
        Returns:
            dict: json decoded data for the index of PvP Talent slots
        """
        data: Dict[str, Any] = self.client.game_data(locale, 'static', 'playable-class', class_id, 'pvp-talent-slots')
        return data
