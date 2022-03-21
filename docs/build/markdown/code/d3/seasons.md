# Season API


### battlenet_client.d3.game_data.season(region_tag: str, season_id: Optional[int] = None, locale: Optional[str] = None)
Returns an index of available seasons, or a leaderboard list for
the specified season.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **season_id** (*int*) – the ID of the season



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.d3.game_data.season_leaderboard(region_tag: str, season_id: int, leaderboard_id: str, locale: Optional[str] = None)
Returns the specified leaderboard for the specified season.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **season_id** (*int*) – the ID of the season


    * **leaderboard_id** (*Str*) – the slug of the leaderboard



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
