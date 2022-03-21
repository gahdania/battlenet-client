# OAuth v2


### battlenet_client.bnet.oauth.user_info(region_tag: str, locale: Optional[str] = None)
Returns the user info


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.bnet.oauth.token_validation(region_tag: str, token: str, locale: Optional[str] = None)
Returns if the token is still valid or not


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **token** (*str*) – token string to validate


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
