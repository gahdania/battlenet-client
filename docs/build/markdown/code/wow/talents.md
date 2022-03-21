# Talent API


### battlenet_client.wow.game_data.talent(region_tag: str, \*, talent_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of talents, or a talent by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **talent_id** (*int**, **optional*) – the slug or ID of the region_tag requested


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.pvp_talent(region_tag: str, \*, pvp_talent_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of PvP talents, or a PvP talent by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **pvp_talent_id** (*int**, **optional*) – the slug or ID of the region_tag requested


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple


# Tech Talent API


### battlenet_client.wow.game_data.tech_talent_tree(region_tag: str, \*, tree_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of tech talent trees, or a tech talent tree by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **tree_id** (*int**, **optional*) – the slug or ID of the region_tag requested


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.tech_talent(region_tag: str, \*, talent_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of tech talents, or a tech talent by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **talent_id** (*int**, **optional*) – the slug or ID of the region_tag requested


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.tech_talent_media(region_tag: str, talent_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns media for a tech talent by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **talent_id** (*int*) – pvp tier id


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
