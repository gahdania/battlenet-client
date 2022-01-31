"""Provides access the creatures API end points for World of Warcraft"""
from typing import Optional, Union, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from wow.client import WoWClient

from wow.decorators import verify_client


class CreatureAPI:
    def __init__(self, client: 'WoWClient') -> None:
        self.client = client
            
    @verify_client
    def creature_family(self, locale: str, family_id: Optional[int] = None) -> Dict[str, Any]:
        """ Returns an index of creature families, or a specific creature family
    
        Args:
            locale (str): which locale to use for the request
            family_id (int, optional): the creature family ID or the default 'index'
    
        Returns:
            dict: json decoded data for the index/individual creature family/families
        """
        if family_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'creature-family', family_id)
        else:
            data = self.client.game_data(locale, 'static', 'creature-family', 'index')

        return data
    
    @verify_client
    def creature_type(self, locale: str, type_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of creature types, or a specific creature type
    
        Args:
            locale (str): which locale to use for the request
            type_id (int, optional): the creature type ID or the default 'index'
    
        Returns:
            dict: json decoded data for the index/individual creature type(s)
        """
        if type_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'creature-type', type_id)
        else:
            data = self.client.game_data(locale, 'static', 'creature-type', 'index')
        return data

    @verify_client
    def creature(self, locale: str, creature_id: int) -> Dict[str, Any]:
        """Returns an index of creatures, or a specific creature
    
        Args:
            locale (str): which locale to use for the request
            creature_id (int, optional): the creature ID
    
        Returns:
            dict: json decoded data for the index/individual creature(s)
        """
        data: Dict[str, Any] = self.client.game_data(locale, 'static', 'creature', creature_id)
        return data

    @verify_client
    def creature_search(self, locale: str, field_values: Dict[str, Union[str, int]]) -> Dict[str, Any]:
        """Searches the creature API for creatures that match the criteria
    
        Args:
            locale (str): which locale to use for the request
            field_values (dict): matching criteria in key/value pairs
    
        Returns:
            dict: json decoded search results that match `field_values`
        """
        data: Dict[str, Any] = self.client.search(locale, 'static', 'creature', field_values)
        return data
    
    @verify_client
    def creature_family_media(self, locale: str, family_id: int) -> Dict[str, Any]:
        """Returns media for a creature family.
    
        Args:
            locale (str): which locale to use for the request
            family_id (int, optional): the creature family ID
    
        Returns:
            dict: json decoded media data for the creature family
        """
        data: Dict[str, Any] = self.client.media_data(locale, 'static', 'creature-family', family_id)
        return data

    @verify_client
    def creature_display_media(self, locale: str, display_id: int) -> Dict[str, Any]:
        """Returns media for a creature display.
    
        Args:
            locale (str): which locale to use for the request
            display_id (int, optional): the creature display ID
    
        Returns:
            dict: json decoded media data for the creature display
        """
        data: Dict[str, Any] = self.client.media_data(locale, 'static', 'creature-display', display_id)
        return data
