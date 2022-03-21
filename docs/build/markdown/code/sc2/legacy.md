# Legacy Data API - NA, APAC, EU


### battlenet_client.sc2.community.legacy_profile(region_tag: str, region_id: int, realm_id: int, profile_id: int, locale: Optional[str] = None)
Retrieves data about an individual SC2 profile.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **region_id** (*int*) – region for the profile, or use sc2.constants


    * **realm_id** (*int*) – the realm of the profile (1 or 2)


    * **profile_id** (*int*) – the profile ID



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple

    Returns:

        tuple: The URL (str) and parameters (dict)




* **Raises**


    * **BNetRegionError** – when the region tag is ‘cn’


    * **BNetValueError** – when region ID is not valid



### battlenet_client.sc2.community.legacy_ladders(region_tag: str, region_id: int, realm_id: int, profile_id: int, locale: Optional[str] = None)
Retrieves data about an individual SC2 profile’s ladders.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **region_id** (*int*) – region for the profile, or use sc2.constants


    * **realm_id** (*int*) – the realm of the profile (1 or 2)


    * **profile_id** (*int*) – the profile ID



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Raises**


    * **BNetRegionError** – when the region tag is ‘cn’


    * **BNetValueError** – when region ID is not valid



### battlenet_client.sc2.community.legacy_match_history(region_tag: str, region_id: int, realm_id: int, profile_id: int, locale: Optional[str] = None)
Returns data about an individual SC2 profile’s match history.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **region_id** (*int*) – region for the profile, or use sc2.constants


    * **realm_id** (*int*) – the realm of the profile (1 or 2)


    * **profile_id** (*int*) – the profile ID



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Raises**


    * **BNetRegionError** – when the region tag is ‘cn’


    * **BNetValueError** – when region ID is not valid



### battlenet_client.sc2.community.legacy_ladder(region_tag: str, region_id: int, ladder_id: int, locale: Optional[str] = None)
Returns data about an individual SC2 profile’s match history.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **region_id** (*int*) – region for the profile, or use sc2.constants


    * **ladder_id** (*int*) – ladder ID for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Raises**


    * **BNetRegionError** – when the region tag is ‘cn’


    * **BNetValueError** – when region ID is not valid



### battlenet_client.sc2.community.legacy_achievements(region_tag: str, region_id: int, locale: Optional[str] = None)
Returns the player data for the provided account_id.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **region_id** (*int*) – the account ID to request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Raises**


    * **BNetRegionError** – when the region tag is ‘cn’


    * **BNetValueError** – when region ID is not valid



### battlenet_client.sc2.community.legacy_rewards(region_tag: str, region_id: int, locale: Optional[str] = None)
Returns the player data for the provided account_id.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **region_id** (*int*) – the account ID to request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Raises**


    * **BNetRegionError** – when the region tag is ‘cn’


    * **BNetValueError** – when region ID is not valid


# Data Resources API - CN


### battlenet_client.sc2.community_cn.achievements(region_tag: str, locale: Optional[str] = None)
Returns a ladder summary, or specific ladder for an individual SC2 profile.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Raises**

    **BNetRegionError** – when the region tag is not ‘cn’



### battlenet_client.sc2.community_cn.rewards(region_tag: str, locale: Optional[str] = None)
Returns a ladder summary, or specific ladder for an individual SC2 profile.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Raises**

    **BNetRegionError** – when the region tag is not ‘cn’
