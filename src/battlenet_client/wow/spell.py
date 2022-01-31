"""Provides access to the Spells API endpoint"""
from typing import Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from wow_api.client import WoWClient

from wow_api.decorators import verify_client


class SpellAPI:
    
    def __init__(self, client: 'WoWClient') -> None:
        self.client = client

    @verify_client
    def spell(self, locale: str, spell_id: int) -> Dict[str, Any]:
        """Returns an index of spells, or a specific spell
    
        Args:
            locale (str): which locale to use for the request, default is None, using the client's locale
            spell_id (int): the slug or ID of the region requested
    
        Returns:
            dict: json decoded data for the index/individual spell(s)
        """
        data: Dict[str, Any] = self.client.game_data(locale, 'static', 'spell', spell_id)
        return data

    @verify_client
    def spell_media(self, locale: str, spell_id: int) -> Dict[str, Any]:
        """Returns media for a spell by ID.
    
        Args:
            spell_id (int): pvp tier id
            locale (str): which locale to use for the request, default is None, using the client's locale
    
        Returns:
            dict: json decoded media data for the spell
        """
        data: Dict[str, Any] = self.client.media_data(locale, 'static', 'spell', spell_id)
        return data

    @verify_client
    def spell_search(self, locale, field_values=None) -> Dict[str, Any]:
        """Searches the creature API for items that match the criteria
    
        Args:
            locale (str): locale to use with the API
            field_values (dict): search criteria, as key/value pairs
    
        Returns:
            dict: json decoded search results that match `field_values`
        """
        data: Dict[str, Any] = self.client.search(locale, 'static', 'spell', field_values)
        return data
