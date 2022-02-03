"""Provides access to the realm related API endpoints"""
from typing import Any, Dict, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from battlenet_client.wow.client import Client

from battlenet_client.wow.decorators import verify_client


class RealmAPI:
    def __init__(self, client: "Client") -> None:
        self.client = client

    @verify_client
    def realm(self, locale: str, realm_name: Optional[str] = None) -> Dict[str, Any]:
        """Returns an index of realms, or a specific realm

        Args:
            locale (str): which locale to use for the request
            realm_name (str, optional): the pvp tier ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual realm(s)
        """
        if realm_name is not None:
            data: Dict[str, Any] = self.client.game_data(
                locale, "dynamic", "realm", self.client.slugify(realm_name)
            )
        else:
            data = self.client.game_data(locale, "dynamic", "realm", "index")
        return data

    @verify_client
    def realm_search(self, locale: str, field_values: Dict[str, Any]) -> Dict[str, Any]:
        """Searches the creature API for connected realm(s) that match the criteria

        Args:
            locale (str): which locale to use for the request
            field_values (dict): search criteria, as key/value pairs

        Returns:
            dict: json decoded search results that match `field_values`
        """
        data: Dict[str, Any] = self.client.search(
            locale, "dynamic", "realm", field_values
        )
        return data
