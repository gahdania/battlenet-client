# Profile API - NA, APAC, EU


### battlenet_client.sc2.community.static(region_tag: str, region_id: int, locale: Optional[str] = None)
Returns all static SC2 profile data (achievements, categories, criteria, and rewards).


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **region_id** (*str*) – region for the profile, or use sc2.constants  (used outside CN only)



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Raises**


    * **BNetRegionError** – when the region tag is ‘cn’


    * **BNetValueError** – when region ID is not valid



### battlenet_client.sc2.community.metadata(region_tag: str, region_id: int, realm_id: int, profile_id: int, locale: Optional[str] = None)
Returns metadata for an individual’s profile.


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



### battlenet_client.sc2.community.profile(region_tag: str, region_id: int, realm_id: int, profile_id: int, locale: Optional[str] = None)
Returns data about an individual SC2 profile.


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



### battlenet_client.sc2.community.ladder(region_tag: str, region_id: int, realm_id: int, profile_id: int, \*, ladder_id: Optional[Union[int, str]] = 'summary', locale: Optional[str] = None)
Returns a ladder summary, or specific ladder for an individual SC2 profile.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **region_id** (*int*) – region for the profile, or use sc2.constants


    * **realm_id** (*int*) – the realm of the profile (1 or 2)


    * **profile_id** (*int*) – the profile ID


    * **ladder_id** (*int**, **optional*) – the ID of a specific ladder, if desired



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Raises**


    * **BNetRegionError** – when the region tag is ‘cn’


    * **BNetValueError** – when region ID is not valid


# Profile API - CN


### battlenet_client.sc2.community_cn.profile(region_tag: str, profile_id: int, region_id: int, profile_name: str, locale: Optional[str] = None)
Returns data about an individual SC2 profile.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **region_id** (*int*) – region for the profile, or use sc2.constants


    * **profile_id** (*int*) – the profile ID


    * **profile_name** (*str*) – name to use with the CN endpoint



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Raises**

    **BNetRegionError** – when the region tag is not ‘cn’



### battlenet_client.sc2.community_cn.ladders(region_tag: str, profile_id: int, region_id: int, profile_name: str, locale: Optional[str] = None)
Returns a ladder summary, or specific ladder for an individual SC2 profile.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **region_id** (*int*) – region for the profile, or use sc2.constants


    * **profile_id** (*int*) – the profile ID


    * **profile_name** (*str*) – Name of the profile



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Raises**

    **BNetRegionError** – when the region tag is not ‘cn’



### battlenet_client.sc2.community_cn.match_history(region_tag: str, profile_id: int, region_id: int, profile_name: str, locale: Optional[str] = None)
Returns data about an individual SC2 profile’s match history.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **region_id** (*int*) – region for the profile, or use sc2.constants


    * **profile_id** (*int*) – the profile ID


    * **profile_name** (*str*) – profile name for the CN region request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Raises**

    **BNetRegionError** – when the region is not ‘cn’
