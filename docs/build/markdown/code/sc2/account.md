# Account API - NA, APAC, EU


### battlenet_client.sc2.community.player(region_tag: str, account_id: str, locale: Optional[str] = None)
Returns the player data for the provided account_id.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **account_id** (*int*) – the account ID to request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Raises**

    **BNetRegionError** – when the region tag is ‘cn’
