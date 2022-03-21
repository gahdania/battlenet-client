# Guild Tabard Components API


### battlenet_client.wow.game_data.guild_crest_components_index(region_tag: str, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of guild crest media.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.guild_crest_media(region_tag: str, category: str, icon_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns media for a guild crest border by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **category** (*str*) – either ‘border’ or ‘emblem’


    * **icon_id** (*int*) – the border ID


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
