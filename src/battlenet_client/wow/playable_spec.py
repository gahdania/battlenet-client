"""Provides access to the playable specializations"""
from typing import Any, Dict, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from battlenet_client.wow.client import Client

from battlenet_client.wow.decorators import verify_client


class PlayableSpecAPI:
    def __init__(self, client: "Client") -> None:
        self.client = client

    @verify_client
    def playable_spec(
        self, locale: str, spec_id: Optional[int] = None
    ) -> Dict[str, Any]:
        """Returns an index of playable specialization, or a specific playable specialization

        Args:
            locale (str): which locale to use for the request
            spec_id (int, optional): the playable specialization's ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual playable specialization(s)
        """
        if spec_id is not None:
            data: Dict[str, Any] = self.client.game_data(
                locale, "static", "playable-specialization", spec_id
            )
        else:
            data = self.client.game_data(
                locale, "static", "playable-specialization", "index"
            )
        return data

    @verify_client
    def playable_spec_media(self, locale: str, spec_id: int) -> Dict[str, Any]:
        """Returns media for a playable specialization by ID.

        Args:
            locale (str): which locale to use for the request
            spec_id (int): specialization id

        Returns:
            dict: json decoded media data for the playable specialization
        """
        data: Dict[str, Any] = self.client.media_data(
            locale, "static", "playable-specialization", spec_id
        )
        return data
