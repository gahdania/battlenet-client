"""Provides access to the API endpoints that are not game specific

.. moduleauthor: David "Gahd" Couples <gahdania@gahd.io>
"""
from typing import Optional, Any, TYPE_CHECKING, List, Dict

if TYPE_CHECKING:
    from battlenet_client.client import BattleNetClient

from battlenet_client.exceptions import BNetClientError


class BattleNetAPI(BattleNetClient):

    def __init__(self, region: str, game: Dict[str, str], *, client_id: Optional[str] = None,
                 client_secret: Optional[str] = None, scope: Optional[List[str]] = None,
                 redirect_uri: Optional[str] = None) -> None:
        super().__init__(region, game, client_id=client_id, client_secret=client_secret, scope=scope,
                         redirect_uri=redirect_uri)

    def user_info(self, locale: Optional[str] = None) -> Any:
        """Returns the user info

        Args:
            locale (str): localization to use

        Returns:
            dict: the json decoded information for the user (user # and battle tag ID)

        Notes:
            this function requires the BattleNet Client to be use OAuth (Authentication Workflow)
        """
        if not self.auth_flow:
            raise BNetClientError("Requires Authorization Code Workflow")

        url = f"{self.auth_host}/oauth/userinfo"
        return self._get(url, params={'locale': locale})
