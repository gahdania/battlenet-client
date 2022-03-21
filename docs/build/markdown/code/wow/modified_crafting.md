# Modified Crafting API


### battlenet_client.wow.game_data.modified_crafting(region_tag: str, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns the parent index for Modified Crafting.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.modified_crafting_category(region_tag: str, \*, category_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns the index of Modified Crafting categories, or a Modified Crafting category by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **category_id** (*int**, **optional*) – the encounter ID or ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.modified_crafting_reagent_slot_type(region_tag: str, \*, slot_type_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns the index of Modified Crafting reagent slot types, or a Modified Crafting reagent slot type by ID


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **slot_type_id** (*int**, **optional*) – the encounter ID or ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
