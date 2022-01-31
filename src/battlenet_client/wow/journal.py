"""Provides access to the Adventurer's Guide API end points for the World of Warcraft"""
from typing import Optional, Any, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from wow_api.client import WoWClient

from wow_api.decorators import verify_client


class JournalAPI:
    
    def __init__(self, client: 'WoWClient') -> None:
        self.client = client
    
    @verify_client
    def journal_expansion(self, locale: str, expansion_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of journal expansions, or a specific journal expansion
    
        Args:
            locale (str): which locale to use for the request, default is None, using the client's locale
            expansion_id (int, optional): the encounter ID or 'index'
    
        Returns:
            dict: json decoded data for the index/individual journal expansion(s)
        """
        if expansion_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'journal-expansion', expansion_id)
        else:
            data = self.client.game_data(locale, 'static', 'journal-expansion', 'index')
        return data

    @verify_client
    def journal_encounter(self, locale, encounter_id=None) -> Dict[str, Any]:
        """Returns an index of journal (boss) encounters, or a specific journal (boss) encounters
    
        Notes:
            This replaced the Boss endpoint of the community REST API
            locale (str): which locale to use for the request, default is None, using the client's locale
    
        Args:
            locale (str): which locale to use for the request, default is None, using the client's locale
            encounter_id (int, optional): the encounter ID or 'index'
    
        Returns:
            dict: json decoded data for the index/individual journal encounter(s)
        """
        if encounter_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'journal-encounter', encounter_id)
        else:
            data = self.client.game_data(locale, 'static', 'journal-encounter', 'index')
        return data

    @verify_client
    def journal_encounter_search(self, locale, field_values) -> Dict[str, Any]:
        """Searches for azerite essences that match `field_values`
    
         Args:
             locale (str): locale to use with the API
             field_values (dict): search criteria, as key/value pairs
    
         Returns:
             dict: json decoded search results that match `field_values`
         """
        data: Dict[str, Any] = self.client.search(locale, 'static', 'journal-encounter', field_values)
        return data
    
    @verify_client
    def journal_instance(self, locale, instance_id=None) -> Dict[str, Any]:
        """Returns an index of journal instances (dungeons), or a specific journal instance (dungeon)
    
        Args:
            locale (str): which locale to use for the request, default is None, using the client's locale
            instance_id (int, optional): the encounter ID or 'index'
    
        Returns:
            dict: json decoded data for the index/individual journal instance(s)
        """
        if instance_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'journal-instance', instance_id)
        else:
            data = self.client.game_data(locale, 'static', 'journal-instance', 'index')
        return data
    
    @verify_client
    def journal_instance_media(self, locale, instance_id) -> Dict[str, Any]:
        """Returns media for an instance.
    
        Args:
            locale (str): which locale to use for the request
            instance_id (int): the creature family ID
    
        Returns:
            dict: json decoded media data for the instance
        """
        data: Dict[str, Any] = self.client.media_data(locale, 'static', 'journal-instance', instance_id)
        return data
