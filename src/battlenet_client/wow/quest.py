"""Provides access to the quest API endpoints"""
from typing import Optional, Any, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from battlenet_client.wow.client import Client

from battlenet_client.wow.decorators import verify_client


class QuestAPI:
    def __init__(self, client: "Client") -> None:
        self.client = client

    @verify_client
    def quest(self, locale: str, quest_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of quests, or a specific quest

        Args:
            locale (str): which locale to use for the request
            quest_id (int, optional): the quest ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual quest(s)
        """
        if quest_id is not None:
            data: Dict[str, Any] = self.client.game_data(
                locale, "static", "quest", quest_id
            )
        else:
            data = self.client.game_data(locale, "static", "quest", "index")
        return data

    @verify_client
    def quest_area(
        self, locale: str, quest_area_id: Optional[int] = None
    ) -> Dict[str, Any]:
        """Returns an index of quest areas, or a specific quest area

        Args:
            quest_area_id (int, optional): the quest area ID or the word 'index'
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data for the index/individual quest area(s)
        """
        if quest_area_id is not None:
            data: Dict[str, Any] = self.client.game_data(
                locale, "static", "quest", "area", quest_area_id
            )
        else:
            data = self.client.game_data(locale, "static", "quest", "area", "index")
        return data

    @verify_client
    def quest_category(
        self, locale: str, quest_category_id: Optional[int] = None
    ) -> Dict[str, Any]:
        """Returns an index of quest categories, or a specific quest category

        Args:
            quest_category_id (int, optional): the quest category ID or the word 'index'
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data for the index/individual quest category/categories)
        """
        if quest_category_id is not None:
            data: Dict[str, Any] = self.client.game_data(
                locale, "static", "quest", "category", quest_category_id
            )
        else:
            data = self.client.game_data(locale, "static", "quest", "category", "index")
        return data

    @verify_client
    def quest_type(
        self, locale: str, quest_type_id: Optional[int] = None
    ) -> Dict[str, Any]:
        """Returns an index of quest types, or a specific quest type

        Args:
            quest_type_id (int, optional): the quest type ID or the word 'index'
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data for the index/individual quest type(s)
        """
        if quest_type_id is not None:
            data: Dict[str, Any] = self.client.game_data(
                locale, "static", "quest", "type", quest_type_id
            )
        else:
            data = self.client.game_data(locale, "static", "quest", "type", "index")
        return data
