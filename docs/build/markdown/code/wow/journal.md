# Adventure Journal API


### battlenet_client.wow.game_data.journal_expansion(region_tag: str, \*, expansion_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of journal expansions, or a journal expansion by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **expansion_id** (*int**, **optional*) – the encounter ID or ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.journal_encounter(region_tag: str, \*, encounter_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of journal encounters, or a journal encounter by ID.

### Notes

This replaced the Boss endpoint of the community REST API


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **encounter_id** (*int**, **optional*) – the encounter ID or ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.journal_encounter_search(region_tag: str, field_values: Dict[str, Any], \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Performs a search of journal encounters.  For more detail see the Search Guide.
[https://develop.battle.net/documentation/world-of-warcraft/guides/search](https://develop.battle.net/documentation/world-of-warcraft/guides/search)


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **field_values** (*dict*) – search criteria, as key/value pairs


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.journal_instance(region_tag: str, \*, instance_id: Optional[Union[int, str]] = 'index', release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of journal instances, or a journal instance.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **instance_id** (*int**, **optional*) – the encounter ID or ‘index’


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.game_data.journal_instance_media(region_tag: str, instance_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns media for a journal instance by ID.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **instance_id** (*int*) – the creature family ID


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
