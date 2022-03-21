from itertools import product
import pytest


from battlenet_client.constants import VALID_REGIONS
from battlenet_client.sc2.community_cn import profile, ladders, match_history, ladder
from battlenet_client.sc2.community_cn import achievements, rewards
from battlenet_client.exceptions import BNetRegionError
from ..constants import INVALID_REGIONS

INVALID_REGIONS = list(INVALID_REGIONS)
INVALID_REGIONS += list(VALID_REGIONS)
INVALID_REGIONS.remove('cn')
VALID_REGIONS = ('cn',)


@pytest.mark.parametrize('region_tag, profile_id, region_id, profile_name',
                         list(product(VALID_REGIONS, (984393, 208709586, 827894), (1, 2, 3),
                                      ('rando12345678', 'boredom7902897045', 'tired108400789'))))
def test_profile_valid_region_id(region_tag, profile_id, region_id, profile_name):
    data = profile(region_tag, profile_id, region_id, profile_name, locale='zhcn')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/profile/{profile_id}/{region_id}/{profile_name}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'zh_CN'


@pytest.mark.parametrize('region_tag, profile_id, region_id, profile_name',
                         list(product(INVALID_REGIONS, (984393, 208709586, 827894), (1, 2, 3),
                                      ('rando12345678', 'boredom7902897045', 'tired108400789'))))
def test_profile_invalid_region_tag(region_tag, profile_id, region_id, profile_name):
    with pytest.raises(BNetRegionError):
        profile(region_tag, profile_id, region_id, profile_name, locale='zhcn')


@pytest.mark.parametrize('region_tag, profile_id, region_id, profile_name',
                         list(product(VALID_REGIONS, (984393, 208709586, 827894), (1, 2, 3),
                                      ('rando12345678', 'boredom7902897045', 'tired108400789'))))
def test_ladders(region_tag, profile_id, region_id, profile_name):
    data = ladders(region_tag, profile_id, region_id, profile_name, locale='zhcn')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/profile/{profile_id}/{region_id}/{profile_name}/ladders')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'zh_CN'


@pytest.mark.parametrize('region_tag, profile_id, region_id, profile_name',
                         list(product(INVALID_REGIONS, (984393, 208709586, 827894), (1, 2, 3),
                                      ('rando12345678', 'boredom7902897045', 'tired108400789'))))
def test_ladders_invalid_region_tag(region_tag, profile_id, region_id, profile_name):
    with pytest.raises(BNetRegionError):
        ladders(region_tag, profile_id, region_id, profile_name, locale='zhcn')


@pytest.mark.parametrize('region_tag, profile_id, region_id, profile_name',
                         list(product(VALID_REGIONS, (984393, 208709586, 827894), (1, 2, 3),
                                      ('rando12345678', 'boredom7902897045', 'tired108400789'))))
def test_match_history(region_tag, profile_id, region_id, profile_name):
    data = match_history(region_tag, profile_id, region_id, profile_name, locale='zhcn')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/profile/{profile_id}/{region_id}/{profile_name}/matches')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'zh_CN'


@pytest.mark.parametrize('region_tag, profile_id, region_id, profile_name',
                         list(product(INVALID_REGIONS, (984393, 208709586, 827894), (1, 2, 3),
                                      ('rando12345678', 'boredom7902897045', 'tired108400789'))))
def test_match_history_invalid_region_tag(region_tag, profile_id, region_id, profile_name):
    with pytest.raises(BNetRegionError):
        match_history(region_tag, profile_id, region_id, profile_name, locale='zhcn')


@pytest.mark.parametrize('region_tag, ladder_id',
                         list(product(VALID_REGIONS, (984393, 208709586, 827894))))
def test_ladder(region_tag, ladder_id):
    data = ladder(region_tag, ladder_id, locale='zhcn')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/ladder/{ladder_id}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'zh_CN'


@pytest.mark.parametrize('region_tag, ladder_id',
                         list(product(INVALID_REGIONS, (984393, 208709586, 827894))))
def test_ladder_invalid_region_tag(region_tag, ladder_id):
    with pytest.raises(BNetRegionError):
        ladder(region_tag, ladder_id, locale='zhcn')


@pytest.mark.parametrize('region_tag', VALID_REGIONS)
def test_achievements_valid_region_id(region_tag):
    data = achievements(region_tag, locale='zhcn')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/data/achievements')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'zh_CN'


@pytest.mark.parametrize('region_tag', INVALID_REGIONS)
def test_achievements_invalid_region_tag(region_tag):
    with pytest.raises(BNetRegionError):
        achievements(region_tag, locale='zhcn')


@pytest.mark.parametrize('region_tag', VALID_REGIONS)
def test_rewards_valid_region_id(region_tag):
    data = rewards(region_tag, locale='zhcn')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/data/rewards')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'zh_CN'


@pytest.mark.parametrize('region_tag', INVALID_REGIONS)
def test_rewards_invalid_region_tag(region_tag):
    with pytest.raises(BNetRegionError):
        rewards(region_tag, locale='zhcn')
