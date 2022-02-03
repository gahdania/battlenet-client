from typing import Any, TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from client import SC2Client

from exceptions import SC2RegionError


class LadderAPI:
    def __init__(self, client: "SC2Client") -> None:
        self.client = client

    def grandmaster(self, locale: str, region_id: int) -> Dict[str, Any]:
        return self.client.community(locale, "ladder", "grandmaster", region_id)

    def season(self, locale: str, region_id: int) -> Dict[str, Any]:
        return self.client.community(locale, "ladder", "season", region_id)


class CNLadderAPI:
    def __init__(self, client: "SC2Client") -> None:
        if client.tag != "cn":
            raise SC2RegionError("Invalid region for API")

        self.client = client

    def ladder(self, locale: str, profile_id: str) -> Dict[str, Any]:

        return self.client.community(locale, "ladder", profile_id)
