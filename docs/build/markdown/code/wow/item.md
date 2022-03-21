# Item API


### battlenet_client.wow.game_data.item_class(region_tag: str, \*, class_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of item classes, or an item class by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **class_id** (*int**, **optional*) – item class ID or the default ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.item_set(region_tag: str, \*, set_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of item sets, or an item set by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **set_id** (*int**, **optional*) – the item class ID or the default ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.item_subclass(region_tag: str, class_id: int, subclass_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an item subclass by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **class_id** (*int*) – the item class ID


    * **subclass_id** (*int**, **optional*) – the item’s subclass ID


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.item(region_tag: str, item_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an item by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **item_id** (*int**, **optional*) – the item class ID


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.item_media(region_tag: str, item_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an item by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **item_id** (*int*) – the creature family ID


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.item_search(region_tag, field_values: Dict[str, Any], \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Performs a search of items. For more detail see the search guide.
[https://develop.battle.net/documentation/world-of-warcraft/guides/search](https://develop.battle.net/documentation/world-of-warcraft/guides/search)


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **field_values** (*dict*) – search criteria as key/value pairs


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
