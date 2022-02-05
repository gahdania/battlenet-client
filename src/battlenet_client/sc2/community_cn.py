from typing import Any, TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from client import SC2Client

from exceptions import SC2RegionError


class CNProfile:
    def __init__(self, client: "SC2Client") -> None:
        if client.tag != "cn":
            raise SC2RegionError("Invalid region for API")

        self.client = client

    class_name = "profile"

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


class CNLadder:
    def __init__(self, client: "SC2Client") -> None:
        if client.tag != "cn":
            raise SC2RegionError("Invalid region for API")

        self.client = client

    class_name = "ladder"

    def ladder(self, locale: str, profile_id: str) -> Dict[str, Any]:

        return self.client.community(locale, "ladder", profile_id)


class CNDataResource:
    def __init__(self, client: "SC2Client") -> None:
        if client.tag != "cn":
            raise SC2RegionError("Invalid region for API")

        self.client = client

    class_name = "data_resource"

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
