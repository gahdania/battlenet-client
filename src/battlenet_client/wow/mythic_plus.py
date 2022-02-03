"""Provides access the Mythic + Keystone Affix API endpoints for the World of Warcraft"""
from typing import Any, Dict, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from battlenet_client.wow.client import Client

from battlenet_client.wow.decorators import verify_client


class MythicPlusAPI:
    def __init__(self, client: "Client") -> None:
        self.client = client

    @verify_client
    def mythic_keystone_affix(
        self, locale: str, affix_id: Optional[int] = None
    ) -> Dict[str, Any]:
        """Returns an index of mythic keystone affixes, or a specific mythic keystone affix

        Args:
            locale (str): which locale to use for the request
            affix_id (int, optional): the affix's ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual mythic keystone affix(es)
        """
        if affix_id is not None:
            data: Dict[str, Any] = self.client.game_data(
                locale, "static", "keystone-affix", affix_id
            )
        else:
            data = self.client.game_data(locale, "static", "keystone-affix", "index")
        return data

    @verify_client
    def mythic_keystone_affix_media(self, locale: str, affix_id: int) -> Dict[str, Any]:
        """Returns media for a mythic keystone affix.

        Args:
            locale (str): which locale to use for the request
            affix_id (int): the affix's ID

        Returns:
            dict: json decoded media data for the mythic keystone affix(es)
        """
        data: Dict[str, Any] = self.client.media_data(
            locale, "static", "keystone-affix", affix_id
        )
        return data

    @verify_client
    def mythic_keystone_dungeon(
        self, locale: str, dungeon_id: Optional[int] = None
    ) -> Dict[str, Any]:
        """Returns an index of mythic keystone dungeons, or a specific mythic keystone dungeon

        Args:
            locale (str): which locale to use for the request
            dungeon_id (int, optional): the dungeon's ID or 'index'

        Returns:
            dict: json decoded data for the index/individual mythic keystone dungeon(s)
        """
        if dungeon_id is not None:
            data: Dict[str, Any] = self.client.game_data(
                locale, "dynamic", "mythic-keystone", "dungeon", dungeon_id
            )
        else:
            data = self.client.game_data(
                locale, "dynamic", "mythic-keystone", "dungeon", "index"
            )
        return data

    @verify_client
    def mythic_keystone_index(self, locale: str) -> Dict[str, Any]:
        """Returns an index of links to other documents related to Mythic Keystone dungeons.

        Args:
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data for the index of the mythic keystone dungeon documents
        """
        data: Dict[str, Any] = self.client.game_data(
            locale, "dynamic", "mythic-keystone", "index"
        )
        return data

    @verify_client
    def mythic_keystone_period(
        self, locale: str, period_id: Optional[int] = None
    ) -> Dict[str, Any]:
        """Returns an index of mythic keystone periods, or a specific mythic keystone period

        Args:
            locale (str): which locale to use for the request
            period_id (int, optional): the keystone's period ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual for mythic keystone period(s)
        """
        if period_id is not None:
            data: Dict[str, Any] = self.client.game_data(
                locale, "dynamic", "mythic-keystone", "period", period_id
            )
        else:
            data = self.client.game_data(
                locale, "dynamic", "mythic-keystone", "period", "index"
            )
        return data

    @verify_client
    def mythic_keystone_season(
        self, locale: str, season_id: Optional[int] = None
    ) -> Dict[str, Any]:
        """Returns an index of mythic keystone seasons, or a specific mythic keystone seasons

        Args:
            locale (str): which locale to use for the request
            season_id (int, optional): the keystone's season ID or the word 'index'

        Returns:
            dict: json decoded data for the index/individual mythic keystone season(s)
        """
        if season_id is not None:
            data: Dict[str, Any] = self.client.game_data(
                locale, "dynamic", "mythic-keystone", "season", season_id
            )
        else:
            data = self.client.game_data(
                locale, "dynamic", "mythic-keystone", "season", "index"
            )
        return data

    @verify_client
    def mythic_keystone_leader_board(
        self,
        locale: str,
        connected_realm_id: int,
        dungeon_id: Optional[int] = None,
        period_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Returns an index of mythic keystone leader boards, or a specific mythic keystone leader board

        Args:
            connected_realm_id (int): the connected realm's id
            locale (str): which locale to use for the request, default is None, using the client's locale
            dungeon_id (int, optional): the particular dungeon's ID or the word 'index'
            period_id (int, optional): the particular period to search or None when looking for the index

        Returns:
            dict: json decoded data for the index/individual mythic keystone leaderboard(s)
        """
        if dungeon_id and period_id:
            data: Dict[str, Any] = self.client.game_data(
                locale,
                "dynamic",
                "connected-realm",
                connected_realm_id,
                "mythic-leaderboard",
                dungeon_id,
                "period",
                period_id,
            )
        else:
            data = self.client.game_data(
                locale,
                "dynamic",
                "connected-realm",
                connected_realm_id,
                "mythic-leaderboard",
                "index",
            )
        return data
