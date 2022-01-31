"""Provides access tho the profession API endpoints for World of Warcraft"""
from typing import Any, Dict, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from wow_api.client import WoWClient

from wow_api.decorators import verify_client


class ProfessionAPI:
    
    def __init__(self, client: 'WoWClient') -> None:
        self.client = client

    @verify_client
    def profession(self, locale: str, profession_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of achievements, or a specific achievements
    
        Args:
            locale (str): which locale to use for the request
            profession_id (int, optional): the profession ID or the word 'index'
    
        Returns:
            dict: json decoded dict for the profession or the index of the achievements
        """
        if profession_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'profession', profession_id)
        else:
            data = self.client.game_data(locale, 'static', 'profession', 'index')
        return data

    @verify_client
    def profession_media(self, locale: str, profession_id: int) -> Dict[str, Any]:
        """Returns media for a creature display.
    
        Args:
            profession_id (int): the profession ID
            locale (str): which locale to use for the request
    
        Returns:
            dict: the media assets for the given creature display ID
        """
        data: Dict[str, Any] = self.client.media_data(locale, 'static', 'profession', profession_id)
        return data

    @verify_client
    def profession_skill_tier(self, locale: str, profession_id: int, skill_tier_id: int) -> Dict[str, Any]:
        """Returns an index of achievements, or a specific achievements
    
        Args:
            profession_id (int): the profession ID
            skill_tier_id (int): the skill tier ID
            locale (str): which locale to use for the request
    
        Returns:
            dict: json decoded dict for the profession or the index of the achievements
        """
        data: Dict[str, Any] = self.client.game_data(locale, 'static', 'profession', profession_id, 'skill-tier',
                                                     skill_tier_id)
        return data

    @verify_client
    def recipe(self, locale: str, recipe_id: int):
        """Returns an index of achievements, or a specific achievements
    
        Args:
            recipe_id (int, optional): the recipe ID or the word 'index'
            locale (str): which locale to use for the request
    
        Returns:
            dict: json decoded dict for the profession or the index of the achievements
        """
        data: Dict[str, Any] = self.client.game_data(locale, 'static', 'recipe', recipe_id)
        return data

    @verify_client
    def recipe_media(self, locale: str, recipe_id: int) -> Dict[str, Any]:
        """Returns media for a creature display.
    
        Args:
            recipe_id (int): the profession ID
            locale (str): which locale to use for the request
    
        Returns:
            dict: the media assets for the given creature display ID
        """
        data: Dict[str, Any] = self.client.media_data(locale, 'static', 'recipe', recipe_id)
        return data
