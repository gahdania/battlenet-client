from itertools import product

import pytest

from battlenet_client.decorators import VALID_REGIONS
from battlenet_client.exceptions import BNetRegionNotFoundError
from battlenet_client.sc2.game_data import league_data
from ..constants import INVALID_REGIONS


@pytest.mark.parametrize('region_tag, season_id, queue_id, team_type, league_id',
                         list(product(VALID_REGIONS, ('37', '44', '57', '63'),
                                      ('1', '2', '3', '4', '101', '102', '103', '104',
                                       '201', '202', '203', '204', '206'),
                                      ('0', '1'),
                                      ('0', '1', '2', '3', '4', '5', '6'))))
def test_league_data_id_valid_region_id(region_tag, season_id, queue_id, team_type, league_id):
    data = league_data(region_tag, season_id, queue_id, team_type, league_id, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/league/{season_id}/{queue_id}/{team_type}/{league_id}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, season_id, queue_id, team_type, league_id',
                         list(product(INVALID_REGIONS, ('37', '44', '57', '63'),
                                      ('1', '2', '3', '4', '101', '102', '103', '104',
                                       '201', '202', '203', '204', '206'),
                                      ('0', '1'),
                                      ('0', '1', '2', '3', '4', '5', '6'))))
def test_league_data_invalid_region_tag(region_tag, season_id, queue_id, team_type, league_id):
    with pytest.raises(BNetRegionNotFoundError):
        league_data(region_tag, season_id, queue_id, team_type, league_id, locale='enus')
