# Item Type and Item API


### battlenet_client.d3.community.item_type(region_tag: str, \*, item_type_slug: Optional[str] = None, locale: Optional[str] = None)
Returns an index of item types, or a single item type by slug


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **item_type_slug** (*str**, **optional*) – the slug of an item type



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.d3.community.item(region_tag: str, item_slug: str, locale: Optional[str] = None)
Returns a single item by item slug and ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **item_slug** (*str*) – the slug of the item



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
