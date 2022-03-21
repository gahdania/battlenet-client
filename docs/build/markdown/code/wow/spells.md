# Spell API


### battlenet_client.wow.game_data.spell(region_tag: str, spell_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns a spell by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **spell_id** (*int*) – the slug or ID of the region_tag requested


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.spell_media(region_tag, spell_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns media for a spell by ID.


* **Parameters**


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **spell_id** (*int*) – pvp tier id



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.spell_search(region_tag: str, field_values: Dict[str, Any] = None, release: Optional[str] = 'retail', locale: Optional[str] = None)
Performs a search of spells. For more detail see the Search Guide.
[https://develop.battle.net/documentation/world-of-warcraft/guides/search](https://develop.battle.net/documentation/world-of-warcraft/guides/search)


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **field_values** (*dict*) – search criteria, as key/value pairs


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
