# Card API


### battlenet_client.hs.game_data.card(region_tag: str, card_id: str, \*, game_mode: Optional[str] = 'constructed', locale: Optional[str] = None)
Returns the card with an ID or slug that matches the one you specify.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **card_id** (*int**, **str*) – the ID or full slug of the card


    * **game_mode** (*str**, **optional*) – the game mode
    See for more information:
    [https://develop.battle.net/documentation/hearthstone/guides/game-modes](https://develop.battle.net/documentation/hearthstone/guides/game-modes)



* **Returns**

    json decoded data for the index/individual azerite essence(s)



* **Return type**

    dict



### battlenet_client.hs.game_data.card_search(region_tag: str, field_values: Dict[str, Any], locale: Optional[str] = None)
Returns an up-to-date list of all cards matching the search criteria.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **field_values** (*dict*) – search criteria, as key/value pairs
    For more information for the field names and options:
    [https://develop.battle.net/documentation/hearthstone/game-data-apis](https://develop.battle.net/documentation/hearthstone/game-data-apis)



* **Returns**

    json decoded search results that match field_values



* **Return type**

    dict
