# Title API


### battlenet_client.wow.game_data.title(region_tag: str, \*, title_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of titles, or a title by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **title_id** (*int**, **optional*) – the slug or ID of the region_tag requested


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
