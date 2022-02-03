"""This module contains all of the methods for accessing specific character information in World of Warcraft"""
from typing import Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from battlenet_client.wow.client import Client

from battlenet_client.wow.decorators import verify_client


class CharacterAPI:
    def __init__(self, client: "Client") -> None:
        self.client = client

    @verify_client
    def achievement_summary(
        self, locale: str, realm_name: str, character_name: str
    ) -> Dict[str, Any]:
        """Accesses the achievement summary of the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data that contains requested achievement summary
        """
        data: Dict[str, Any] = self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "achievements",
        )
        return data

    @verify_client
    def achievement_statistics(
        self, locale: str, realm_name: str, character_name: str
    ) -> Dict[str, Any]:
        """Accesses the achievement statistics for the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data that contains the requested achievement statistics
        """
        data: Dict[str, Any] = self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "achievements",
            "statistics",
        )
        return data

    @verify_client
    def appearance_summary(
        self, locale: str, realm_name: str, character_name: str
    ) -> Dict[str, Any]:
        """Accesses the appearance summary for the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data that contains requested appearance summary
        """
        data: Dict[str, Any] = self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "appearance",
        )
        return data

    @verify_client
    def collections(
        self,
        locale: str,
        realm_name: str,
        character_name: str,
        category: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Accesses the battle pet and/or mount collections for the requested
        character identified by :character_name: on realm :realm_name: of the
        given :category:.

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character
            category (str): cateogry to retrieve. options are pets or mounts, or None (default).  None will
                provide both

        Returns:
            dict: JSON decoded data that contains requested collection
        """
        if category is not None:
            if category.lower() not in ("pets", "mounts"):
                raise ValueError("Category needs to pets or mounts")

            data: Dict[str, Any] = self.client.profile_data(
                locale,
                "profile",
                "character",
                self.client.slugify(realm_name),
                self.client.slugify(character_name),
                "collections",
                category.lower(),
            )
        else:
            data = self.client.profile_data(
                locale,
                "profile",
                "character",
                self.client.slugify(realm_name),
                self.client.slugify(character_name),
                "collections",
            )

        return data

    @verify_client
    def encounters(
        self,
        locale: str,
        realm_name: str,
        character_name: str,
        category: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Accesses the encounters for the requested character identified by
        :character_name: on realm :realm_name:.  The encounters can be limited
        by :category:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character
            category (str): category to retrieve.  options are 'dungeons',
                'raids', or None (default).  None will access both dungeons and raids

        Returns:
            dict: JSON decoded dict that contains requested encounter data or index
        """

        if category is not None:
            if category.lower() not in ("dungeons", "raids"):
                raise ValueError("Available Categories: None, dungeons and raids")
            data: Dict[str, Any] = self.client.profile_data(
                locale,
                "profile",
                "character",
                self.client.slugify(realm_name),
                self.client.slugify(character_name),
                "encounters",
                self.client.slugify(category),
            )
        else:
            data = self.client.profile_data(
                locale,
                "profile",
                "character",
                self.client.slugify(realm_name),
                self.client.slugify(character_name),
                "encounters",
            )

        return data

    @verify_client
    def equipment_summary(
        self, locale: str, realm_name: str, character_name: str
    ) -> Dict[str, Any]:
        """Accesses the equipped items of the requested character identified by
        :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded dict that contains requested equipment summary
        """
        data: Dict[str, Any] = self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "equipment",
        )
        return data

    @verify_client
    def hunter_pets_summary(
        self, locale: str, realm_name: str, character_name: str
    ) -> Dict[str, Any]:
        """Access the list of hunter pets of the requested character identified
        by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data of the hunter's pets
        """
        data: Dict[str, Any] = self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "hunter-pets",
        )
        return data

    @verify_client
    def media_summary(
        self, locale: str, realm_name: str, character_name: str
    ) -> Dict[str, Any]:
        """Accesses the media assets, such as avatar render, of the requested
        character identified by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data that contains requested media assets
        """
        data: Dict[str, Any] = self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "character-media",
        )
        return data

    @verify_client
    def mythic_keystone(
        self,
        locale: str,
        realm_name: str,
        character_name: str,
        season_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        """Accesses the mythic keystone (M+ or Mythic+) information of the
        requested character identified by :character_name: on realm
        :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character
            season_id (int or None): season id or None (default).  None
                accesses the list of seasons for the current expansion

        Returns:
            dict: JSON decoded data of requested mythic keystone details
        """
        if season_id:
            data: Dict[str, Any] = self.client.profile_data(
                locale,
                "profile",
                "character",
                self.client.slugify(realm_name),
                self.client.slugify(character_name),
                "mythic-keystone-profile",
                "season",
                season_id,
            )
        else:
            data = self.client.profile_data(
                locale,
                "profile",
                "character",
                self.client.slugify(realm_name),
                self.client.slugify(character_name),
                "mythic-keystone-profile",
            )

        return data

    @verify_client
    def professions_summary(
        self, locale: str, realm_name: str, character_name: str
    ) -> Dict[str, Any]:
        """Accesses the profession information of the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data of the character's professions
        """
        data: Dict[str, Any] = self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "professions",
        )
        return data

    @verify_client
    def profile(
        self, locale: str, realm_name: str, character_name: str, status: bool = False
    ) -> Dict[str, Any]:
        """Acceses the profile status of the requested character identified by
        :character_name: on realm :realm_name:

        When requesting the character profile status, a note from Blizzard:

        Returns the status and a unique ID for a character. A client should
        delete information about a character from their application if
        any of the following conditions occur:

            1) an HTTP 404 Not Found error is returned
            2) the is_valid value is false
            3) the returned character ID doesn't match the previously recorded
                value for the character

        The following example illustrates how to use this endpoint:
            1) A client requests and stores information about a character, including
            its unique character ID and the timestamp of the request.
            2) After 30 days, the client makes a request to the status endpoint to
            verify if the character information is still valid.
            3) If character cannot be found, is not valid, or the characters IDs do
            not match, the client removes the information from their application.
            4) If the character is valid and the character IDs match, the client retains
            the data for another 30 days.

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character
            status (bool): flag to request a profile summary (False default) or status (True)

        Returns:
            dict: JSON decoded data of character profile summary
        """

        if status:
            data: Dict[str, Any] = self.client.profile_data(
                locale,
                "profile",
                "character",
                self.client.slugify(realm_name),
                self.client.slugify(character_name),
                "status",
            )
        else:
            data = self.client.profile_data(
                locale,
                "profile",
                "character",
                self.client.slugify(realm_name),
                self.client.slugify(character_name),
            )
        return data

    @verify_client
    def pvp(
        self,
        locale: str,
        realm_name: str,
        character_name: str,
        pvp_bracket: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Accesses the Player versus Player (PvP) information of the requested
        character identified by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character
            pvp_bracket (str or None): '2v2', '3v3', 'rbg', None (default).
                None returns a summary of pvp activity

        Returns:
            dict: JSON decoded data of requested pvp details
        """

        if pvp_bracket is not None:
            data: Dict[str, Any] = self.client.profile_data(
                locale,
                "profile",
                "character",
                self.client.slugify(realm_name),
                self.client.slugify(character_name),
                "pvp-bracket",
                pvp_bracket,
            )
        else:
            data = self.client.profile_data(
                locale,
                "profile",
                "character",
                self.client.slugify(realm_name),
                self.client.slugify(character_name),
                "pvp-summary",
            )
        return data

    @verify_client
    def quests(
        self, locale: str, realm_name: str, character_name: str, completed: bool = False
    ) -> Dict[str, Any]:
        """Accesses the all or just completed quest information of the
        requested character identified by :character_name: on realm
        :realm_name:.

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character
            completed (bool):  To show all quests (False), or to show only
                completed quests (True)
        Returns:
            dict: JSON decoded data of the completed or uncompleted quests
        """

        if completed:
            data: Dict[str, Any] = self.client.profile_data(
                locale,
                "profile",
                "character",
                self.client.slugify(realm_name),
                self.client.slugify(character_name),
                "quests",
                "completed",
            )
        else:
            data = self.client.profile_data(
                locale,
                "profile",
                "character",
                self.client.slugify(realm_name),
                self.client.slugify(character_name),
                "quests",
            )
        return data

    @verify_client
    def reputations_summary(
        self, locale: str, realm_name: str, character_name: str
    ) -> Dict[str, Any]:
        """Accesses the reputation data of the requested character identified
        by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data of the character's reputations
        """
        data: Dict[str, Any] = self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "reputations",
        )
        return data

    @verify_client
    def soulbinds(
        self, locale: str, realm_name: str, character_name: str
    ) -> Dict[str, Any]:
        """Accesses the available soulbinds of the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data of the character's soulbinds
        """
        data: Dict[str, Any] = self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "soulbinds",
        )
        return data

    @verify_client
    def specializations_summary(
        self, locale: str, realm_name: str, character_name: str
    ) -> Dict[str, Any]:
        """Access the avaiable specializations of the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data of the character's specializations
        """
        data: Dict[str, Any] = self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "specializations",
        )
        return data

    @verify_client
    def statistics_summary(
        self, locale: str, realm_name: str, character_name: str
    ) -> Dict[str, Any]:
        """Accesses the statistics of the requested character identified by
        :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data of the character's statistics
        """
        data: Dict[str, Any] = self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "statistics",
        )
        return data

    @verify_client
    def title_summary(
        self, locale: str, realm_name: str, character_name: str
    ) -> Dict[str, Any]:
        """Accesses the list of titles earned by the requested character
        identified by :character_name: on realm :realm_name:

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the slug for the character's realm
            character_name (str): name of character

        Returns:
            dict: JSON decoded data the titles the player has earned
        """
        data: Dict[str, Any] = self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "titles",
        )
        return data
