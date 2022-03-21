# Guild API


### battlenet_client.wow.profile.guild(region_tag: str, realm_name: str, guild_name: str, \*, category: Optional[str] = None, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns a single guild by its name and realm, achievements, activity, or roster


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **realm_name** (*str*) – the name of the guild’s realm


    * **guild_name** (*str*) – the name of the guild


    * **category** (*str*) – category of guild data to retrieve


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
