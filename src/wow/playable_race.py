"""Provides access to the Playable Race API for World of Warcraft"""
from typing import Any, Dict, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from wow.client import WoWClient

from wow.decorators import verify_client


class PlayableRaceAPI:
    
    def __init__(self, client: 'WoWClient') -> None:
        self.client = client
        
    @verify_client
    def playable_race(self, locale: str, race_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of playable races, or a specific playable race
    
        Args:
            locale (str): which locale to use for the request
            race_id (int, optional): the playable race's ID or the word 'index'
    
        Returns:
            dict: json decoded data for the index/individual playable race(s)
        """
        if race_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'playable-race', race_id)
        else:
            data = self.client.game_data(locale, 'static', 'playable-race', 'index')
        return data
