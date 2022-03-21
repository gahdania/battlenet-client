# Region API


### battlenet_client.wow.game_data.region(region_tag: str, \*, region_req: Optional[int] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of regions, or a region by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **region_req** (*int**, **optional*) – the region_tag ID or the word ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
