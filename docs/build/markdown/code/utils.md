# Global Utility Functions

Miscellaneous functions to support world of warcraft

Functions:

    currency_convertor


### battlenet_client.utils.currency_convertor(value: int)
Returns the value into gold, silver and copper


* **Parameters**

    **value** (*int/str*) – the value to be converted



* **Returns**

    gold, silver and copper values



* **Return type**

    tuple



### battlenet_client.utils.localize(locale: Optional[str] = None)
Returns the standardized locale


* **Parameters**

    **locale** (*str*) – the locality to be standardized



* **Returns**

    the locale in the format of “<lang>_<COUNTRY>”



* **Return type**

    str



* **Raises**


    * **TypeError** – when locale is not a string


    * **ValueError** – when the lang and country are not in the given lists



### battlenet_client.utils.slugify(value: str)
Returns the ‘slugified’ string


* **Parameters**

    **value** (*str*) – the string to be converted into a slug



* **Returns**

    the slug of :value:



* **Return type**

    str
