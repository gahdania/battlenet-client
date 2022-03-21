# Professions API


### battlenet_client.wow.game_data.profession(region_tag: str, \*, profession_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
RReturns an index of professions, or a profession by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **profession_id** (*int**, **optional*) – the profession ID or the word ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.profession_media(region_tag: str, profession_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns media for a profession by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **profession_id** (*str*) – profession ID


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.profession_skill_tier(region_tag: str, profession_id: int, skill_tier_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns a skill tier for a profession by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **profession_id** (*int*) – the profession ID


    * **skill_tier_id** (*int*) – the skill tier ID


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.recipe(region_tag: str, recipe_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns a recipe by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **recipe_id** (*str*) – the recipe ID


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.recipe_media(region_tag: str, recipe_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns media for a recipe by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **recipe_id** (*int*) – the profession ID


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
