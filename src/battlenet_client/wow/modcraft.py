"""Provides access to the processions and modified crafting API game_datas for World of Warcraft"""
from typing import Optional, Any, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from wow_api.client import WoWClient

from wow_api.decorators import verify_client


class ModifiedCraftingAPI:
    
    def __init__(self, client: 'WoWClient') -> None:
        self.client = client
        
    @verify_client
    def modified_crafting(self, locale: str) -> Dict[str, Any]:
        """Returns an index of modified crafting recipes
    
        Args:
            locale (str): which locale to use for the request
    
        Returns:
            dict: json decoded data for the index of modified crafting
        """
        data: Dict[str, Any] = self.client.game_data(locale, 'static', 'modified-crafting', 'index')
        return data
    
    @verify_client
    def modified_crafting_category(self, locale: str, category_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of modified crafting category index, or a specific modified crafting category
    
        Args:
            locale (str): which locale to use for the request
            category_id (int, optional): the encounter ID or 'index'
    
        Returns:
            dict: json decoded data for the index/individual modified crafting category/categories
        """
        if category_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'modified-crafting', 'category', category_id)
        else:
            data = self.client.game_data(locale, 'static', 'modified-crafting', 'category', 'index')
        return data
    
    @verify_client
    def modified_crafting_reagent_slot_type(self, locale: str, slot_type_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of modified crafting reagent slot type, or a specific reagent slot type
    
        Args:
            locale (str): which locale to use for the request
            slot_type_id (int, optional): the encounter ID or 'index'
    
        Returns:
            dict: json decoded data for the index/individual modified crafting reagent slot type(s)
        """
        if slot_type_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'modified-crafting', 'reagent-slot-type',
                                                         slot_type_id)
        else:
            data = self.client.game_data(locale, 'static', 'modified-crafting', 'reagent-slot-type', 'index')
        return data
