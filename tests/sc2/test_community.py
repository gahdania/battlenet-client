from itertools import product
import pytest

from battlenet_client.constants import VALID_REGIONS
from battlenet_client.utils import slugify
from battlenet_client.sc2.community import static, metadata, profile, ladder, grandmaster, season, player
from battlenet_client.sc2.community import legacy_profile, legacy_ladder, legacy_ladders, legacy_rewards
from battlenet_client.sc2.community import legacy_match_history, legacy_achievements
from battlenet_client.exceptions import BNetRegionNotFoundError, BNetRegionError, BNetValueError
from ..constants import INVALID_REGIONS

VALID_REGIONS = list(VALID_REGIONS)
VALID_REGIONS.remove('cn')

INVALID_REGIONS = list(INVALID_REGIONS)


@pytest.mark.parametrize('region_tag, region_id',
                         list(product(VALID_REGIONS,
                                      (1, 2, 3))))
def test_static_valid(region_tag, region_id):
    data = static(region_tag, region_id, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/static/profile/{region_id}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, region_id',
                         list(product(VALID_REGIONS,
                                      (10, 20, 'Zz'))))
def test_static_invalid_region_id(region_tag, region_id):
    with pytest.raises(BNetValueError):
        static(region_tag, region_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id',
                         list(product(INVALID_REGIONS,
                                      (1, 2, 3))))
def test_static_invalid_region_tag(region_tag, region_id):
    with pytest.raises(BNetRegionNotFoundError):
        static(region_tag, region_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id',
                         list(product(('cn',),
                                      (1, 2, 3))))
def test_static_invalid_region_tag_cn(region_tag, region_id):
    with pytest.raises(BNetRegionError):
        static(region_tag, region_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(VALID_REGIONS, (1, 3, 5), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_metadata_valid_region_id(region_tag, region_id, realm_id, profile_id):
    data = metadata(region_tag, region_id, realm_id, profile_id, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/metadata/profile/{region_id}/{realm_id}/{profile_id}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(VALID_REGIONS, (10, 'ZZ'), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_metadata_invalid_region_id(region_tag, region_id, realm_id, profile_id):
    with pytest.raises(BNetValueError):
        metadata(region_tag, region_id, realm_id, profile_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(INVALID_REGIONS, (1, 3), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_metadata_invalid_region_tag(region_tag, region_id, realm_id, profile_id):
    with pytest.raises(BNetRegionNotFoundError):
        metadata(region_tag, region_id,  realm_id, profile_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(('cn',), (1, 3), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_metadata_invalid_region_tag_cn(region_tag, region_id, realm_id, profile_id):
    with pytest.raises(BNetRegionError):
        metadata(region_tag, region_id, realm_id, profile_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(VALID_REGIONS, (1, 3, 5), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_profile_valid_region_id(region_tag, region_id, realm_id, profile_id):
    data = profile(region_tag, region_id, realm_id, profile_id, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/profile/{region_id}/{realm_id}/{profile_id}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(VALID_REGIONS, (10, 'ZZ'), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_profile_invalid_region_id(region_tag, region_id, realm_id, profile_id):
    with pytest.raises(BNetValueError):
        profile(region_tag, region_id, realm_id, profile_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(INVALID_REGIONS, (1, 3), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_profile_invalid_region_tag(region_tag, region_id, realm_id, profile_id):
    with pytest.raises(BNetRegionNotFoundError):
        profile(region_tag, region_id, realm_id, profile_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(('cn',), (1, 3), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_profile_invalid_region_tag(region_tag, region_id, realm_id, profile_id):
    with pytest.raises(BNetRegionError):
        profile(region_tag, region_id, realm_id, profile_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(VALID_REGIONS, (1, 3, 5), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_ladder_default_ladder(region_tag, region_id, realm_id, profile_id):
    data = ladder(region_tag, region_id, realm_id, profile_id, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/profile/{region_id}/{realm_id}/{profile_id}/ladder/summary')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(VALID_REGIONS, (10, 'ZZ'), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_ladder_default_ladder_invalid_region_id(region_tag, region_id, realm_id, profile_id):
    with pytest.raises(BNetValueError):
        ladder(region_tag, region_id, realm_id, profile_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(INVALID_REGIONS, (1, 3), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_ladder_default_ladder_invalid_region_tag(region_tag, region_id, realm_id, profile_id):
    with pytest.raises(BNetRegionNotFoundError):
        ladder(region_tag, region_id, realm_id, profile_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(('cn',), (1, 3), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_ladder_default_ladder_invalid_region_tag_cn(region_tag, region_id, realm_id, profile_id):
    with pytest.raises(BNetRegionError):
        ladder(region_tag, region_id, realm_id, profile_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id, ladder_id',
                         list(product(VALID_REGIONS, (1, 2, 3, 5), (1788, 9138, 1093),
                                      (3, 123, 187389), ('summary', 1))))
def test_ladder_explicit_ladder(region_tag, region_id, realm_id, profile_id, ladder_id):
    data = ladder(region_tag, region_id, realm_id, profile_id, ladder_id=ladder_id, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/profile/{region_id}/{realm_id}/{profile_id}/ladder/{ladder_id}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id, ladder_id',
                         list(product(VALID_REGIONS, (10, 'ZZ'), (1788, 9138, 1093),
                                      (3, 123, 187389), ('summary', 1))))
def test_ladder_explicit_ladder_invalid_region_id(region_tag, region_id, realm_id, profile_id, ladder_id):
    with pytest.raises(BNetValueError):
        ladder(region_tag, region_id, realm_id, profile_id, ladder_id=ladder_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id, ladder_id',
                         list(product(INVALID_REGIONS, (1, 3, 5), (1788, 9138, 1093),
                                      (3, 123, 187389), ('summary', 1))))
def test_ladder_explicit_ladder_invalid_region_tag(region_tag, region_id, realm_id, profile_id, ladder_id):
    with pytest.raises(BNetRegionNotFoundError):
        ladder(region_tag, region_id, realm_id, profile_id, ladder_id=ladder_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id, ladder_id',
                         list(product(('cn',), (1, 3, 5), (1788, 9138, 1093),
                                      (3, 123, 187389), ('summary', 1))))
def test_ladder_explicit_ladder_invalid_region_tag_cn(region_tag, region_id, realm_id, profile_id, ladder_id):
    with pytest.raises(BNetRegionError):
        ladder(region_tag, region_id, realm_id, profile_id, ladder_id=ladder_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id',
                         list(product(VALID_REGIONS, (1, 3, 5))))
def test_grandmaster_id_valid_region_id(region_tag, region_id):
    data = grandmaster(region_tag, region_id, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/ladder/grandmaster/{region_id}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, region_id',
                         list(product(VALID_REGIONS, (10, 'ZZ'))))
def test_grandmaster_explicit_grandmaster_invalid_region_id_(region_tag, region_id):
    with pytest.raises(BNetValueError):
        grandmaster(region_tag, region_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id',
                         list(product(INVALID_REGIONS, (1, 3, 5))))
def test_grandmaster_invalid_region_tag_explicit_grandmaster(region_tag, region_id):
    with pytest.raises(BNetRegionNotFoundError):
        grandmaster(region_tag, region_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id',
                         list(product(VALID_REGIONS, (1, 3, 5))))
def test_season_id_valid_region_id(region_tag, region_id):
    data = season(region_tag, region_id, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/ladder/season/{region_id}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, region_id',
                         list(product(VALID_REGIONS, (10, 'ZZ'))))
def test_season_id_explicit_season_invalid_region(region_tag, region_id):
    with pytest.raises(BNetValueError):
        season(region_tag, region_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id',
                         list(product(VALID_REGIONS, (10, 'ZZ'))))
def test_season_id_explicit_season_invalid_region(region_tag, region_id):
    with pytest.raises(BNetValueError):
        season(region_tag, region_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id',
                         list(product(('cn',), (10, 'ZZ'))))
def test_season_id_explicit_season_invalid_region_cn(region_tag, region_id):
    with pytest.raises(BNetValueError):
        season(region_tag, region_id, locale='enus')


@pytest.mark.parametrize('region_tag, account_id',
                         list(product(VALID_REGIONS, ('rando12345', 'boredom10394020', 'hensteeth1234'))))
def test_player_valid_region_id(region_tag, account_id):
    data = player(region_tag, account_id, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/player/{slugify(account_id)}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, account_id',
                         list(product(INVALID_REGIONS, ('rando12345', 'boredom10394020', 'hensteeth1234'))))
def test_player_invalid_region_tag(region_tag, account_id):
    with pytest.raises(BNetRegionNotFoundError):
        player(region_tag, account_id, locale='enus')


@pytest.mark.parametrize('region_tag, account_id',
                         list(product(('cn',), ('rando12345', 'boredom10394020', 'hensteeth1234'))))
def test_player_invalid_region_tag_cn(region_tag, account_id):
    with pytest.raises(BNetRegionError):
        player(region_tag, account_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(VALID_REGIONS, (1, 3, 5), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_legacy_profile_id_valid_region_id(region_tag, region_id, realm_id, profile_id):
    data = legacy_profile(region_tag, region_id, realm_id, profile_id, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/legacy/profile/{region_id}/{realm_id}/{profile_id}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(VALID_REGIONS, (10, 'ZZ'), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_legacy_profile_explicit_legacy_profile_invalid_region_id(region_tag, region_id, realm_id, profile_id):
    with pytest.raises(BNetValueError):
        legacy_profile(region_tag, region_id, realm_id, profile_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(INVALID_REGIONS, (1, 3, 5), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_legacy_profile_explicit_legacy_profile_invalid_region_tag(region_tag, region_id, realm_id, profile_id):
    with pytest.raises(BNetRegionNotFoundError):
        legacy_profile(region_tag, region_id, realm_id, profile_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(('cn',), (1, 3, 5), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_legacy_profile_explicit_legacy_profile_invalid_region_tag_cn(region_tag, region_id, realm_id, profile_id):
    with pytest.raises(BNetRegionError):
        legacy_profile(region_tag, region_id, realm_id, profile_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(VALID_REGIONS, (1, 3, 5), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_legacy_ladders_id_valid_region_id(region_tag, region_id, realm_id, profile_id):
    data = legacy_ladders(region_tag, region_id, realm_id, profile_id, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/legacy/profile/{region_id}/{realm_id}/{profile_id}/ladders')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(VALID_REGIONS, (10, 'ZZ'), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_legacy_ladders_explicit_legacy_ladders_invalid_region_id(region_tag, region_id, realm_id, profile_id):
    with pytest.raises(BNetValueError):
        legacy_ladders(region_tag, region_id, realm_id, profile_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(INVALID_REGIONS, (1, 3, 5), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_legacy_ladders_explicit_legacy_ladders_invalid_region_tag(region_tag, region_id, realm_id, profile_id):
    with pytest.raises(BNetRegionNotFoundError):
        legacy_ladders(region_tag, region_id, realm_id, profile_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(('cn',), (1, 3, 5), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_legacy_profile_explicit_legacy_profile_invalid_region_tag_cn(region_tag, region_id, realm_id, profile_id):
    with pytest.raises(BNetRegionError):
        legacy_profile(region_tag, region_id, realm_id, profile_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(VALID_REGIONS, (1, 3, 5), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_legacy_match_history_id_valid_region_id(region_tag, region_id, realm_id, profile_id):
    data = legacy_match_history(region_tag, region_id, realm_id, profile_id, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/legacy/profile/{region_id}/{realm_id}/{profile_id}/matches')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(VALID_REGIONS, (10, 'ZZ'), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_legacy_match_history_explicit_legacy_match_history_invalid_region_id(region_tag, region_id, realm_id,
                                                                              profile_id):
    with pytest.raises(BNetValueError):
        legacy_match_history(region_tag, region_id, realm_id, profile_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(INVALID_REGIONS, (1, 3, 5), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_legacy_match_history_explicit_legacy_match_history_invalid_region_tag(region_tag, region_id, realm_id,
                                                                               profile_id):
    with pytest.raises(BNetRegionNotFoundError):
        legacy_match_history(region_tag, region_id, realm_id, profile_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id, profile_id',
                         list(product(('cn',), (1, 3, 5), (1788, 9138, 1093),
                                      (3, 123, 187389))))
def test_legacy_match_history_explicit_legacy_match_history_invalid_region_tag_cn(region_tag, region_id, realm_id,
                                                                                  profile_id):
    with pytest.raises(BNetRegionError):
        legacy_match_history(region_tag, region_id, realm_id, profile_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id',
                         list(product(VALID_REGIONS, (1, 3, 5), (1788, 9138, 1093))))
def test_legacy_ladder_id_valid_region_id(region_tag, region_id, realm_id):
    data = legacy_ladder(region_tag, region_id, realm_id, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/legacy/ladder/{region_id}/{realm_id}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, region_id, realm_id',
                         list(product(VALID_REGIONS, (10, 'ZZ'), (1788, 9138, 1093))))
def test_legacy_ladder_explicit_legacy_ladder_invalid_region_id(region_tag, region_id, realm_id):
    with pytest.raises(BNetValueError):
        legacy_ladder(region_tag, region_id, realm_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id',
                         list(product(INVALID_REGIONS, (1, 3, 5), (1788, 9138, 1093))))
def test_legacy_ladder_explicit_legacy_ladder_invalid_region_tag(region_tag, region_id, realm_id):
    with pytest.raises(BNetRegionNotFoundError):
        legacy_ladder(region_tag, region_id, realm_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id, realm_id',
                         list(product(('cn',), (1, 3, 5), (1788, 9138, 1093))))
def test_legacy_ladder_explicit_legacy_ladder_invalid_region_tag_cn(region_tag, region_id, realm_id):
    with pytest.raises(BNetRegionError):
        legacy_ladder(region_tag, region_id, realm_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id',
                         list(product(VALID_REGIONS, (1, 3, 5))))
def test_legacy_achievements_id_valid_region_id(region_tag, region_id):
    data = legacy_achievements(region_tag, region_id, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/legacy/data/achievements/{region_id}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, region_id',
                         list(product(VALID_REGIONS, (10, 'ZZ'))))
def test_legacy_achievements_explicit_legacy_achievements_invalid_region_id(region_tag, region_id):
    with pytest.raises(BNetValueError):
        legacy_achievements(region_tag, region_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id',
                         list(product(INVALID_REGIONS, (1, 3, 5))))
def test_legacy_achievements_explicit_legacy_achievements_invalid_region_tag(region_tag, region_id):
    with pytest.raises(BNetRegionNotFoundError):
        legacy_achievements(region_tag, region_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id',
                         list(product(('cn',), (1, 3, 5))))
def test_legacy_achievements_explicit_legacy_achievements_invalid_region_tag_cn(region_tag, region_id):
    with pytest.raises(BNetRegionError):
        legacy_achievements(region_tag, region_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id',
                         list(product(VALID_REGIONS, (1, 3, 5))))
def test_legacy_rewards_id_valid_region_id(region_tag, region_id):
    data = legacy_rewards(region_tag, region_id, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'sc2/legacy/data/rewards/{region_id}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, region_id',
                         list(product(VALID_REGIONS, (10, 'ZZ'))))
def test_legacy_rewards_explicit_legacy_rewards_invalid_region_id(region_tag, region_id):
    with pytest.raises(BNetValueError):
        legacy_rewards(region_tag, region_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id',
                         list(product(INVALID_REGIONS, (1, 3, 5))))
def test_legacy_rewards_explicit_legacy_rewards_invalid_region_tag(region_tag, region_id):
    with pytest.raises(BNetRegionNotFoundError):
        legacy_rewards(region_tag, region_id, locale='enus')


@pytest.mark.parametrize('region_tag, region_id',
                         list(product(('cn',), (1, 3, 5))))
def test_legacy_rewards_explicit_legacy_rewards_invalid_region_tag_cn(region_tag, region_id):
    with pytest.raises(BNetRegionError):
        legacy_rewards(region_tag, region_id, locale='enus')
