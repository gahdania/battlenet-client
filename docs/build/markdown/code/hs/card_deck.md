# Card Deck API


### battlenet_client.hs.game_data.card_deck(region_tag: str, field_values: Dict[str, Any], locale: Optional[str] = None)
Finds a deck by list of cards, including the hero.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **field_values** (*dict*) – search criteria, as key/value pairs
    For more information for the field names and options:
    [https://develop.battle.net/documentation/hearthstone/guides/decks](https://develop.battle.net/documentation/hearthstone/guides/decks)



* **Returns**

    json decoded search results that match field_values



* **Return type**

    dict
