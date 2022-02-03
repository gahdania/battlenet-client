"""Provides access to Talent API endpoints"""
from typing import Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from battlenet_client.wow.client import Client

from battlenet_client.wow.decorators import verify_client


class TalentAPI:
    def __init__(self, client: "Client") -> None:
        self.client = client

    @verify_client
    def talent(self, locale: str, talent_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of spells, or a specific spell

        Args:
            locale (str): which locale to use for the request
            talent_id (int, optional): the slug or ID of the region requested

        Returns:
            dict: json decoded data for the index/individual talent(s)
        """
        if talent_id is not None:
            data: Dict[str, Any] = self.client.game_data(
                locale, "static", "talent", talent_id
            )
        else:
            data = self.client.game_data(locale, "static", "talent", "index")
        return data

    @verify_client
    def pvp_talent(
        self, locale: str, pvp_talent_id: Optional[int] = None
    ) -> Dict[str, Any]:
        """Returns an index of spells, or a specific spell

        Args:
            locale (str): which locale to use for the request
            pvp_talent_id (int, optional): the slug or ID of the region requested

        Returns:
            dict: json decoded data for the index/individual Talent talent(s)
        """
        if pvp_talent_id is not None:
            data: Dict[str, Any] = self.client.game_data(
                locale, "static", "pvp-talent", pvp_talent_id
            )
        else:
            data = self.client.game_data(locale, "static", "pvp-talent", "index")
        return data
