# Playable Specializations API


### battlenet_client.wow.game_data.playable_spec(region_tag: str, \*, spec_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of playable specializations, or a playable specialization by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **spec_id** (*int**, **optional*) – the playable specialization’s ID or the word ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.playable_spec_media(region_tag: str, spec_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns media for a playable specialization by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **spec_id** (*int*) – specialization id


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
