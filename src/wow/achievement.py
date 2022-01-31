"""This module contains all of the methods for accessing achievement related
API end points in World of Warcraft

..moduleauthor:: David Couples (Gahdania Stormhoof)"""
from typing import Optional, Any, TYPE_CHECKING, Dict, Union

if TYPE_CHECKING:
    from wow.client import WoWClient

from wow.decorators import verify_client


class AchievementAPI:

    def __init__(self, client: 'WoWClient') -> None:
        self.client = client
        
    @verify_client
    def achievement_category(self, locale: str, category_id: Union[int, None] = None) -> Dict[str, Any]:
        """Accesses a list achievement categories or specific achievement
        category if :category_id: is provided
    
        Args:
            locale (str): which locale to use for the request
            category_id (int, optional): the achievement's category ID or
                None(default).  None will retrieve the entire list of categories
    
        Returns:
    
            dict: json decoded data for the index/individual achievement categories
        """
        if category_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'achievement-category', category_id)
        else:
            data = self.client.game_data(locale, 'static', 'achievement-category', 'index')
        return data
    
    @verify_client
    def achievement(self, locale: str, achievement_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of achievements, or a specific achievements
    
        Args:
            locale (str): which locale to use for the request
            achievement_id (int, optional): the achievement ID or the word 'index'
    
        Returns:
            dict: json decoded data for the index/individual achievements
        """
        if achievement_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'achievement', achievement_id)
        else:
            data = self.client.game_data(locale, 'static', 'achievement', 'index')

        return data

    @verify_client
    def achievement_media(self, locale: str, achievement_id: int) -> Dict[str, Any]:
        """Returns media for an achievement's icon.
    
        Args:
            locale (str): which locale to use for the request
            achievement_id (int): the achievement ID or the word 'index'
    
        Returns:
            dict: json decoded media data for the achievement
        """
        data: Dict[str, Any] = self.client.media_data(locale, 'static', 'achievement', achievement_id)
        return data
