# Account and Hero API


### battlenet_client.d3.community.api_account(region_tag: str, bnet_tag: str, locale: Optional[str] = None)
Returns the specified account profile.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **bnet_tag** (*str*) – bnet tag of the user



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.d3.community.api_hero(region_tag: str, bnet_tag: str, hero_id: str, \*, category: Optional[str] = None, locale: Optional[str] = None)
Returns a single hero, a list of items for the specified hero, or
list of items for the specified hero’s followers.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **bnet_tag** (*str*) – BNet tag for the account


    * **hero_id** (*str*) – Hero’s ID


    * **category** (*str*) – category to retrieve if specified (‘items’, ‘follower-items’)



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Raises**

    **BNetValueError** – category is not None and not ‘items’ or ‘follower-items’
