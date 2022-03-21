import pytest
from itertools import product

from battlenet_client.exceptions import BNetRegionError
from battlenet_client.constants import VALID_REGIONS
from battlenet_client.d3.game_data import season, season_leaderboard, era, era_leaderboard
from ..constants import INVALID_REGIONS


@pytest.mark.parametrize('region_tag', VALID_REGIONS)
def test_season_index(region_tag):
    data = season(region_tag, locale="enus")
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'/d3/season/')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag', INVALID_REGIONS)
def test_season_index_invalid_region(region_tag):
    with pytest.raises(BNetRegionError):
        season(region_tag, locale="enus")


@pytest.mark.parametrize('region_tag, season_id',
                         list(product(VALID_REGIONS, (1, '1'))))
def test_season(region_tag, season_id):
    data = season(region_tag, season_id=season_id, locale="enus")
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'/d3/season/{season_id}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, season_id',
                         list(product(INVALID_REGIONS, (1, '1'))))
def test_season_invalid_region(region_tag, season_id):
    with pytest.raises(BNetRegionError):
        season(region_tag, season_id=season_id, locale="enus")


@pytest.mark.parametrize('region_tag, season_id, leaderboard',
                         list(product(VALID_REGIONS,
                                      (1, '1'),
                                      ('achievement-points', 'rift-barbarian', 'rift-demon-hunter'))))
def test_season_leaderboard(region_tag, season_id, leaderboard):
    data = season_leaderboard(region_tag, season_id=season_id, leaderboard_id=leaderboard, locale="enus")
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'd3/season/{season_id}/leaderboard/{leaderboard}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, season_id, leaderboard',
                         list(product(INVALID_REGIONS,
                                      (1, '1'),
                                      ('achievement-points', 'rift-barbarian', 'rift-demon-hunter'))))
def test_season_leaderboard_invalid_region(region_tag, season_id, leaderboard):
    with pytest.raises(BNetRegionError):
        season_leaderboard(region_tag, season_id=season_id, leaderboard_id=leaderboard, locale="enus")


@pytest.mark.parametrize('region_tag', VALID_REGIONS)
def test_era_index(region_tag):
    data = era(region_tag, locale="enus")
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'd3/era/')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag', INVALID_REGIONS)
def test_era_index_invalid_region(region_tag):
    with pytest.raises(BNetRegionError):
        era(region_tag, locale="enus")


@pytest.mark.parametrize('region_tag, era_id',
                         list(product(VALID_REGIONS, (1, '1'))))
def test_era(region_tag, era_id):
    data = era(region_tag, era_id=era_id, locale="enus")
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'd3/era/{era_id}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, era_id',
                         list(product(INVALID_REGIONS, (1, '1'))))
def test_era_invalid_region(region_tag, era_id):
    with pytest.raises(BNetRegionError):
        era(region_tag, era_id=era_id, locale="enus")


@pytest.mark.parametrize('region_tag, season_id, leaderboard',
                         list(product(VALID_REGIONS,
                                      (1, '1'),
                                      ('achievement-points', 'rift-barbarian', 'rift-demon-hunter'))))
def test_era_leaderboard(region_tag, season_id, leaderboard):
    data = era_leaderboard(region_tag, season_id, leaderboard, locale="enus")
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'd3/era/{season_id}/leaderboard/{leaderboard}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, season_id, leaderboard',
                         list(product(INVALID_REGIONS,
                                      (1, '1'),
                                      ('achievement-points', 'rift-barbarian', 'rift-demon-hunter'))))
def test_era_leaderboard_invalid_region(region_tag, season_id, leaderboard):
    with pytest.raises(BNetRegionError):
        era_leaderboard(region_tag, season_id, leaderboard, locale="enus")
