from typing import Optional, Any, TYPE_CHECKING, Dict, List

if TYPE_CHECKING:
    from client import WoWClient

from .exceptions import WoWReleaseError


class Account:
    def __init__(self, client: "WoWClient") -> None:
        self.client = client

    def account_profile_summary(self, locale: str) -> Dict[str, Any]:
        """Accesses a summary of the account

        Args:
            locale (str): which locale to use for the request

        Returns:
            dict: JSON decoded data that contains the profile summary
        """
        return self.client.protected_data(locale, "profile")

    def protected_character_profile_summary(
        self, locale: str, realm_id: int, character_id: int
    ) -> Dict[str, Any]:
        """Accesses a summary of protected account information for the
        character identified by :realm_id: and :character_id:

        Args:
            locale (str): which locale to use for the request
            realm_id (int): the ID for the character's realm
            character_id (int): the ID of character

        Returns:
            dict: JSON decoded data that contains the protected character
                profile summary
        """
        return self.client.protected_data(
            locale, "profile", "protected-character", realm_id, character_id
        )

    def account_collections(
        self, locale: str, category: Optional[str] = None
    ) -> Dict[str, Any]:
        """Access the collection of battle pets and/or mounts of an account as
        provided by :category:

        Args:
            locale (str): which locale to use for the request
            category (str): 'pets' to retrieve the pet collections, and
                'mounts' to retrieve the mount collection of the account or
                None for both pets and mounts

        Returns:
            dict: JSON decoded data for the index/individual collections
        """
        if category is not None:
            return self.client.protected_data(
                locale, "profile", "collections", self.client.slugify(category)
            )
        return self.client.protected_data(locale, "profile", "collections")


class CharacterAchievements:
    def __init__(self, client: "WoWClient") -> None:
        self.client = client

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
        return self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "achievements",
        )

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
        return self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "achievements",
            "statistics",
        )


class CharacterAppearance:
    def __init__(self, client: "WoWClient") -> None:
        self.client = client

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
        return self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "appearance",
        )


class CharacterCollections:
    def __init__(self, client: "WoWClient") -> None:
        self.client = client

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
        if category:
            if category.lower() not in ("pets", "mounts"):
                raise ValueError("Category needs to pets or mounts")

            return self.client.profile_data(
                locale,
                "profile",
                "character",
                self.client.slugify(realm_name),
                self.client.slugify(character_name),
                "collections",
                category.lower(),
            )
        return self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "collections",
        )


class CharacterEncounters:
    def __init__(self, client: "WoWClient") -> None:
        self.client = client

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

        if category:
            if category.lower() not in ("dungeons", "raids"):
                raise ValueError("Available Categories: None, dungeons and raids")
            return self.client.profile_data(
                locale,
                "profile",
                "character",
                self.client.slugify(realm_name),
                self.client.slugify(character_name),
                "encounters",
                self.client.slugify(category),
            )
        return self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "encounters",
        )


class CharacterEquipment:
    def __init__(self, client: "WoWClient") -> None:
        self.client = client

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
        return self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "equipment",
        )


class CharacterHunterPets:
    def __init__(self, client: "WoWClient") -> None:
        self.client = client

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
        return self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "hunter-pets",
        )


class CharacterMedia:
    def __init__(self, client: "WoWClient") -> None:
        self.client = client

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
        return self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "character-media",
        )


class CharacterMythicKeystone:
    def __init__(self, client: "WoWClient") -> None:
        self.client = client

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
            return self.client.profile_data(
                locale,
                "profile",
                "character",
                self.client.slugify(realm_name),
                self.client.slugify(character_name),
                "mythic-keystone-profile",
                "season",
                season_id,
            )
        return self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "mythic-keystone-profile",
        )


class CharacterProfessions:
    def __init__(self, client: "WoWClient") -> None:
        self.client = client

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
        return self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "professions",
        )


class CharacterProfile:
    def __init__(self, client: "WoWClient") -> None:
        self.client = client

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
            return self.client.profile_data(
                locale,
                "profile",
                "character",
                self.client.slugify(realm_name),
                self.client.slugify(character_name),
                "status",
            )
        return self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
        )


class CharacterPVP:
    def __init__(self, client: "WoWClient") -> None:
        self.client = client

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

        if pvp_bracket:
            return self.client.profile_data(
                locale,
                "profile",
                "character",
                self.client.slugify(realm_name),
                self.client.slugify(character_name),
                "pvp-bracket",
                pvp_bracket,
            )
        return self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "pvp-summary",
        )


class CharacterQuests:
    def __init__(self, client: "WoWClient") -> None:
        self.client = client

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
            return self.client.profile_data(
                locale,
                "profile",
                "character",
                self.client.slugify(realm_name),
                self.client.slugify(character_name),
                "quests",
                "completed",
            )
        return self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "quests",
        )


class CharacterReputations:
    def __init__(self, client: "WoWClient") -> None:
        self.client = client

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
        return self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "reputations",
        )


class CharacterSoulbinds:
    def __init__(self, client: "WoWClient") -> None:
        self.client = client

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
        return self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "soulbinds",
        )


class CharacterSpecializations:
    def __init__(self, client: "WoWClient") -> None:
        self.client = client

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
        return self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "specializations",
        )


class CharacterStatistics:
    def __init__(self, client: "WoWClient") -> None:
        self.client = client

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
        return self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "statistics",
        )


class CharacterTitles:
    def __init__(self, client: "WoWClient") -> None:
        self.client = client

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
        return self.client.profile_data(
            locale,
            "profile",
            "character",
            self.client.slugify(realm_name),
            self.client.slugify(character_name),
            "titles",
        )


class Guild:
    def __init__(self, client: "WoWClient") -> None:
        self.client = client

    def guild(self, locale: str, realm_name: str, guild_name: str) -> Dict[str, Any]:
        """Returns a single guild by its name and realm.

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the name of the guild's realm
            guild_name (str): the name of the guild

        Returns:
            dict: json decoded data of the guild
        """
        if self.client.release != "retail":
            raise WoWReleaseError(
                f"{self.client.release} does not support the Guild Data API"
            )

        return self.client.game_data(
            locale,
            "profile",
            "guild",
            self.client.slugify(realm_name),
            self.client.slugify(guild_name),
        )

    def guild_activities(
        self, locale: str, realm_name: str, guild_name: str
    ) -> Dict[str, Any]:
        """Returns a single guild's activity by name and realm.

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the name of the guild's realm
            guild_name (str): the name of the guild

        Returns:
            dict: json decoded data of the guild activities
        """
        if self.client.release != "retail":
            raise WoWReleaseError(
                f"{self.client.release} does not support the Guild Data API"
            )

        return self.client.game_data(
            locale,
            "profile",
            "guild",
            self.client.slugify(realm_name),
            self.client.slugify(guild_name),
            "activity",
        )

    def guild_achievements(
        self, locale: str, realm_name: str, guild_name: str
    ) -> Dict[str, Any]:
        """Returns a single guild's achievements by name and realm.

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the name of the guild's realm
            guild_name (str): the name of the guild

        Returns:
            dict: json decoded data of the guild achievements
        """
        if self.client.release != "retail":
            raise WoWReleaseError(
                f"{self.client.release} does not support the Guild Data API"
            )

        return self.client.game_data(
            locale,
            "profile",
            "guild",
            self.client.slugify(realm_name),
            self.client.slugify(guild_name),
            "achievements",
        )

    def guild_roster(
        self, locale: str, realm_name: str, guild_name: str
    ) -> Dict[str, Any]:
        """Returns a single guild's roster by its name and realm.

        Args:
            locale (str): which locale to use for the request
            realm_name (str): the name of the guild's realm
            guild_name (str): the name of the guild

        Returns:
            dict: json decoded data of the guild's achievement summary
        """
        if self.client.release != "retail":
            raise WoWReleaseError(
                f"{self.client.release} does not support the Guild Data API"
            )

        return self.client.game_data(
            locale,
            "profile",
            "guild",
            self.client.slugify(realm_name),
            self.client.slugify(guild_name),
            "roster",
        )

    def guild_crest_components_index(self, locale: str) -> Dict[str, Any]:
        """Returns an index of guild crest components.

        Args:
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data for the index of guild crest components
        """
        return self.client.game_data(locale, "static", "guild-crest", "index")

    def guild_crest_border_media(self, locale: str, border_id: int) -> Dict[str, Any]:
        """Returns media for a specific guild crest border.

        Args:
            locale (str): which locale to use for the request
            border_id (int): the border ID

        Returns:
            dict: json decoded media data for the guild border
        """
        return self.client.media_data(
            locale, "static", "guild-crest", "border", border_id
        )

    def guild_crest_emblem_media(self, locale: str, crest_id: int) -> Dict[str, Any]:
        """Returns media for a specific guild crest emblem.

        Args:
            locale (str): which locale to use for the request
            crest_id (int): the border ID

        Returns:
            dict: json decoded media data for the guild crest
        """
        return self.client.media_data(
            locale, "static", "guild-crest", "emblem", crest_id
        )