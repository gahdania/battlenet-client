"""Provides access the Mythic Raid Leader Board API endpoints"""
from typing import Any, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from wow_api.client import WoWClient

from wow_api.decorators import verify_client


class MythicRaidAPI:
    
    def __init__(self, client: 'WoWClient') -> None:
        self.client = client
    
    @verify_client
    def mythic_raid_leaderboard(self, locale: str, raid_name: str, faction: str) -> Dict[str, Any]:
        """Returns an index of mythic keystone affixes, or a specific mythic keystone affix
    
        Args:
            locale (str, optional): which locale to use for the request, default is None, using the client's locale
            raid_name (str): name of the raid
            faction (str): horde or alliance, defaults to alliance
    
        Returns:
            dict: json decoded data for the index/individual mythic raid
        """
        data: Dict[str, Any] = self.client.game_data(locale, 'dynamic', 'leaderboard', 'hall-of-fame',
                                                     self.client.slugify(raid_name), faction)
        return data