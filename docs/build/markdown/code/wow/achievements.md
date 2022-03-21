# Achievement API


### battlenet_client.wow.game_data.achievement(region_tag: str, \*, achievement_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of achievements, or an achievement by ID


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **achievement_id** (*int**, **optional*) – the achievement ID or the word ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.achievement_category(region_tag: str, \*, category_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of achievement categories, or an achievement category by ID


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **category_id** (*int**, **optional*) – the achievement’s category ID or None (default).
    None will retrieve the entire list of achievement categories


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.achievement_media(region_tag: str, achievement_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns media for an achievement by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **achievement_id** (*int*) – the achievement ID or the word ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
