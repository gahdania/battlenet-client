# Reputation API


### battlenet_client.wow.game_data.reputation_faction(region_tag: str, \*, faction_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of reputation factions, or a single reputation faction by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **faction_id** (*int**, **optional*) – the slug or ID of the region_tag requested


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.reputation_tier(region_tag: str, \*, tier_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of reputation tiers, or a single set of reputation tiers by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **tier_id** (*int**, **optional*) – the slug or ID of the region_tag requested


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
