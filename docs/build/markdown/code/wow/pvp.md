# PvP Season and Tier API


### battlenet_client.wow.game_data.pvp_season(region_tag: str, \*, season_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of PvP seasons, or a PvP season by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **season_id** (*int**, **optional*) – the power type’s ID or the word ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.pvp_regions(region_tag: str, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of PvP regions


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.pvp_regional_season(region_tag: str, pvp_region_id: int, \*, pvp_season_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of PvP regions


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **pvp_region_id** (*int*) – the regional PVP ID (use pvp_regions)


    * **pvp_season_id** (*int*) – the pvp season ID


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.pvp_leaderboard(region_tag, pvp_region_id: int, season_id: int, \*, pvp_bracket: Optional[str] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of PvP leaderboards for a PvP season, or
the PvP leaderboard of a specific PvP bracket for a PvP season.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **pvp_region_id** (*int*) – the regional PVP ID (use pvp_regions)


    * **season_id** (*int*) – pvp season’s ID


    * **pvp_bracket** (*int**, **optional*) – the PvP bracket to view (‘2v2’, ‘3v3’, ‘5v5’, ‘rbg’) or the word ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.pvp_rewards_index(region_tag: str, pvp_region_id: int, season_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of PvP rewards for a PvP season.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **pvp_region_id** (*int*) – the regional PVP ID (use pvp_regions)


    * **season_id** (*int*) – the season ID for the rewards or the word ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.pvp_tier(region_tag: str, \*, tier_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of PvP tiers, or a PvP tier by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **tier_id** (*int**, **optional*) – the pvp tier ID or the default ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.pvp_tier_media(region_tag, tier_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns media for a PvP tier by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **tier_id** (*int*) – pvp tier id


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
