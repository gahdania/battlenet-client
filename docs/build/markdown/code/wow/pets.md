# Pet API


### battlenet_client.wow.game_data.pet(region_tag: str, \*, pet_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of battle pets, or a battle pet by ID.


* **Parameters**


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **pet_id** (*int**, **optional*) – the pet ID or the word ‘index’



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.pet_media(region_tag: str, pet_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns media for a battle pet by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **pet_id** (*int*) – the azerite pet ID


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.pet_ability(region_tag: str, \*, pet_ability_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of pet abilities, or a pet ability by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **pet_ability_id** (*int**, **optional*) – the pet ID or the word ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.pet_ability_media(region_tag: str, ability_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns media for a pet ability by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **ability_id** (*int*) – the azerite ability ID


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
