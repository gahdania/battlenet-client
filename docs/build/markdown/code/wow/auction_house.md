# Auction House API


### battlenet_client.wow.game_data.auction(region_tag: str, connected_realm_id: int, \*, auction_house_id: Optional[int] = None, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns all active auctions for a connected realm.

See the Connected Realm API for information about retrieving a list of connected realm IDs.
Auction house data updates at a set interval. The value was initially set at 1 hour;
however, it might change over time without notice.

Depending on the number of active auctions on the specified connected realm, the response
from this endpoint may be rather large, sometimes exceeding 10 MB.

See the Connected Realm utils.api for information about retrieving a list of
connected realm IDs.

Auction house data updates at a set interval. The value was initially set
at 1 hour; however, it might change over time without notice.

Depending on the number of active auctions on the specified connected realm,
the response from this game_data may be rather large, sometimes exceeding
10 MB.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **connected_realm_id** (*int*) – the id of the connected realm


    * **auction_house_id** (*int**, **optional*) – the ID of the auction house


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Raises**

    **exceptions.BNetReleaseError** – when an AH ID is used for the retail


### Notes

Auction house functionality is not available for WoW 1.x (Vanilla Classic)
