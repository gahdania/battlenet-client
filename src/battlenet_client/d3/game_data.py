"""Generates the URI/querystring and headers for the Diablo III API endpoints

Classes:
    GameData

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of Diablo III and any data
    retrieved from this API.
"""
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from requests import Response
    from client import D3Client


class GameData:
    def __init__(self, client: "D3Client") -> None:
        self.client = client

    def season(self, locale: str, season_id: Optional[int] = None) -> Response:
        """Returns an index of seasons, or a leaderboard of the specified season

        Args:
            locale (str): localization to use with API
            season_id (int): the ID of the season

        Returns:
            dict: the dict containing for the index of seasons, or the index of
                the leaderboards for the given season
        """
        if season_id:
            return self.client.game_data(locale, "season", season_id)

        return self.client.game_data(locale, "season/")

    def season_leaderboard(
        self, locale: str, season_id: int, leaderboard_id: str
    ) -> Response:
        """Returns the leaderboard for the specified season by slug

        Args:
            locale (str): localization to use with API
            season_id (int): the ID of the season
            leaderboard_id (Str): the slug of the leaderboard

        Returns:
            dict: the dict containing for the leaderboard for the given season
        """
        return self.client.game_data(
            locale, "season", season_id, "leaderboard", leaderboard_id
        )

    def era(self, locale: str, era_id: Optional[int] = None) -> Response:
        """Returns an index of eras, or index of leaderboards for the era

        Args:
            locale (str): localization to use with API
            era_id (int): the ID of the era

        Returns:
            dict: the dict containing for the index of sea, or the leaderboard
                for the given season
        """
        if era_id:
            return self.client.game_data(locale, "era", era_id)

        return self.client.game_data(locale, "era/")

    def era_leaderboard(
        self, locale: str, era_id: int, leaderboard_id: str
    ) -> Response:
        """Returns the leaderboard for the specified era by slug

        Args:
            locale (str): localization to use with API
            era_id (int): the ID of the season
            leaderboard_id (str): the slug of the leaderboard

        Returns:
            dict: the dict containing for the leaderboard for the given season
        """
        return self.client.game_data(
            locale, "era", era_id, "leaderboard", leaderboard_id
        )
