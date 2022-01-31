"""Provides access to the data resources for achievements and rewards"""

from sc2_client.decorators import verify_client
from sc2_client.exceptions import SC2RegionError


class CNDataResourceAPI:

    def __init__(self, client):
        if client.tag != 'cn':
            raise SC2RegionError("Invalid region for API")

        self.client = client

    @verify_client
    def achievements(self, locale):
        """Returns the achievements for Starcraft II

        Args:
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data of the guild's achievement summary
        """

        return self.client.community(locale, 'data', 'achievements')

    @verify_client
    def rewards(self, locale):
        """Returns the rewards of the achievements in Starcrft II

        Args:
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data of the guild's achievement summary
        """
        if self.client.region != 5:
            raise SC2RegionError("This API is available in this region")

        return self.client.community(locale, 'data', 'rewards')
