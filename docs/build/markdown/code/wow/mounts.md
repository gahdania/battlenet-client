# Mounts API


### battlenet_client.wow.game_data.mount(region_tag: str, \*, mount_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of mounts, or a mount by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **mount_id** (*int**, **optional*) – the mount ID or ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.mount_search(region_tag: str, field_values: Dict[str, Any], \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Performs a search of mounts. For more detail see the Search Guide.
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
