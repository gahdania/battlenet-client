# Artisan API


### battlenet_client.d3.community.artisan(region_tag: str, artisan_slug: str, locale: Optional[str] = None)
Returns a single artisan by the slug


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **artisan_slug** (*str*) – the slug of the artisan



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.d3.community.recipe(region_tag: str, artisan_slug: str, recipe_slug: str, locale: Optional[str] = None)
Returns a single recipe by slug for the specified artisan.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **artisan_slug** (*str*) – the slug of the artisan


    * **recipe_slug** (*str*) – the slug of the recipe



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
