# Quest API


### battlenet_client.wow.game_data.quest(region_tag: str, \*, quest_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns the parent index for quests, or a quest by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **quest_id** (*int**, **optional*) – the quest ID or the word ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.quest_category(region_tag: str, \*, quest_category_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of quest categories (such as quests for a specific class, profession, or storyline),
or a quest category by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **quest_category_id** (*int**, **optional*) – the quest category ID or the word ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.quest_area(region_tag: str, \*, quest_area_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of quest areas, or a quest area by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **quest_area_id** (*int**, **optional*) – the quest area ID or the word ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.quest_type(region_tag: str, \*, quest_type_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of quest types (such as PvP quests, raid quests, or account quests),
or a quest type by ID.


* **Parameters**


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **quest_type_id** (*int**, **optional*) – the quest type ID or the word ‘index’



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
