"""Provides access the Azerite Essence API endpoints for World of Warcraft"""
from typing import Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from battlenet_client.wow.client import Client

from battlenet_client.wow.decorators import verify_client


class AzeriteAPI:
    def __init__(self, client: "Client") -> None:
        self.client = client

    @verify_client
    def azerite_essence(
        self, locale: str, essence_id: Optional[int] = None
    ) -> Dict[str, Any]:
        """Returns an index of Azerite Essences, or a specific Azerite Essence

        Args:
            locale (str): which locale to use for the request
            essence_id (int, optional): the Azerite essence ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual azerite essence(s)
        """
        if essence_id is not None:
            data: Dict[str, Any] = self.client.game_data(
                locale, "static", "azerite-essence", essence_id
            )
        else:
            data = self.client.game_data(locale, "static", "azerite-essence", "index")

        return data

    @verify_client
    def azerite_essence_search(
        self, locale: str, field_values: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Searches for azerite essences that match `field_values`

        Args:
            locale (str): locale to use with the API
            field_values (dict): search criteria, as key/value pairs

        Returns:
            dict: json decoded search results that match `field_values`
        """
        data: Dict[str, Any] = self.client.search(
            locale, "static", "azerite-essence", field_values
        )
        return data

    @verify_client
    def azerite_essence_media(self, locale: str, essence_id: int) -> Dict[str, Any]:
        """Returns media data for an azerite essence.

        Args:
            locale (str): which locale to use for the request
            essence_id (int): the azerite essence ID

        Returns:
            dict: json decoded media data for the azerite essence
        """
        data: Dict[str, Any] = self.client.media_data(
            locale, "static", "azerite-essence", essence_id
        )
        return data
