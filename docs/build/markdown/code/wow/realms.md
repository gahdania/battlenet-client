# Realm API


### battlenet_client.wow.game_data.realm(region_tag: str, \*, realm_slug: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of realms, or a single realm by slug or ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **realm_slug** (*str/int**, **optional*) – the pvp tier ID or the word ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.realm_search(region_tag, field_values: Dict[str, Any], \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Performs a search of realms. For more detail see the Search Guide.
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


# Connected Realm API


### battlenet_client.wow.game_data.connected_realm(region_tag: str, \*, connected_realm_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of connected realms, or a connected realm by ID.

A connected realm is a collection of realms operating as one larger realm


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **connected_realm_id** (*int**, **optional*) – the ID of the connected realm


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.connected_realm_search(region_tag: str, field_values: Dict[str, Any], \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Performs a search of connected realms. For more detail see the search guide:
[https://develop.battle.net/documentation/world-of-warcraft/guides/search](https://develop.battle.net/documentation/world-of-warcraft/guides/search)


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **field_values** (*dict*) – field/value pairs


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
