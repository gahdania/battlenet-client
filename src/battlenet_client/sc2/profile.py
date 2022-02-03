from typing import Any, TYPE_CHECKING, Dict, Union

if TYPE_CHECKING:
    from client import SC2Client

from battlenet_client.sc2.exceptions import SC2RegionError


class ProfileAPI:
    def __init__(self, client: "SC2Client") -> None:
        self.client = client

    def static(self, locale: str, region_id: int) -> Dict[str, Any]:

        return self.client.community(locale, "static", "profile", region_id)

    def metadata(self, locale: str, region_id: str, realm_id: str, profile_id: str):

        return self.client.community(
            locale, "metadata", "profile", region_id, realm_id, profile_id
        )

    def profile(self, locale, region_id, realm_id, profile_id):
        """

        Args:
            locale:
            region_id:
            realm_id:
            profile_id:

        Returns:

        """
        return self.client.community(locale, "profile", region_id, realm_id, profile_id)

    def ladder(self, locale, region_id, realm_id, profile_id, ladder_id=None):
        if ladder_id is not None:
            return self.client.community(
                locale, "profile", region_id, realm_id, profile_id, "ladder", ladder_id
            )

        return self.client.community(
            locale, "profile", region_id, realm_id, profile_id, "ladder", "summary"
        )


class CNProfileAPI:
    def __init__(self, client):
        if client.tag != "cn":
            raise SC2RegionError("Invalid region for API")

        self.client = client

    def profile(self, locale, profile_id, region, name):

        if self.client.tag != 5:
            raise SC2RegionError("This API is available in this region")

        return self.client.community(locale, "profile", profile_id, region, name)

    def ladders(self, locale, profile_id, region, name):
        if self.client.tag != 5:
            raise SC2RegionError("This API is available in this region")

        return self.client.community(
            locale, "profile", profile_id, region, name, "ladders"
        )

    def match_history(self, locale, profile_id, region, name):
        if self.client.tag != 5:
            raise SC2RegionError("This API is available in this region")

        return self.client.community(
            locale, "profile", profile_id, region, name, "matches"
        )
