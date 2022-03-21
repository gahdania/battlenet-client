# Era API


### battlenet_client.d3.game_data.era(region_tag: str, era_id: Optional[int] = None, locale: Optional[str] = None)
Returns an index of available eras, or a leaderboard list for a
particular era.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **era_id** (*int*) – the ID of the era



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.d3.game_data.era_leaderboard(region_tag: str, era_id: int, leaderboard_id: str, locale: Optional[str] = None)
Returns the specified leaderboard for the specified era.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **era_id** (*int*) – the ID of the season


    * **leaderboard_id** (*str*) – the slug of the leaderboard



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
