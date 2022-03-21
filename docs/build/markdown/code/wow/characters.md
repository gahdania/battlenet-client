# Character Profile API


### battlenet_client.wow.profile.achievement_summary(region_tag: str, realm_name: str, character_name: str, \*, statistics: Optional[bool] = False, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns a summary of the achievements a character has completed.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **realm_name** (*str*) – the slug for the character’s realm


    * **character_name** (*str*) – name of character


    * **statistics** (*bool*) – Boolean to determine to display the statistics or not


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.profile.appearance_summary(region_tag: str, realm_name: str, character_name: str, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns a summary of a character’s appearance settings.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **realm_name** (*str*) – the slug for the character’s realm


    * **character_name** (*str*) – name of character


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.profile.collections(region_tag: str, realm_name: str, character_name: str, \*, category: Optional[str] = None, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of collection types for a character, a summary of the mounts
a character has obtained, or a summary of the battle pets a character has obtained.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **realm_name** (*str*) – the slug for the character’s realm


    * **character_name** (*str*) – name of character


    * **category** (*str*) – category to retrieve. options are pets or mounts, or None (default).  None will
    provide both


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.profile.encounters(region_tag: str, realm_name: str, character_name: str, \*, category: Optional[str] = None, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns a summary of all of a character’s encounters, just dungeon encounters,
or just raid encounters


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **realm_name** (*str*) – the slug for the character’s realm


    * **character_name** (*str*) – name of character


    * **category** (*str*) – category to retrieve.  options are ‘dungeons’,
    ‘raids’, or None (default).  None will access both dungeons and raids


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.profile.equipment_summary(region_tag: str, realm_name: str, character_name: str, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns a summary of the items equipped by a character.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **realm_name** (*str*) – the slug for the character’s realm


    * **character_name** (*str*) – name of character


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.profile.hunter_pets_summary(region_tag: str, realm_name: str, character_name: str, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
If the character is a hunter, returns a summary of the character’s hunter pets.
Otherwise, returns an HTTP 404 Not Found error.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **realm_name** (*str*) – the slug for the character’s realm


    * **character_name** (*str*) – name of character


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.profile.media_summary(region_tag: str, realm_name: str, character_name: str, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns a summary of the media assets available for a character (such as an avatar render).


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **realm_name** (*str*) – the slug for the character’s realm


    * **character_name** (*str*) – name of character


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.profile.mythic_keystone(region_tag: str, realm_name: str, character_name: str, \*, season_id: Optional[int] = None, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns the Mythic Keystone profile index for a character,
or the Mythic Keystone season details for a character.

Returns a 404 Not Found for characters that have not yet completed
a Mythic Keystone dungeon for the specified season.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **realm_name** (*str*) – the slug for the character’s realm


    * **character_name** (*str*) – name of character


    * **season_id** (*int** or **None*) – season id or None (default).  None
    accesses the list of seasons for the current expansion


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.profile.professions_summary(region_tag: str, realm_name: str, character_name: str, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns a summary of professions for a character.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **realm_name** (*str*) – the slug for the character’s realm


    * **character_name** (*str*) – name of character


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.profile.profile(region_tag: str, realm_name: str, character_name: str, \*, status: bool = False, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns a profile summary for a character, or the status and a unique ID for a character.

A should delete information about a character from their application if
any of the following conditions occur:

>
> 1. an HTTP 404 Not Found error is returned


> 2. the is_valid value is false


> 3. the returned character ID doesn’t match the previously recorded

>     value for the character

The following example illustrates how to use this endpoint:

    1) A requests and stores information about a character, including
    its unique character ID and the timestamp of the request.
    2) After 30 days, the makes a request to the status endpoint to
    verify if the character information is still valid.
    3) If character cannot be found, is not valid, or the characters IDs do
    not match, the removes the information from their application.
    4) If the character is valid and the character IDs match, the retains
    the data for another 30 days.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **realm_name** (*str*) – the slug for the character’s realm


    * **character_name** (*str*) – name of character


    * **status** (*bool*) – flag to request a profile summary (False default) or status (True)


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.profile.pvp(region_tag: str, realm_name: str, character_name: str, \*, pvp_bracket: Optional[str] = None, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns the PvP bracket statistics for a character, or a PvP summary for a character.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **realm_name** (*str*) – the slug for the character’s realm


    * **character_name** (*str*) – name of character


    * **pvp_bracket** (*str** or **None*) – ‘2v2’, ‘3v3’, ‘rbg’, None (default).
    None returns a summary of pvp activity


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.profile.quests(region_tag: str, realm_name: str, character_name: str, \*, completed: Optional[bool] = False, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns a character’s active quests as well as a link to the character’s completed quests, or
a list of quests that a character has completed.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **realm_name** (*str*) – the slug for the character’s realm


    * **character_name** (*str*) – name of character


    * **completed** (*bool*) – To show all quests (False), or to show only
    completed quests (True)


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.profile.reputations_summary(region_tag: str, realm_name: str, character_name: str, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns a summary of a character’s reputations.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **realm_name** (*str*) – the slug for the character’s realm


    * **character_name** (*str*) – name of character


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.profile.soulbinds(region_tag: str, realm_name: str, character_name: str, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns a character’s soulbinds.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **realm_name** (*str*) – the slug for the character’s realm


    * **character_name** (*str*) – name of character


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.profile.specializations_summary(region_tag: str, realm_name: str, character_name: str, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns a summary of a character’s specializations.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **realm_name** (*str*) – the slug for the character’s realm


    * **character_name** (*str*) – name of character


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.profile.statistics_summary(region_tag: str, realm_name: str, character_name: str, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns a statistics summary for a character.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **realm_name** (*str*) – the slug for the character’s realm


    * **character_name** (*str*) – name of character


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.profile.title_summary(region_tag: str, realm_name: str, character_name: str, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns a summary of titles a character has obtained.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **realm_name** (*str*) – the slug for the character’s realm


    * **character_name** (*str*) – name of character


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
