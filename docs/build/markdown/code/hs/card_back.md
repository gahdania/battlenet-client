# Card Back API


### battlenet_client.hs.game_data.card_back(region_tag: str, card_back_id: str, locale: Optional[str] = None)
Returns a specific card back by using card back ID or slug.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **card_back_id** (*int**, **str*) – the ID or full slug of the card back



* **Returns**

    json decoded data for the card back identified by card_back_id



* **Return type**

    dict



### battlenet_client.hs.game_data.card_back_search(region_tag: str, field_values: Dict[str, Any], locale: Optional[str] = None)
Returns an up-to-date list of all card backs matching the search criteria.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **field_values** (*dict*) – search criteria, as key/value pairs
    For more information for the field names and options:
    [https://develop.battle.net/documentation/hearthstone/guides/card-backs](https://develop.battle.net/documentation/hearthstone/guides/card-backs)



* **Returns**

    json decoded search results that match field_values



* **Return type**

    dict
