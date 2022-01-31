"""Provides access the PvP season API endpoints for World of Warcraft"""
from typing import Any, Dict, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from wow.client import WoWClient

from wow.decorators import verify_client
from wow.exceptions import WoWReleaseError


class PvPAPI:
    
    def __init__(self, client: 'WoWClient') -> None:
        self.client = client
        
    @verify_client
    def pvp_season(self, locale: str, season_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of pvp seasons, or a specific pvp season
    
        Args:
            locale (str): which locale to use for the request
            season_id (int, optional): the power type's ID or the word 'index'
    
        Returns:
            dict: json decoded data for the index/individual PvP season(s)
        """
        if season_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'dynamic', 'pvp-season', season_id)
        else:
            data = self.client.game_data(locale, 'dynamic', 'pvp-season', 'index')
        return data
    
    @verify_client
    def pvp_leader_board(self, locale: str, season_id: int, pvp_bracket: Optional[str] = None) -> Dict[str, Any]:
        """Returns an index of pvp leader boards, or a specific pvp leader board
    
        Args:
            locale (str): which locale to use for the request
            season_id (int): pvp season's ID
            pvp_bracket (int, optional): the PvP bracket to view ('2v2', '3v3', '5v5', 'rbg') or the word 'index'
            
        Returns:
            dict: json decoded data for the index of the PvP leader board
        """
        if pvp_bracket:
            data: Dict[str, Any] = self.client.game_data(locale, 'dynamic', 'pvp-season', season_id, 'pvp-leaderboard',
                                                         pvp_bracket)
        else:
            data = self.client.game_data(locale, 'dynamic', 'pvp-season', season_id, 'pvp-leaderboard', 'index')

        return data
    
    @verify_client
    def pvp_rewards_index(self, locale: str, season_id: int) -> Dict[str, Any]:
        """Returns an index of pvp rewards, or a specific pvp reward
    
        Args:
            locale (str): which locale to use for the request
            season_id (int): the season ID for the rewards or the word 'index'
    
        Returns:
            dict: json decoded data for the index of PvP rewards
        """
        data: Dict[str, Any] = self.client.game_data(locale, 'dynamic', 'pvp-season', season_id, 'pvp-reward', 'index')
        return data

    @verify_client
    def pvp_tier(self, locale: str, tier_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns an index of pvp tier, or a specific pvp tier

        Args:
            locale (str): which locale to use for the request
            tier_id (int, optional): the pvp tier ID or the default 'index'

        Returns:
            dict: the index or data for the pvp tier
        """

        if self.client.release in ('classic1x', 'classic'):
            raise WoWReleaseError(f"{self.client.release} does not support PvP tier API")

        if tier_id is not None:
            data: Dict[str, Any] = self.client.game_data(locale, 'static', 'pvp-tier', tier_id)
        else:
            data = self.client.game_data(locale, 'static', 'pvp-tier', 'index')

        return  data

    @verify_client
    def pvp_tier_media(self, locale: str, tier_id: int) -> Dict[str, Any]:
        """Returns media for a PvP tier by ID.

        Args:
            locale (str): which locale to use for the request
            tier_id (int): pvp tier id

        Returns:
            dict: json decoded media data for the PvP tier
        """

        if self.client.release in ('classic1x', 'classic'):
            raise WoWReleaseError(f"{self.client.release} does not support PvP tier API")

        data: Dict[str, Any] = self.client.media_data(locale, 'static', 'pvp-tier', tier_id)
        return data
