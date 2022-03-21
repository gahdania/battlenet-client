import pytest
from itertools import product

from battlenet_client.exceptions import BNetRegionError, BNetValueError
from battlenet_client.constants import VALID_REGIONS
from battlenet_client.wow.profile import (
    account_profile_summary, protected_character_profile_summary, account_collections, achievement_summary,
    appearance_summary, collections, encounters, equipment_summary, hunter_pets_summary, media_summary, mythic_keystone,
    professions_summary, profile, pvp, quests, reputations_summary, soulbinds, specializations_summary,
    statistics_summary, title_summary, guild
)
from battlenet_client import utils
from battlenet_client.wow.constants import Release
from ..constants import INVALID_REGIONS


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.ALL)))
def test_account_profile_summary_default_index(region_tag, release):
    data = account_profile_summary(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'profile/user/wow')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.ALL)))
def test_account_profile_summary_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionError):
        account_profile_summary(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_id, character_id',
                         list(product(VALID_REGIONS, Release.ALL, (1, '1', 1234, '1234'), (56065486, "56546846"))))
def test_account_protected_character_profile_summary_id(region_tag, release, realm_id, character_id):
    data = protected_character_profile_summary(region_tag, realm_id, character_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'profile/user/wow/protected-character/{realm_id}-{character_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_id, character_id',
                         list(product(INVALID_REGIONS, Release.ALL, (1, '1', 1234, '1234'), (56065486, "56546846"))))
def test_protected_character_profile_summary_id_invalid_region(region_tag, release, realm_id, character_id):
    with pytest.raises(BNetRegionError):
        protected_character_profile_summary(region_tag, realm_id, character_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.ALL)))
def test_account_collections_default_index(region_tag, release):
    data = account_collections(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'profile/user/wow/collections')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.ALL)))
def test_account_collections_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionError):
        account_collections(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, collection_type',
                         list(product(VALID_REGIONS, Release.ALL, (None, 'mounts', 'pets'))))
def test_account_collections_id(region_tag, release, collection_type):
    data = account_collections(region_tag, category=collection_type, release=release, locale='enus')
    assert isinstance(data, tuple)
    if collection_type is None:
        assert data[0].endswith(f'profile/user/wow/collections')
    else:
        assert data[0].endswith(f'profile/user/wow/collections/{collection_type}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, collection_type',
                         list(product(INVALID_REGIONS, Release.ALL, (None, 'mounts', 'pets'))))
def test_character_profile_summary_id_invalid_region(region_tag, release, collection_type):
    with pytest.raises(BNetRegionError):
        account_collections(region_tag, category=collection_type, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, collection_type',
                         list(product(VALID_REGIONS, Release.ALL, ('achivements', 'encounters'))))
def test_character_profile_summary_id_invalid_region(region_tag, release, collection_type):
    with pytest.raises(BNetValueError):
        account_collections(region_tag, category=collection_type, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_achievement_summary_id(region_tag, release, realm_slug, character_slug):
    data = achievement_summary(region_tag, realm_slug, character_slug, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}/achievements'
    assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_achievement_summary_id_invalid_region(region_tag, release, realm_slug, character_slug):
    with pytest.raises(BNetRegionError):
        achievement_summary(region_tag, realm_slug, character_slug, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug, stats',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'), (True, False))))
def test_character_achievement_summary_statistics_id(region_tag, release, realm_slug, character_slug, stats):
    data = achievement_summary(region_tag, realm_slug, character_slug, statistics=stats, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}/achievements'
    if stats:
        assert data[0].endswith(f"{base_url}/statistics")
    else:
        assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug, stats_flag',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'), (True, False))))
def test_character_achievement_summary_statistics_id_invalid_region(region_tag, release, realm_slug, character_slug,
                                                                    stats_flag):
    with pytest.raises(BNetRegionError):
        achievement_summary(region_tag, realm_slug, character_slug, statistics=stats_flag, release=release,
                            locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_appearance_summary_default_index(region_tag, release, realm_slug, character_slug):
    data = appearance_summary(region_tag, realm_slug, character_slug, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}/appearance'
    assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_appearance_summary_default_index_invalid_region(region_tag, release, realm_slug, character_slug):
    with pytest.raises(BNetRegionError):
        appearance_summary(region_tag, realm_slug, character_slug, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_collections_default_index(region_tag, release, realm_slug, character_slug):
    data = collections(region_tag, realm_slug, character_slug, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}/collections'
    assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_collections_default_index_invalid_region(region_tag, release, realm_slug, character_slug):
    with pytest.raises(BNetRegionError):
        collections(region_tag, realm_slug, character_slug, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug, collection_type',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'), (None, 'mounts', 'pets'))))
def test_character_collections_id(region_tag, release, realm_slug, character_slug, collection_type):
    data = collections(region_tag, realm_slug, character_slug, category=collection_type, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}/collections'
    if collection_type:
        assert data[0].endswith(f"{base_url}/{collection_type}")
    else:
        assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug, collection_type',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'), (None, 'mounts', 'pets'))))
def test_character_collections_id_invalid_region(region_tag, release, realm_slug, character_slug, collection_type):
    with pytest.raises(BNetValueError):
        collections(region_tag, realm_slug, character_slug, category=collection_type, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug, collection_type',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'), ('achievements', 'encounters'))))
def test_character_collections_id_invalid_category(region_tag, release, realm_slug, character_slug, collection_type):
    with pytest.raises(BNetValueError):
        collections(region_tag, realm_slug, character_slug, category=collection_type, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_encounters_default_index(region_tag, release, realm_slug, character_slug):
    data = encounters(region_tag, realm_slug, character_slug, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}/encounters'
    assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_encounters_default_index_invalid_region(region_tag, release, realm_slug, character_slug):
    with pytest.raises(BNetRegionError):
        encounters(region_tag, realm_slug, character_slug, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug, collection_type',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'), (None, 'dungeons', 'raids'))))
def test_character_encounters_id(region_tag, release, realm_slug, character_slug, collection_type):
    data = encounters(region_tag, realm_slug, character_slug, category=collection_type, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}/encounters'
    if collection_type:
        assert data[0].endswith(f"{base_url}/{collection_type}")
    else:
        assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug, collection_type',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'), (None, 'dungeons', 'raids'))))
def test_character_collections_id_invalid_region(region_tag, release, realm_slug, character_slug, collection_type):
    with pytest.raises(BNetRegionError):
        collections(region_tag, realm_slug, character_slug, category=collection_type, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug, collection_type',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'), ('achievements', 'encounters'))))
def test_character_collections_id_invalid_category(region_tag, release, realm_slug, character_slug, collection_type):
    with pytest.raises(BNetValueError):
        collections(region_tag, realm_slug, character_slug, category=collection_type, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_equipment_summary_default_index(region_tag, release, realm_slug, character_slug):
    data = equipment_summary(region_tag, realm_slug, character_slug, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}/equipment'
    assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_equipment_summary_default_index_invalid_region(region_tag, release, realm_slug, character_slug):
    with pytest.raises(BNetRegionError):
        equipment_summary(region_tag, realm_slug, character_slug, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_hunter_pets_summary_default_index(region_tag, release, realm_slug, character_slug):
    data = hunter_pets_summary(region_tag, realm_slug, character_slug, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}/hunter-pets'
    assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_hunter_pets_summary_default_index_invalid_region(region_tag, release, realm_slug, character_slug):
    with pytest.raises(BNetRegionError):
        hunter_pets_summary(region_tag, realm_slug, character_slug, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_media_summary_default_index(region_tag, release, realm_slug, character_slug):
    data = media_summary(region_tag, realm_slug, character_slug, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}/character-media'
    assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_media_summary_default_index_invalid_region(region_tag, release, realm_slug, character_slug):
    with pytest.raises(BNetRegionError):
        media_summary(region_tag, realm_slug, character_slug, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_mythic_keystone_default_index(region_tag, release, realm_slug, character_slug):
    data = mythic_keystone(region_tag, realm_slug, character_slug, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}/mythic-keystone-profile'
    assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.ALL)))
def test_character_mythic_keystone_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionError):
        mythic_keystone(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug, season_id',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'), (None, 1, 67))))
def test_character_mythic_keystone_id(region_tag, release, realm_slug, character_slug, season_id):
    data = mythic_keystone(region_tag, realm_slug, character_slug, season_id=season_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}/mythic-keystone-profile'
    if season_id:
        assert data[0].endswith(f"{base_url}/season/{season_id}")
    else:
        assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug, season_id',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'), (None, 1, 67))))
def test_character_mythic_keystone_id_invalid_region(region_tag, release, realm_slug, character_slug, season_id):
    with pytest.raises(BNetRegionError):
        mythic_keystone(region_tag, realm_slug, character_slug, season_id=season_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_professions_summary_default_index(region_tag, release, realm_slug, character_slug):
    data = professions_summary(region_tag, realm_slug, character_slug, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}/professions'
    assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_professions_summary_default_index_invalid_region(region_tag, release, realm_slug, character_slug):
    with pytest.raises(BNetRegionError):
        professions_summary(region_tag, realm_slug, character_slug, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug, status',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'), (True, False))))
def test_character_profile_statistics_id(region_tag, release, realm_slug, character_slug, status):
    data = profile(region_tag, realm_slug, character_slug, status=status, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}'
    if status:
        assert data[0].endswith(f"{base_url}/status")
    else:
        assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug, status',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'), (True, False))))
def test_character_profile_statistics_id_invalid_region(region_tag, release, realm_slug, character_slug, status):
    with pytest.raises(BNetRegionError):
        profile(region_tag, realm_slug, character_slug, status=status, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug, bracket',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'),
                                      (None, '2v2', '3v3', '5v5', 'rbg'))))
def test_character_pvp_id(region_tag, release, realm_slug, character_slug, bracket):
    data = pvp(region_tag, realm_slug, character_slug, pvp_bracket=bracket, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}'
    if bracket:
        assert data[0].endswith(f"{base_url}/pvp-bracket/{bracket}")
    else:
        assert data[0].endswith(f"{base_url}/pvp-summary")
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug, bracket',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'),
                                      (None, '2v2', '3v3', '5v5', 'rbg'))))
def test_character_pvp_statistics_id_invalid_region(region_tag, release, realm_slug, character_slug, bracket):
    with pytest.raises(BNetRegionError):
        pvp(region_tag, realm_slug, character_slug, pvp_bracket=bracket, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug, bracket',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'),
                                      ('1v1', '4b4', '5b5', 'ubg'))))
def test_character_pvp_statistics_id_invalid_bracket(region_tag, release, realm_slug, character_slug, bracket):
    with pytest.raises(BNetValueError):
        pvp(region_tag, realm_slug, character_slug, pvp_bracket=bracket, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug, completed',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'), (True, False))))
def test_character_quests_id(region_tag, release, realm_slug, character_slug, completed):
    data = quests(region_tag, realm_slug, character_slug, completed=completed, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}/quests'
    if completed:
        assert data[0].endswith(f"{base_url}/completed")
    else:
        assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug, completed',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'), (True, False))))
def test_character_quests_id_invalid_region(region_tag, release, realm_slug, character_slug, completed):
    with pytest.raises(BNetRegionError):
        quests(region_tag, realm_slug, character_slug, completed=completed, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_reputations_summary_default_index(region_tag, release, realm_slug, character_slug):
    data = reputations_summary(region_tag, realm_slug, character_slug, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}/reputations'
    assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_reputations_summary_default_index_invalid_region(region_tag, release, realm_slug, character_slug):
    with pytest.raises(BNetRegionError):
        reputations_summary(region_tag, realm_slug, character_slug, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(VALID_REGIONS, Release.ALL, ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_soulbinds_default_index(region_tag, release, realm_slug, character_slug):
    data = soulbinds(region_tag, realm_slug, character_slug, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}/soulbinds'
    assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_soulbinds_default_index_invalid_region(region_tag, release, realm_slug, character_slug):
    with pytest.raises(BNetRegionError):
        soulbinds(region_tag, realm_slug, character_slug, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(VALID_REGIONS, Release.ALL, ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_specializations_summary_default_index(region_tag, release, realm_slug, character_slug):
    data = specializations_summary(region_tag, realm_slug, character_slug, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}/specializations'
    assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_characters_specializations_summary_default_index_invalid_region(region_tag, release, realm_slug,
                                                                         character_slug):
    with pytest.raises(BNetRegionError):
        specializations_summary(region_tag, realm_slug, character_slug, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(VALID_REGIONS, Release.ALL, ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_statistics_summary_default_index(region_tag, release, realm_slug, character_slug):
    data = statistics_summary(region_tag, realm_slug, character_slug, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}/statistics'
    assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_characters_statistics_summary_default_index_invalid_region(region_tag, release, realm_slug, character_slug):
    with pytest.raises(BNetRegionError):
        statistics_summary(region_tag, realm_slug, character_slug, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_character_titles_summary_default_index(region_tag, release, realm_slug, character_slug):
    data = title_summary(region_tag, realm_slug, character_slug, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'profile/wow/character/{utils.slugify(realm_slug)}/{utils.slugify(character_slug)}/titles'
    assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, character_slug',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('Gahdania', 'Hirotoh', 'Stonetoh'))))
def test_characters_title_summary_default_index_invalid_region(region_tag, release, realm_slug, character_slug):
    with pytest.raises(BNetRegionError):
        title_summary(region_tag, realm_slug, character_slug, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, guild_slug, category',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('To The Rescue', 'Thanks I hate it', 'Knights of the WoW Table'),
                                      (None, 'activity', 'achievements', 'roster'))))
def test_guild_id(region_tag, release, realm_slug, guild_slug, category):
    data = guild(region_tag, realm_slug, guild_slug, category=category, release=release, locale='enus')
    assert isinstance(data, tuple)
    base_url = f'data/wow/guild/{utils.slugify(realm_slug)}/{utils.slugify(guild_slug)}'
    if category:
        assert data[0].endswith(f"{base_url}/{category}")
    else:
        assert data[0].endswith(base_url)
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'profile-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'profile-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug, guild_slug, category',
                         list(product(INVALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('To The Rescue', 'Thanks I hate it', 'Knights of the WoW Table'),
                                      (None, 'activity', 'achievements', 'roster'))))
def test_guild_default_index_invalid_region(region_tag, release, realm_slug, guild_slug, category):
    with pytest.raises(BNetRegionError):
        guild(region_tag, realm_slug, guild_slug, category=category, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug, guild_slug, category',
                         list(product(VALID_REGIONS, Release.ALL,
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'),
                                      ('To The Rescue', 'Thanks I hate it', 'Knights of the WoW Table'),
                                      ('laxidazial', 'undergrad', 'poster-child'))))
def test_guild_default_index_invalid_category(region_tag, release, realm_slug, guild_slug, category):
    with pytest.raises(BNetValueError):
        guild(region_tag, realm_slug, guild_slug, category=category, release=release, locale='enus')
