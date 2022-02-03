from typing import Any, TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from client import SC2Client


class LeagueData:
    def __init__(self, client: "SC2Client") -> None:
        self.client = client

    def league_data(
        self, locale: str, season_id: str, queue_id: str, team_type: str, league_id: str
    ) -> Dict[str, Any]:
        return self.client.game_data(
            locale, "league", season_id, queue_id, team_type, league_id
        )
