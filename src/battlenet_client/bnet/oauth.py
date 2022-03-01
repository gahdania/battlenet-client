"""defines the methods for accessing user data from Battle.net

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of Diablo III and any data
    retrieved from this API.
"""

from typing import Optional

from battlenet_client import utils


class OAuth:
    @staticmethod
    def user_info(client, region_tag: str, locale: Optional[str] = None):
        """Returns the user info

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request

        Returns:
            dict: the json decoded information for the user (user # and battle tag ID)

        Notes:
            this function requires the BattleNet Client to be use OAuth (Authentication Workflow)
        """

        url = f"{utils.auth_host(region_tag)}/oauth/userinfo"
        params = {"locale": utils.localize(locale)}

        try:
            return client.post(url, params=params)
        except AttributeError:
            return client.fetch_protected_resource(url, "POST", params=params)
