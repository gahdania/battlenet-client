from typing import Any, TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from client import SC2Client


class LegacyAPI:
    def __init__(self, client: "SC2Client"):
        self.client = client

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
