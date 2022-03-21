# Ladder API - NA, APAC, EU


### battlenet_client.sc2.community.grandmaster(region_tag: str, region_id: int, locale: Optional[str] = None)
Returns ladder data for the current season’s grandmaster leaderboard.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **region_id** (*int*) – region for the profile, or use sc2.constants



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



### battlenet_client.sc2.community.season(region_tag: str, region_id: int, locale: Optional[str] = None)
Returns data about the current season.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **region_id** (*int*) – region for the profile, or use sc2.constants



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


# Ladder API - CN


### battlenet_client.sc2.community_cn.ladder(region_tag: str, ladder_id: int, locale: Optional[str] = None)
Returns a ladder summary, or specific ladder for an individual SC2 profile.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **ladder_id** (*int*) – region for the profile, or use sc2.constants



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



* **Raises**

    **BNetRegionError** – when the region tag is not ‘cn’
