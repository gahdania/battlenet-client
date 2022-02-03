"""Provides access to the guild API endpoints for World of Warcraft"""
from typing import Any, TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from battlenet_client.wow.client import Client

from battlenet_client.wow.decorators import verify_client
from battlenet_client.wow.exceptions import WoWReleaseError


class GuildAPI:
    def __init__(self, client: "Client") -> None:
        self.client = client

    @verify_client
    def guild(self, locale: str, realm_name: str, guild_name: str) -> Dict[str, Any]:
        """Returns a single guild by its name and realm.

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the name of the guild's realm
            guild_name (str): the name of the guild

        Returns:
            dict: json decoded data of the guild
        """
        if self.client.release != "retail":
            raise WoWReleaseError(
                f"{self.client.release} does not support the Guild Data API"
            )

        data: Dict[str, Any] = self.client.game_data(
            locale,
            "profile",
            "guild",
            self.client.slugify(realm_name),
            self.client.slugify(guild_name),
        )
        return data

    @verify_client
    def guild_activities(
        self, locale: str, realm_name: str, guild_name: str
    ) -> Dict[str, Any]:
        """Returns a single guild's activity by name and realm.

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the name of the guild's realm
            guild_name (str): the name of the guild

        Returns:
            dict: json decoded data of the guild activities
        """
        if self.client.release != "retail":
            raise WoWReleaseError(
                f"{self.client.release} does not support the Guild Data API"
            )

        data: Dict[str, Any] = self.client.game_data(
            locale,
            "profile",
            "guild",
            self.client.slugify(realm_name),
            self.client.slugify(guild_name),
            "activity",
        )
        return data

    @verify_client
    def guild_achievements(
        self, locale: str, realm_name: str, guild_name: str
    ) -> Dict[str, Any]:
        """Returns a single guild's achievements by name and realm.

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the name of the guild's realm
            guild_name (str): the name of the guild

        Returns:
            dict: json decoded data of the guild achievements
        """
        if self.client.release != "retail":
            raise WoWReleaseError(
                f"{self.client.release} does not support the Guild Data API"
            )

        data: Dict[str, Any] = self.client.game_data(
            locale,
            "profile",
            "guild",
            self.client.slugify(realm_name),
            self.client.slugify(guild_name),
            "achievements",
        )
        return data

    @verify_client
    def guild_roster(
        self, locale: str, realm_name: str, guild_name: str
    ) -> Dict[str, Any]:
        """Returns a single guild's roster by its name and realm.

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the name of the guild's realm
            guild_name (str): the name of the guild

        Returns:
            dict: json decoded data of the guild's achievement summary
        """
        if self.client.release != "retail":
            raise WoWReleaseError(
                f"{self.client.release} does not support the Guild Data API"
            )

        data: Dict[str, Any] = self.client.game_data(
            locale,
            "profile",
            "guild",
            self.client.slugify(realm_name),
            self.client.slugify(guild_name),
            "roster",
        )
        return data

    @verify_client
    def guild_crest_components_index(self, locale: str) -> Dict[str, Any]:
        """Returns an index of guild crest components.

        Args:
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data for the index of guild crest components
        """
        data: Dict[str, Any] = self.client.game_data(
            locale, "static", "guild-crest", "index"
        )
        return data

    @verify_client
    def guild_crest_border_media(self, locale: str, border_id: int) -> Dict[str, Any]:
        """Returns media for a specific guild crest border.

        Args:
            locale (str): which locale to use for the request
            border_id (int): the border ID

        Returns:
            dict: json decoded media data for the guild border
        """
        data: Dict[str, Any] = self.client.media_data(
            locale, "static", "guild-crest", "border", border_id
        )
        return data

    @verify_client
    def guild_crest_emblem_media(self, locale: str, crest_id: int) -> Dict[str, Any]:
        """Returns media for a specific guild crest emblem.

        Args:
            locale (str): which locale to use for the request
            crest_id (int): the border ID

        Returns:
            dict: json decoded media data for the guild crest
        """
        data: Dict[str, Any] = self.client.media_data(
            locale, "static", "guild-crest", "emblem", crest_id
        )
        return data
