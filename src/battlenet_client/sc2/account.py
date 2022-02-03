"""Provides the access to the account API for the players in Starcraft2"""


from typing import Any, TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from battlenet_client.sc2.client import SC2Client

from battlenet_client.sc2.decorators import verify_client
from battlenet_client.sc2.exceptions import SC2ClientError


class PlayerAPI:
    def __init__(self, client: "SC2Client") -> None:
        self.client = client

    @verify_client
    def player(self, locale: str, account_id: int) -> Dict[str, Any]:
        """Returns the player data for the provided `account_id`.

        Args:
            locale (str): which locale to use for the request
            account_id (int): the account ID to request

        Returns:
            dict: json decoded data of the guild's achievement summary
        """
        if not self.client.auth_flow:
            raise SC2ClientError("Requires the authorized workflow")

        return self.client.community(locale, "player", account_id)
