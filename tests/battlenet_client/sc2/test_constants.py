import pytest

from battlenet_client.sc2.constants import Region, QueueID, TeamType, LeagueID
from battlenet_client.constants import Region as BaseRegion


def test_region_class():
    assert issubclass(Region, BaseRegion)


@pytest.mark.parametrize('queue, expected_value', (
        ('WoL_1v1', 1),
        ('WoL_2v2', 2),
        ('WoL_3v3', 3),
        ('WoL_4v4', 4),
        ('HotS_1v1', 101),
        ('HotS_2v2', 102),
        ('HotS_3v3', 103),
        ('HotS_4v4', 104),
        ('LotV_1v1', 201),
        ('LotV_2v2', 202),
        ('LotV_3v3', 203),
        ('LotV_4v4', 204),
        ('LotV_Archon', 206)
))
def test_queue_id(queue, expected_value):
    assert getattr(QueueID, queue) == expected_value


@pytest.mark.parametrize('team_type, expected_value', (
        ('ARRANGED', 0),
        ('RANDOM', 1)
))
def test_team_type(team_type, expected_value):
    assert getattr(TeamType, team_type) == expected_value


@pytest.mark.parametrize('league, expected_value', (
        ('BRONZE', 0),
        ('SILVER', 1),
        ('GOLD', 2),
        ('PLATINUM', 3),
        ('DIAMOND', 4),
        ('MASTER', 5),
        ('GRANDMASTER', 6)
))
def test_league(league, expected_value):
    assert getattr(LeagueID, league) == expected_value
