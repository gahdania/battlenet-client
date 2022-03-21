# Playable Race API


### battlenet_client.wow.game_data.playable_race(region_tag: str, \*, race_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of playable races, or a playable race by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **race_id** (*int**, **optional*) – the playable race’s ID or the word ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
