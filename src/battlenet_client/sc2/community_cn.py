from typing import Any, TYPE_CHECKING, Dict, Optional

if TYPE_CHECKING:
    from client import SC2Client

from exceptions import SC2ClientError, SC2RegionError


class CNProfileAPI:
    def __init__(self, client: "SC2Client") -> None:
        if client.tag != "cn":
            raise SC2RegionError("Invalid region for API")

        self.client = client

    def profile(
        self, locale: str, profile_id: str, region: str, name: str
    ) -> Dict[str, Any]:

        if self.client.tag != 5:
            raise SC2RegionError("This API is not available in this region")

        return self.client.community(locale, "profile", profile_id, region, name)

    def ladders(
        self, locale: str, profile_id: str, region: str, name: str
    ) -> Dict[str, Any]:
        if self.client.tag != 5:
            raise SC2RegionError("This API is not available in this region")

        return self.client.community(
            locale, "profile", profile_id, region, name, "ladders"
        )

    def match_history(
        self, locale: str, profile_id: str, region: str, name: str
    ) -> Dict[str, Any]:
        if self.client.tag != 5:
            raise SC2RegionError("This API is not available in this region")

        return self.client.community(
            locale, "profile", profile_id, region, name, "matches"
        )


class CNLadderAPI:
    def __init__(self, client: "SC2Client") -> None:
        if client.tag != "cn":
            raise SC2RegionError("Invalid region for API")

        self.client = client

    def ladder(self, locale: str, profile_id: str) -> Dict[str, Any]:

        return self.client.community(locale, "ladder", profile_id)


class CNDataResourceAPI:
    def __init__(self, client: "SC2Client") -> None:
        if client.tag != "cn":
            raise SC2RegionError("Invalid region for API")

        self.client = client

    def achievements(self, locale: str) -> Dict[str, Any]:
        """Returns the achievements for Starcraft II

        Args:
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data of the guild's achievement summary
        """
        return self.client.community(locale, "data", "achievements")

    def rewards(self, locale: str) -> Dict[str, Any]:
        """Returns the rewards of the achievements in Starcrft II

        Args:
            locale (str): which locale to use for the request

        Returns:
            dict: json decoded data of the guild's achievement summary
        """
        return self.client.community(locale, "data", "rewards")
