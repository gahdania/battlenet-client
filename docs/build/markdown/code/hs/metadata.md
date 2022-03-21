# Metadata API


### battlenet_client.hs.game_data.metadata(region_tag: str, \*, meta_data: Optional[str] = None, locale: Optional[str] = None)
Returns information about the categorization of cards. Metadata
includes the card set, set group (for example, Standard or Year of
the Dragon), rarity, class, card type, minion type, and keywords, or
information about just one type of metadata.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **locale** (*str*) – which locale to use for the request


    * **meta_data** (*str**, **optional*) – what metadata to filter
    Please see below for more information
    [https://develop.battle.net/documentation/hearthstone/guides/metadata](https://develop.battle.net/documentation/hearthstone/guides/metadata)
    valid options: sets, setGroups, types, rarities, classes,
    minionTypes, keywords



* **Returns**

    json decoded list of metadata or a specific set of metadata



* **Return type**

    dict
