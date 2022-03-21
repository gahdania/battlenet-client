# Azerite Essence API


### battlenet_client.wow.game_data.azerite_essence(region_tag: str, \*, essence_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of azerite essences, or an azerite essence by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **essence_id** (*int**, **optional*) – the Azerite essence ID or the word ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.azerite_essence_media(region_tag: str, essence_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns media for an azerite essence by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **essence_id** (*int*) – the azerite essence ID


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.azerite_essence_search(region_tag: str, field_values: Dict[str, Any], \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Performs a search of azerite essences. For more detail see the search guide at:
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
