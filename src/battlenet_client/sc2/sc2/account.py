"""Provides the access to the account API for the players in Starcraft2"""


from sc2_client.exceptions import SC2ClientError
from sc2_client.decorators import verify_client


class PlayerAPI:

    def __init__(self, client):
        self.client = client

    @verify_client
    def player(self, locale, account_id):
        """Returns the player data for the provided `account_id`.

        Args:
            locale (str): which locale to use for the request
            account_id (int): the account ID to request

        Returns:
            dict: json decoded data of the guild's achievement summary
        """
        if not self.client.auth_flow:
            raise SC2ClientError('Requires the authorized workflow')

        return self.client.community(locale, 'player', account_id)
