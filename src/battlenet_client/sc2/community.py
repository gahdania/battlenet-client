from typing import Any, TYPE_CHECKING, Dict, Optional

if TYPE_CHECKING:
    from client import SC2Client

from exceptions import SC2ClientError


class Profile:
    def __init__(self, client: "SC2Client") -> None:
        self.client = client

    __class_name = "profile"

    def static(self, locale: str, region_id: int) -> Dict[str, Any]:

        return self.client.community(locale, "static", "profile", region_id)

    def metadata(
        self, locale: str, region_id: int, realm_id: int, profile_id: int
    ) -> Dict[str, Any]:

        return self.client.community(
            locale, "metadata", "profile", region_id, realm_id, profile_id
        )

    def profile(
        self, locale: str, region_id: int, realm_id: int, profile_id: int
    ) -> Dict[str, Any]:
        """

        Args:
            locale:
            region_id:
            realm_id:
            profile_id:

        Returns:

        """
        return self.client.community(locale, "profile", region_id, realm_id, profile_id)

    def ladder(
        self,
        locale: str,
        region_id: int,
        realm_id: int,
        profile_id: int,
        ladder_id: Optional[int] = None,
    ) -> Dict[str, Any]:
        if ladder_id:
            return self.client.community(
                locale, "profile", region_id, realm_id, profile_id, "ladder", "summary"
            )

        return self.client.community(
            locale, "profile", region_id, realm_id, profile_id, "ladder", ladder_id
        )


class Ladder:
    def __init__(self, client: "SC2Client") -> None:
        self.client = client

    __class_name = "ladder"

    def grandmaster(self, locale: str, region_id: int) -> Dict[str, Any]:
        return self.client.community(locale, "ladder", "grandmaster", region_id)

    def season(self, locale: str, region_id: int) -> Dict[str, Any]:
        return self.client.community(locale, "ladder", "season", region_id)


class Account:
    def __init__(self, client: "SC2Client") -> None:
        self.client = client

    __class_name = "account"

    def player(self, locale: str, account_id: str) -> Dict[str, Any]:
        """Returns the player data for the provided `account_id`.

        Args:
            locale (str): which locale to use for the request
            account_id (int): the account ID to request

        Returns:
            dict: json decoded data of the guild's achievement summary
        """
        if not self.client.auth_flow:
            raise SC2ClientError("Requires the authorized workflow")

        return self.client.community(locale, "player", account_id)


class Legacy:
    def __init__(self, client: "SC2Client") -> None:
        self.client = client

    __class_name = "legacy"

    def profile(
        self, locale: str, region_id: int, realm_id: int, profile_id: int
    ) -> Dict[str, Any]:

        return self.client.community(
            locale, "legacy", "profile", region_id, realm_id, profile_id
        )

    def ladders(
        self, locale: str, region_id: int, realm_id: int, profile_id: int
    ) -> Dict[str, Any]:

        return self.client.community(
            locale, "legacy", "profile", region_id, realm_id, profile_id, "ladders"
        )

    def match_history(
        self, locale: str, region_id: int, realm_id: int, profile_id: int
    ) -> Dict[str, Any]:

        return self.client.community(
            locale, "legacy", "profile", region_id, realm_id, profile_id, "matches"
        )

    def ladder(self, locale: str, region_id: int, ladder_id: int) -> Dict[str, Any]:

        return self.client.community(locale, "legacy", "ladder", region_id, ladder_id)

    def achievements(self, locale: str, region_id: int) -> Dict[str, Any]:
        return self.client.community(
            locale, "legacy", "data", "achievements", region_id
        )

    def rewards(self, locale: str, region_id: int) -> Dict[str, Any]:
        return self.client.community(locale, "legacy", "data", "rewards", region_id)
