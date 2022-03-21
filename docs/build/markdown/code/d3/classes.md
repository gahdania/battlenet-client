# Character Class API


### battlenet_client.d3.community.character_class(region_tag: str, class_slug: str, locale: Optional[str] = None)
Returns a single character class by slug.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **class_slug** (*str*) – the slug of a character class



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.d3.community.api_skill(region_tag: str, class_slug: str, skill_slug: str, locale: Optional[str] = None)
Returns a single skill by slug for a specific character class.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **class_slug** (*str*) – the slug of a character class


    * **skill_slug** (*str*) –



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
