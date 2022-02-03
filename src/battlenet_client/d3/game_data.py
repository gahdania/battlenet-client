from typing import Optional, Any, TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from client import D3Client


class GameDataAPI:
    def __init__(self, client: "D3Client") -> None:
        self.client = client

    def season(self, locale: str, season_id: Optional[int] = None) -> Dict[str, Any]:
        if season_id:
            return self.client.game_data(locale, "season", season_id)

        return self.client.game_data(locale, "season/")

    def season_leaderboard(
        self, locale: str, season_id: int, leaderboard_id: str
    ) -> Dict[str, Any]:
        return self.client.game_data(
            locale, "season", season_id, "leaderboard", leaderboard_id
        )

    def era(self, locale: str, era_id: Optional[int] = None) -> Dict[str, Any]:

        if era_id:
            return self.client.game_data(locale, "era", era_id)

        return self.client.game_data(locale, "era/")

    def era_leaderboard(
        self, locale: str, era_id: str, leaderboard_id: str
    ) -> Dict[str, Any]:
        return self.client.game_data(
            locale, "era", era_id, "leaderboard", leaderboard_id
        )
