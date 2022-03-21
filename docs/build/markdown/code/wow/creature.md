# Creature API


### battlenet_client.wow.game_data.creature_family(region_tag: str, \*, family_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of creature families, or a creature family by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **family_id** (*int**, **optional*) – the creature family ID or the default ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.creature_type(region_tag: str, \*, type_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of creature types, or a creature type by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **type_id** (*int**, **optional*) – the creature type ID or the default ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.creature(region_tag: str, creature_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns a creature by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **creature_id** (*int**, **optional*) – the creature ID


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.creature_search(region_tag: str, field_values: Dict[str, Any], \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Performs a search of creatures. For more detail see the search guide

    [https://develop.battle.net/documentation/world-of-warcraft/guides/search](https://develop.battle.net/documentation/world-of-warcraft/guides/search)


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **field_values** (*dict*) – matching criteria in key/value pairs


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.creature_display_media(region_tag: str, display_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns media for a creature display by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **display_id** (*int**, **optional*) – the creature display ID


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.creature_family_media(region_tag: str, family_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns media for a creature family by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **family_id** (*int**, **optional*) – the creature family ID


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
