# Media Search API


### battlenet_client.wow.game_data.media_search(region_tag: str, field_values: Dict[str, Any], \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Performs a search of all types of media documents. For more detail see the Search Guide.
[https://develop.battle.net/documentation/world-of-warcraft/guides/search](https://develop.battle.net/documentation/world-of-warcraft/guides/search)


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **field_values** (*dict*) – fields and values for the search criteria


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
