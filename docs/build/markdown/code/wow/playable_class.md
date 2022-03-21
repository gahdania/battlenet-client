# Playable Classes API


### battlenet_client.wow.game_data.playable_class(region_tag: str, \*, class_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of playable classes, or a playable class by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **class_id** (*int**, **optional*) – the class ID or the word ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.playable_class_media(region_tag: str, class_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns media for a playable class by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **class_id** (*int*) – class id


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.pvp_talent_slots(region_tag: str, class_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns the PvP talent slots for a playable class by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **class_id** (*int*) – class id


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.power_type(region_tag: str, \*, power_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of power types, or a power type by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **power_id** (*int**, **optional*) – the power type’s ID or the word ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
