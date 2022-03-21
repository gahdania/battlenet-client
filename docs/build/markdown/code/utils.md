# Global Utility Functions


### battlenet_client.utils.currency_convertor(value: int)
Returns the value into gold, silver and copper


* **Parameters**

    **value** (*int*) – the value to be converted



* **Returns**

    gold (int), silver (int) and copper (int)



* **Return type**

    tuple



### battlenet_client.utils.slugify(value: Union[str, int])
Returns value as a slug


* **Parameters**

    **value** (*str*) – the string to be converted into a slug



* **Returns**

    the slug



* **Return type**

    str



### battlenet_client.utils.localize(locale: Optional[str] = None)
Returns the standardized locale


* **Parameters**

    **locale** (*str*) – the locality to be standardized



* **Returns**

    the locale in the format of “<language>_<COUNTRY>”



* **Return type**

    str



* **Raises**


    * **TypeError** – when locale is not a string


    * **ValueError** – when the lang and country are not in the given lists



### battlenet_client.utils.api_host(region_tag: str)
Returns the API endpoint hostname and protocol


* **Parameters**

    **region_tag** (*str*) – the region abbreviation



* **Returns**

    The API endpoint hostname and protocol



* **Return type**

    str



### battlenet_client.utils.auth_host(region_tag: str)
Returns the authorization endpoint hostname and protocol


* **Parameters**

    **region_tag** (*str*) – the region abbreviation



* **Returns**

    The authorization endpoint hostname and protocol



* **Return type**

    str



### battlenet_client.utils.render_host(region_tag: str)
Returns the render endpoint hostname and protocol


* **Parameters**

    **region_tag** (*str*) – the region abbreviation



* **Returns**

    The render endpoint hostname and protocol



* **Return type**

    str
