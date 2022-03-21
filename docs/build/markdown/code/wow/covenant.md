# Covenant API


### battlenet_client.wow.game_data.covenant(region_tag: str, \*, covenant_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of covenants, or a covenant by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **covenant_id** (*int**, **optional*) – the ID of the covenant or the default ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.covenant_media(region_tag: str, covenant_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns media for a covenant by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **covenant_id** (*int**, **optional*) – the covenant ID


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.soulbind(region_tag: str, \*, soulbind_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of soulbinds, or a soulbind by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **soulbind_id** (*int**, **optional*) – the ID of the soulbind or the word of ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.conduit(region_tag: str, \*, conduit_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of conduits, or a conduit by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **conduit_id** (*int**, **optional*) – the ID of the conduit or the word of ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
