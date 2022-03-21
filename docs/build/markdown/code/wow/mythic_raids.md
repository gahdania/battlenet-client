# Mythic Raid Leaderboard API


### battlenet_client.wow.game_data.mythic_raid_leaderboard(region_tag: str, raid_name: str, faction: str, \*, release: Optional[str] = 'retail', locale: Optional[str] = None)
Returns the leaderboard for a given raid and faction.


* **Parameters**


    * **region_tag** (*str*) – region_tag abbreviation


    * **raid_name** (*str*) – name of the raid


    * **faction** (*str*) – horde or alliance, defaults to alliance


    * **release** (*str*) – release of the game (ie classic1x, classic, retail)


    * **locale** (*str*) – which locale to use for the request



* **Returns**

    The URL (str) and parameters (dict)



* **Return type**

    tuple
