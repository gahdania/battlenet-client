"""Bnet Oauth Clients handle the processing on the requests with the Developer Portal API

.. moduleauthor: David "Gahd" Couples <gahdania@gahd.io>
"""
from typing import List, Optional, Any, Dict

from client import BNetClient
import exceptions


class BNetOauth(BNetClient):
    """Handles the communication using OAuth v2 client to the Battle.net REST API

    Args:
        region (str): region abbreviation for use with the APIs
        game (dict): the game for the request
        client_id (str): the client ID from the developer portal
        client_secret (str): the client secret from the developer portal

    Keyword Args:
        scope (list, optional): the scope or scopes to use during the endpoints that require the Web Application Flow
        redirect_uri (str, optional): the URI to return after a successful authentication between the user and Blizzard
    """

    def __init__(
        self,
        region: str,
        game: Dict[str, str],
        *,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        scope: Optional[List[str]] = None,
        redirect_uri: Optional[str] = None,
    ) -> None:
        super().__init__(
            region,
            game,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
            redirect_uri=redirect_uri,
        )

    __class_name = "oauth"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} Instance: {self.game['abbrev']}"

    def user_info(self, locale: Optional[str] = None) -> Dict[str, Any]:
        """Returns the user info

        Args:
            locale (str): localization to use

        Returns:
            dict: the json decoded information for the user (user # and battle tag ID)

        Notes:
            this function requires the BattleNet Client to be use OAuth (Authentication Workflow)
        """
        if not self.auth_flow:
            raise exceptions.BNetClientError("Requires Authorization Code Workflow")

        url = f"{self.auth_host}/oauth/userinfo"
        return self._get(url, params={"locale": locale})
