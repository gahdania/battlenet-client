"""provides access to the item API endpoints for World of Warcraft"""
from typing import Optional, Any, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from battlenet_client.wow.client import Client

from battlenet_client.wow.decorators import verify_client


class ItemAPI:
    def __init__(self, client: "Client") -> None:
        self.client = client

    @verify_client
    def item_class(self, locale: str, class_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of item classes, or a specific item class

        Args:
            locale (str): which locale to use for the request
            class_id (int, optional): item class ID or the default 'index'

        Returns:
            dict: json decoded data for the index/individual item class(es)
        """
        if class_id is not None:
            data: Dict[str, Any] = self.client.game_data(
                locale, "static", "item-class", class_id
            )
        else:
            data = self.client.game_data(locale, "static", "item-class", "index")

        return data

    @verify_client
    def item_set(self, locale: str, set_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of item sets, or a specific item set

        Args:
            locale (str): which locale to use for the request
            set_id (int, optional): the item class ID or the default 'index'

        Returns:
            dict: json decoded data for the index/individual item set(s)
        """
        if set_id is not None:
            data: Dict[str, Any] = self.client.game_data(
                locale, "static", "item-set", set_id
            )
        else:
            data = self.client.game_data(locale, "static", "item-set", "index")

        return data

    @verify_client
    def item_subclass(
        self, locale: str, class_id: int, subclass_id: int
    ) -> Dict[str, Any]:
        """Returns an index of item subclasses, or a specific item subclass

        Args:
            locale (str): which locale to use for the request
            class_id (int): the item class ID
            subclass_id (int, optional): the item's subclass ID

        Returns:
            dict: json decoded data for the item's subclass
        """
        data: Dict[str, Any] = self.client.game_data(
            locale, "static", "item-class", class_id, "item-subclass", subclass_id
        )
        return data

    @verify_client
    def item(self, locale: str, item_id: int) -> Dict[str, Any]:
        """Returns an index of items, or a specific item

        Args:
            locale (str): which locale to use for the request
            item_id (int, optional): the item class ID

        Returns:
            dict: json decoded data for the individual item
        """
        data: Dict[str, Any] = self.client.game_data(locale, "static", "item", item_id)
        return data

    @verify_client
    def item_media(self, locale: str, item_id: int) -> Dict[str, Any]:
        """Returns media for an item.

        Args:
            locale (str): which locale to use for the request
            item_id (int): the creature family ID

        Returns:
            dict: json decoded media data for the item
        """
        data: Dict[str, Any] = self.client.media_data(locale, "static", "item", item_id)
        return data

    @verify_client
    def item_search(self, locale: str, field_values: Dict[str, Any]):
        """Searches the item API for items that match the criteria

        Args:
            locale (str): which locale to use for the request
            field_values (dict): search criteria as key/value pairs

        Returns:
             dict: json decoded search results that match `field_values`
        """
        data: Dict[str, Any] = self.client.search(
            locale, "static", "item", field_values
        )
        return data
