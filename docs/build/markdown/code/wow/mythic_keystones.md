# Mythic Keystone Affix API


### battlenet_client.wow.game_data.mythic_keystone_affix(region_tag: str, \*, affix_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of mythic keystone affixes. or a mythic keystone affix by ID


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **affix_id** (*int**, **optional*) – the affix’s ID or the word ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.mythic_keystone_affix_media(region_tag: str, affix_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns media for a mythic keystone affix by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **affix_id** (*int*) – the affix’s ID


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple


# Mythic Keystone Dungeon API


### battlenet_client.wow.game_data.mythic_keystone_dungeon(region_tag: str, \*, dungeon_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of Mythic Keystone dungeons, or a Mythic Keystone dungeon by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **dungeon_id** (*int**, **optional*) – the dungeon’s ID or ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.mythic_keystone_index(region_tag: str, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of links to other documents related to Mythic Keystone dungeons.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.mythic_keystone_period(region_tag: str, \*, period_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of Mythic Keystone periods, or a Mythic Keystone period by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **period_id** (*int**, **optional*) – the keystone’s period ID or the word ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.mythic_keystone_season(region_tag: str, \*, season_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of Mythic Keystone seasons, or a Mythic Keystone season by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **season_id** (*int**, **optional*) – the keystone’s season ID or the word ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.mythic_keystone_leaderboard(region_tag: str, connected_realm_id: int, \*, dungeon_id: Optional[Union[int, str]] = None, period_id: Optional[Union[int, str]] = None, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of Mythic Keystone Leaderboard dungeon instances for a connected realm,
or a weekly Mythic Keystone Leaderboard by period.


* **Parameters**


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **connected_realm_id** (*int*) – the connected realm’s id


    * **dungeon_id** (*int**, **optional*) – the particular dungeon’s ID or the word ‘index’


    * **period_id** (*int**, **optional*) – the particular period to search or None when looking for the index



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
