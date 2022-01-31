"""Provides access to the auction houses API game_data for World of Warcraft"""
from typing import Optional, Any, TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from wow.client import WoWClient

from wow.decorators import verify_client
from wow.exceptions import WoWReleaseError


class AuctionAPI:
    
    def __init__(self, client: 'WoWClient') -> None:
        self.client = client
    
    @verify_client
    def auction(self, locale: str, connected_realm_id: int, auction_house_id: Optional[int] = None) -> Dict[str, Any]:
        """Returns auction data.  With retail client, it returns all of the auctions for the given connected realm.
        For classic titles, the results can be either the entire list, or the individual auctions

        See the Connected Realm API for information about retrieving a list of
            connected realm IDs.

        Auction house data updates at a set interval. The value was initially set
            at 1 hour; however, it might change over time without notice.

        Depending on the number of active auctions on the specified connected realm,
            the response from this game_data may be rather large, sometimes exceeding
            10 MB.

        Args:
            locale (str): which locale to use for the request
            connected_realm_id (int): the id of the connected realm
            auction_house_id (int, optional): the ID of the auction house

        Returns:
            dict: json decoded data for the index/individual auction(s)

        Raises:
            WoWClientError: when a client other than WoWClient is used.
            WoWReleaseError: when an AH ID is used for the retail client

        Notes:
            Auction house functionality is not available for WoW 1.x (Vanilla Classic)
        """
        if self.client.release == 'retail' and auction_house_id is None:
            data: Dict[str, Any] = self.client.game_data(locale, 'dynamic', 'connected-realm', connected_realm_id,
                                                         'auctions')

        if self.client.release != 'retail' and auction_house_id is None:
            data = self.client.game_data(locale, 'dynamic', 'connected-realm', connected_realm_id, 'auctions', 'index')

        if self.client.release != 'retail' and auction_house_id is not None:
            data = self.client.game_data(locale, 'dynamic', 'connected-realm', connected_realm_id, 'auctions',
                                         auction_house_id)

        if self.client.release == 'retail' and auction_house_id is not None:
            raise WoWReleaseError("Auction House ID provided for retail")

        return data
