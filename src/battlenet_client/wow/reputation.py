"""Provides access to the Reputation API endpoints"""
from typing import Any, Dict, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from battlenet_client.wow.client import Client

from battlenet_client.wow.decorators import verify_client


class ReputationAPI:
    def __init__(self, client: "Client") -> None:
        self.client = client

    @verify_client
    def reputation_faction(
        self, locale: str, faction_id: Optional[int] = None
    ) -> Dict[str, Any]:
        """Returns an index of reputation factions, or a specific reputation fa

        Args:
            locale (str): which locale to use for the request
            faction_id (int, optional): the slug or ID of the region requested

        Returns:
            dict: json decoded data for the index/individual reputation faction(s)
        """
        if faction_id is not None:
            data: Dict[str, Any] = self.client.game_data(
                locale, "static", "reputation-faction", faction_id
            )
        else:
            data = self.client.game_data(
                locale, "static", "reputation-faction", "index"
            )
        return data

    @verify_client
    def reputation_tier(
        self, locale: str, tier_id: Optional[int] = None
    ) -> Dict[str, Any]:
        """Returns an index of reputation factions, or a specific reputation fa

        Args:
            locale (str): which locale to use for the request
            tier_id (int, optional): the slug or ID of the region requested

        Returns:
            dict: json decoded data for the index/individual reputation tier(s)
        """
        if tier_id is not None:
            data: Dict[str, Any] = self.client.game_data(
                locale, "static", "reputation-tiers", tier_id
            )
        else:
            data = self.client.game_data(locale, "static", "reputation-tiers", "index")
        return data
