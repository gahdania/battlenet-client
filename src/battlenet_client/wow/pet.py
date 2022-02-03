"""Provides access the pet API game_data"""
from typing import Optional, Any, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from battlenet_client.wow.client import Client

from battlenet_client.wow.decorators import verify_client


class PetAPI:
    def __init__(self, client: "Client") -> None:
        self.client = client

    @verify_client
    def pet(self, locale: str, pet_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of pets, or the data about the specified pet

        Args:
            locale (str): which locale to use for the request
            pet_id (int, optional): the pet ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual pet(s)
        """
        if pet_id is not None:
            data: Dict[str, Any] = self.client.game_data(
                locale, "static", "pet", pet_id
            )
        else:
            data = self.client.game_data(locale, "static", "pet", "index")
        return data

    @verify_client
    def pet_media(self, locale: str, pet_id: int) -> Dict[str, Any]:
        """Returns media for a pet

        Args:
            locale (str): which locale to use for the request
            pet_id (int): the azerite pet ID

        Returns:
            dict: json decoded media data for the for pet
        """
        data: Dict[str, Any] = self.client.media_data(locale, "static", "pet", pet_id)
        return data

    @verify_client
    def pet_ability(self, locale: str, pet_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of pets, or the data about the specified pet

        Args:
            locale (str): which locale to use for the request
            pet_id (int, optional): the pet ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual pet ability/abilities
        """
        if pet_id is not None:
            data: Dict[str, Any] = self.client.game_data(
                locale, "static", "pet-ability", pet_id
            )
        else:
            data = self.client.game_data(locale, "static", "pet-ability", "index")
        return data

    @verify_client
    def pet_ability_media(self, locale: str, ability_id: int) -> Dict[str, Any]:
        """Returns media for an azerite ability.

        Args:
            locale (str): which locale to use for the request
            ability_id (int): the azerite ability ID

        Returns:
            dict: json decoded media data for the pet ability
        """
        data: Dict[str, Any] = self.client.media_data(
            locale, "static", "pet-ability", ability_id
        )
        return data
