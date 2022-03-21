# Account Profile API


### battlenet_client.wow.profile.account_profile_summary(region_tag: str, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns a profile summary for an account.

Because this endpoint provides data about the current logged-in user’s World of Warcraft account,
it requires an access token with the ‘wow.profile’ scope acquired via the Authorization Code Flow.
[https://develop.battle.net/documentation/guides/using-oauth/authorization-code-flow](https://develop.battle.net/documentation/guides/using-oauth/authorization-code-flow)


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple



### battlenet_client.wow.profile.protected_character_profile_summary(region_tag: str, realm_id: int, character_id: int, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns a protected profile summary for a character.

Because this endpoint provides data about the current logged-in user’s World of Warcraft account,
it requires an access token with the ‘wow.profile’ scope acquired via the Authorization Code Flow.
[https://develop.battle.net/documentation/guides/using-oauth/authorization-code-flow](https://develop.battle.net/documentation/guides/using-oauth/authorization-code-flow)


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **realm_id** (*int*) – the ID for the character’s realm


    * **character_id** (*int*) – the ID of character


    * **release** (*str*) – release of the game (ie classi\`c1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)

        profile summary




* **Return type**

    tuple



### battlenet_client.wow.profile.account_collections(region_tag: str, \*, category: Optional[str] = None, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns an index of collection types for an account.

Because this endpoint provides data about the current logged-in user’s World of Warcraft account,
it requires an access token with the ‘wow.profile’ scope acquired via the Authorization Code Flow.
[https://develop.battle.net/documentation/guides/using-oauth/authorization-code-flow](https://develop.battle.net/documentation/guides/using-oauth/authorization-code-flow)


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **category** (*str*) – ‘pets’ to retrieve the pet collections, and
    ‘mounts’ to retrieve the mount collection of the account or
    None for both pets and mounts


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
