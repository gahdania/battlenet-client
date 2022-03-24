import pytest
from itertools import product

from battlenet_client.exceptions import BNetRegionNotFoundError, BNetValueError, BNetReleaseError
from battlenet_client.decorators import VALID_REGIONS
from battlenet_client import utils
from battlenet_client.wow.game_data import (
    achievement, achievement_category, achievement_media, auction, azerite_essence, azerite_essence_media,
    azerite_essence_search, conduit, connected_realm, connected_realm_search, covenant, covenant_media, creature,
    creature_display_media, creature_family, creature_family_media, creature_search, creature_type,
    guild_crest_components_index, guild_crest_media, item, item_class, item_media, item_search, item_set, item_subclass,
    journal_encounter, journal_encounter_search, journal_expansion, journal_instance, journal_instance_media,
    media_search, modified_crafting, modified_crafting_category, modified_crafting_reagent_slot_type, mount,
    mount_search, mythic_keystone_affix, mythic_keystone_affix_media, mythic_keystone_dungeon, mythic_keystone_index,
    mythic_keystone_leaderboard, mythic_keystone_period, mythic_keystone_season, mythic_raid_leaderboard,
    pet, pet_ability, pet_ability_media, pet_media, playable_class, playable_class_media, playable_race,
    playable_spec, playable_spec_media, power_type, profession, profession_media, profession_skill_tier,
    pvp_leaderboard, pvp_regions, pvp_regional_season, pvp_rewards_index, pvp_season, pvp_talent, pvp_talent_slots,
    pvp_tier, pvp_tier_media, quest, quest_area, quest_category, quest_type, realm, realm_search, recipe, recipe_media,
    region, reputation_faction, reputation_tier, soulbind, spell, spell_media, spell_search, talent, tech_talent,
    tech_talent_media, tech_talent_tree, title, wow_token_index
)

from battlenet_client.wow.constants import Release
from ..constants import INVALID_REGIONS

NOT_RETAIL = list(Release.all())
NOT_RETAIL.remove(Release.RETAIL)


@pytest.mark.parametrize('region_tag, release', list(product(VALID_REGIONS, Release.all())))
def test_achievement_category_default_index(region_tag, release):
    data = achievement_category(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/achievement-category/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'
    if release.lower() == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release.lower()}-{region_tag.lower()}'


@pytest.mark.parametrize('region_tag, release', list(product(VALID_REGIONS, Release.all())))
def test_achievement_category_default_index_all_locales(region_tag, release):
    data = achievement_category(region_tag, release=release, locale=None)
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/achievement-category/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    assert data[1]['locale'] is None
    if release.lower() == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release.lower()}-{region_tag.lower()}'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_achievement_category_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        achievement_category(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, category',
                         list(product(VALID_REGIONS, Release.all(), ('index', 81, '81'))))
def test_achievement_category_id(region_tag, release, category):
    data = achievement_category(region_tag, category_id=category, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/achievement-category/{category}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'
    if release.lower() == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release.lower()}-{region_tag.lower()}'


@pytest.mark.parametrize('region_tag, release, category',
                         list(product(VALID_REGIONS, Release.all(), ('index', 81, '81'))))
def test_achievement_category_id_all_locales(region_tag, release, category):
    data = achievement_category(region_tag, category_id=category, release=release)
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/achievement-category/{category}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    assert data[1]['locale'] is None
    if release.lower() == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release.lower()}-{region_tag.lower()}'


@pytest.mark.parametrize('region_tag, release, category',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 81, '81'))))
def test_achievement_category_id_invalid_region(region_tag, release, category):
    with pytest.raises(BNetRegionNotFoundError):
        achievement_category(region_tag, category_id=category, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release', list(product(VALID_REGIONS, Release.all())))
def test_achievement_default_index(region_tag, release):
    data = achievement(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/achievement/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'
    if release.lower() == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release.lower()}-{region_tag.lower()}'


@pytest.mark.parametrize('region_tag, release', list(product(VALID_REGIONS, Release.all())))
def test_achievement_default_index_all_locales(region_tag, release):
    data = achievement(region_tag, release=release)
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/achievement/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    assert data[1]['locale'] is None
    if release.lower() == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release.lower()}-{region_tag.lower()}'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_achievement_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        achievement_category(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, achievement_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 6, '6'))))
def test_achievement_id(region_tag, release, achievement_id):
    data = achievement(region_tag, achievement_id=achievement_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/achievement/{achievement_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'
    if release.lower() == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release.lower()}-{region_tag.lower()}'


@pytest.mark.parametrize('region_tag, release, category',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 81, '81'))))
def test_achievement_id_invalid_region(region_tag, release, category):
    with pytest.raises(BNetRegionNotFoundError):
        achievement(region_tag, achievement_id=category, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, achievement_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 6, '6'))))
def test_achievement_media_id(region_tag, release, achievement_id):
    data = achievement_media(region_tag, achievement_id=achievement_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/media/achievement/{achievement_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'
    if release.lower() == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release.lower()}-{region_tag.lower()}'


@pytest.mark.parametrize('region_tag, release, category',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 81, '81'))))
def test_achievement_media_id_invalid_region(region_tag, release, category):
    with pytest.raises(BNetRegionNotFoundError):
        achievement_media(region_tag, achievement_id=category, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, connected_realm_id',
                         list(product(VALID_REGIONS, (Release.RETAIL,), (4, '4', 5, '5', 9, '9', 11, '11'))))
def test_auction_no_auction_house(region_tag, release, connected_realm_id):
    data = auction(region_tag, connected_realm_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/connected-realm/{connected_realm_id}/auctions')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'
    if release.lower() == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release.lower()}-{region_tag.lower()}'


@pytest.mark.parametrize('region_tag, release, connected_realm_id, house_id',
                         list(product(VALID_REGIONS, (Release.RETAIL,), (4, '4', 5, '5', 9, '9', 11, '11'), (2, 6, 7))))
def test_auction_auction_house_bnet_release_error(region_tag, release, connected_realm_id, house_id):
    with pytest.raises(BNetReleaseError):
        auction(region_tag, connected_realm_id, auction_house_id=house_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, connected_realm_id',
                         list(product(VALID_REGIONS, NOT_RETAIL, (4372, 5064))))
def test_auction_auction_house_index(region_tag, release, connected_realm_id):
    data = auction(region_tag, connected_realm_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/connected-realm/{connected_realm_id}/auctions/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'
    if release.lower() == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release.lower()}-{region_tag.lower()}'


@pytest.mark.parametrize('region_tag, release, connected_realm_id, house_id', (
    list(product(VALID_REGIONS, NOT_RETAIL, (4372, 5064), (2, 6, 7)))
))
def test_auction_auction_house_id(region_tag, release, connected_realm_id, house_id):
    data = auction(region_tag, connected_realm_id, auction_house_id=house_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/connected-realm/{connected_realm_id}/auctions/{house_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'
    if release.lower() == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release.lower()}-{region_tag.lower()}'


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, (Release.RETAIL,))))
def test_azerite_essence_default_index(region_tag, release):
    data = azerite_essence(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/azerite-essence/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'
    if release.lower() == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release.lower()}-{region_tag.lower()}'


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, (Release.RETAIL,))))
def test_azerite_essence_default_index_all_locales(region_tag, release):
    data = azerite_essence(region_tag, release=release)
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/azerite-essence/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    assert data[1]['locale'] is None
    if release.lower() == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release.lower()}-{region_tag.lower()}'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, (Release.RETAIL,))))
def test_azerite_essence_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        azerite_essence(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, essence_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 2, '2'))))
def test_azerite_essence_id(region_tag, release, essence_id):
    data = azerite_essence(region_tag, essence_id=essence_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/azerite-essence/{essence_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'
    if release.lower() == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release.lower()}-{region_tag.lower()}'


@pytest.mark.parametrize('region_tag, release, essence_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 2, '2'))))
def test_azerite_essence_id_invalid_region(region_tag, release, essence_id):
    with pytest.raises(BNetRegionNotFoundError):
        azerite_essence(region_tag, essence_id=essence_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_azerite_essence_search(region_tag, release):
    fields = {
        'allowed_specializations.id': 65,
        'orderby': 'name',
        '_page': 1
    }

    data = azerite_essence_search(region_tag, fields, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/search/azerite-essence')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'
    if release.lower() == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release.lower()}-{region_tag.lower()}'
    for k, v in fields.items():
        assert k in data[1]
        assert data[1][k] == v


@pytest.mark.parametrize('region_tag, release, essence_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 2, '2'))))
def test_azerite_essence_search_invalid_region(region_tag, release, essence_id):
    fields = {
        'allowed_specializations.id': 65,
        'orderby': 'name',
        '_page': 1
    }
    with pytest.raises(BNetRegionNotFoundError):
        azerite_essence_search(region_tag, fields, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, essence_id',
                         list(product(VALID_REGIONS, Release.all(), (2, '2'))))
def test_azerite_essence_media(region_tag, release, essence_id):
    data = azerite_essence_media(region_tag, essence_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/media/azerite-essence/{essence_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'
    if release.lower() == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release.lower()}-{region_tag.lower()}'


@pytest.mark.parametrize('region_tag, release, essence_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 2, '2'))))
def test_azerite_essence_media_id_invalid_region(region_tag, release, essence_id):
    with pytest.raises(BNetRegionNotFoundError):
        azerite_essence_media(region_tag, essence_id=essence_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_connected_realm_default_index(region_tag, release):
    data = connected_realm(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/connected-realm/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_connected_realm_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        connected_realm(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, cr_id',
                         list(product(VALID_REGIONS, Release.all(),
                                      ('index', 4, 5, 9, 11, 4372, 4373, 4374, 4376, 5064, 5066, 5072))))
def test_connected_realm_id(region_tag, release, cr_id):
    data = connected_realm(region_tag, connected_realm_id=cr_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/connected-realm/{cr_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, cr_id',
                         list(product(INVALID_REGIONS, Release.all(),
                                      ('index', 4, 5, 9, 11, 4372, 4373, 4374, 4376, 5064, 5066, 5072))))
def test_connected_realm_id_invalid_region(region_tag, release, cr_id):
    with pytest.raises(BNetRegionNotFoundError):
        connected_realm(region_tag, connected_realm_id=cr_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_connected_realm_search(region_tag, release):
    fields = {
        'status.type': 'UP',
        'realms.timezone': 'America/New_York',
        'orderby': 'id',
        '_page': 1
    }
    data = connected_realm_search(region_tag, fields, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/search/connected-realm')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'
    for k, v in fields.items():
        assert k in data[1]
        assert data[1][k] == v


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_connected_realm_search_invalid_region(region_tag, release):
    fields = {
        'status.type': 'UP',
        'realms.timezone': 'America/New_York',
        'orderby': 'id',
        '_page': 1
    }
    with pytest.raises(BNetRegionNotFoundError):
        connected_realm_search(region_tag, fields, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_covenant_default_index(region_tag, release):
    data = covenant(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/covenant/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_covenant_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        covenant(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, covenant_id',
                         list(product(VALID_REGIONS, Release.all(), (1, '1'))))
def test_covenant_id(region_tag, release, covenant_id):
    data = covenant(region_tag, covenant_id=covenant_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/covenant/{covenant_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, covenant_id',
                         list(product(INVALID_REGIONS, Release.all(), (1, '1'))))
def test_covenant_id_invalid_region(region_tag, release, covenant_id):
    with pytest.raises(BNetRegionNotFoundError):
        covenant(region_tag, covenant_id=covenant_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, covenant_id',
                         list(product(VALID_REGIONS, Release.all(), (1, '1'))))
def test_covenant_media_id(region_tag, release, covenant_id):
    data = covenant_media(region_tag, covenant_id=covenant_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/media/covenant/{covenant_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, covenant_id',
                         list(product(INVALID_REGIONS, Release.all(), (1, '1'))))
def test_covenant_media_id_invalid_region(region_tag, release, covenant_id):
    with pytest.raises(BNetRegionNotFoundError):
        covenant_media(region_tag, covenant_id=covenant_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_soulbind_default_index(region_tag, release):
    data = soulbind(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/covenant/soulbind/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_soulbind_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        soulbind(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, soulbind_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1'))))
def test_soulbind_id(region_tag, release, soulbind_id):
    data = soulbind(region_tag, soulbind_id=soulbind_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/covenant/soulbind/{soulbind_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, soulbind_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1, '1'))))
def test_soulbind_id_invalid_region(region_tag, release, soulbind_id):
    with pytest.raises(BNetRegionNotFoundError):
        soulbind(region_tag, soulbind_id=soulbind_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_conduit_default_index(region_tag, release):
    data = conduit(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/covenant/conduit/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_conduit_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        conduit(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, conduit_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 5, '5'))))
def test_conduit_id(region_tag, release, conduit_id):
    data = conduit(region_tag, conduit_id=conduit_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/covenant/conduit/{conduit_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, conduit_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1, '1'))))
def test_conduit_id_invalid_region(region_tag, release, conduit_id):
    with pytest.raises(BNetRegionNotFoundError):
        conduit(region_tag, conduit_id=conduit_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_creature_family_default_index(region_tag, release):
    data = creature_family(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/creature-family/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_creature_family_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        creature_family(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, family_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1'))))
def test_creature_family_id(region_tag, release, family_id):
    data = creature_family(region_tag, family_id=family_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/creature-family/{family_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, creature_family_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1, '1'))))
def test_creature_family_id_invalid_region(region_tag, release, creature_family_id):
    with pytest.raises(BNetRegionNotFoundError):
        creature_family(region_tag, creature_family_id=creature_family_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_creature_type_default_index(region_tag, release):
    data = creature_type(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/creature-type/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_creature_type_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        creature_type(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, type_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1'))))
def test_creature_type_id(region_tag, release, type_id):
    data = creature_type(region_tag, type_id=type_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/creature-type/{type_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, creature_type_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1, '1'))))
def test_creature_type_id_invalid_region(region_tag, release, creature_type_id):
    with pytest.raises(BNetRegionNotFoundError):
        creature_type(region_tag, creature_type_id=creature_type_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, creature_id',
                         list(product(VALID_REGIONS, Release.all(), (42722, '42722'))))
def test_creature_id(region_tag, release, creature_id):
    data = creature(region_tag, creature_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/creature/{creature_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, creature_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1, '1'))))
def test_creature_id_invalid_region(region_tag, release, creature_id):
    with pytest.raises(BNetRegionNotFoundError):
        creature(region_tag, creaturetype_id=creature_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_creature_search(region_tag, release):
    fields = {
        'name.en_US': 'Dragon',
        'orderby': 'id',
        '_page': 1
    }

    data = creature_search(region_tag, fields, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/search/creature')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'
    assert data[1]['locale'] == 'en_US'
    for k, v in fields.items():
        assert k in data[1]
        assert data[1][k] == v


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_creature_search_id_invalid_region(region_tag, release):
    fields = {
        'name.en_US': 'Dragon',
        'orderby': 'id',
        '_page': 1
    }

    with pytest.raises(BNetRegionNotFoundError):
        creature_search(region_tag, fields, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, creature_id',
                         list(product(VALID_REGIONS, Release.all(), (42722, '42722'))))
def test_creature_display_media_id(region_tag, release, creature_id):
    data = creature_display_media(region_tag, creature_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/media/creature-display/{creature_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, creature_display_media_id',
                         list(product(INVALID_REGIONS, Release.all(), (42722, '42722'))))
def test_creature_display_media_id_invalid_region(region_tag, release, creature_display_media_id):
    with pytest.raises(BNetRegionNotFoundError):
        creature_display_media(region_tag, creature_display_mediatype_id=creature_display_media_id, release=release,
                               locale='enus')


@pytest.mark.parametrize('region_tag, release, family_id',
                         list(product(VALID_REGIONS, Release.all(), (42722, '42722'))))
def test_creature_family_media_id(region_tag, release, family_id):
    data = creature_family_media(region_tag, family_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/media/creature-family/{family_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, creature_family_media_id',
                         list(product(INVALID_REGIONS, Release.all(), (42722, '42722'))))
def test_creature_family_media_id_invalid_region(region_tag, release, creature_family_media_id):
    with pytest.raises(BNetRegionNotFoundError):
        creature_family_media(region_tag, creature_family_mediatype_id=creature_family_media_id, release=release,
                              locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_guild_crest_components_default_index(region_tag, release):
    data = guild_crest_components_index(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/guild-crest/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_guild_crest_components_index_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        guild_crest_components_index(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, category, crest_id',
                         list(product(VALID_REGIONS, Release.all(), ('border', 'emblem'), (1, '1'))))
def test_guild_crest_media_category_and_id(region_tag, release, category, crest_id):
    data = guild_crest_media(region_tag, category, crest_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/media/guild-crest/{category}/{crest_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, category, crest_id',
                         list(product(INVALID_REGIONS, Release.all(), ('border', 'emblem'), (1, '1'))))
def test_guild_crest_media_category_id_invalid_region(region_tag, release, category, crest_id):
    with pytest.raises(BNetRegionNotFoundError):
        guild_crest_media(region_tag, category, crest_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, category, crest_id',
                         list(product(VALID_REGIONS, Release.all(), ('icon', 'lines'), (1, '1'))))
def test_guild_crest_media_category_id_invalid_category(region_tag, release, category, crest_id):
    with pytest.raises(BNetValueError):
        guild_crest_media(region_tag, category, crest_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_item_class_default_index(region_tag, release):
    data = item_class(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/item-class/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_item_class_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        item_class(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, item_class_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 0, '0'))))
def test_item_class_id(region_tag, release, item_class_id):
    data = item_class(region_tag, class_id=item_class_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/item-class/{item_class_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, item_class_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1, '1'))))
def test_item_class_id_invalid_region(region_tag, release, item_class_id):
    with pytest.raises(BNetRegionNotFoundError):
        item_class(region_tag, class_id=item_class_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_item_set_default_index(region_tag, release):
    data = item_set(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/item-set/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_item_set_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        item_set(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, item_set_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1'))))
def test_item_set_id(region_tag, release, item_set_id):
    data = item_set(region_tag, set_id=item_set_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/item-set/{item_set_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, item_set_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1, '1'))))
def test_item_set_id_invalid_region(region_tag, release, item_set_id):
    with pytest.raises(BNetRegionNotFoundError):
        item_set(region_tag, set_id=item_set_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, class_id, subclass_id',
                         list(product(VALID_REGIONS, Release.all(), (0, '0'), (0, '0'))))
def test_item_subclass_id(region_tag, release, class_id, subclass_id):
    data = item_subclass(region_tag, class_id, subclass_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/item-class/{class_id}/item-subclass/{subclass_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, class_id, subclass_id',
                         list(product(INVALID_REGIONS, Release.all(), (0, 0), (0, 0))))
def test_item_subclass_id_invalid_region(region_tag, release, class_id, subclass_id):
    with pytest.raises(BNetRegionNotFoundError):
        item_subclass(region_tag, class_id, subclass_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, item_id',
                         list(product(VALID_REGIONS, Release.all(), (19019, '10019'))))
def test_item_id(region_tag, release, item_id):
    data = item(region_tag, item_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/item/{item_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, item_id',
                         list(product(INVALID_REGIONS, Release.all(), (1019, '19019'))))
def test_item_id_invalid_region(region_tag, release, item_id):
    with pytest.raises(BNetRegionNotFoundError):
        item(region_tag, item_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, item_id',
                         list(product(VALID_REGIONS, Release.all(), (19019, '10019'))))
def test_item_media_id(region_tag, release, item_id):
    data = item_media(region_tag, item_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/media/item/{item_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, item_id',
                         list(product(INVALID_REGIONS, Release.all(), (1019, '19019'))))
def test_item_media_id_invalid_region(region_tag, release, item_id):
    with pytest.raises(BNetRegionNotFoundError):
        item_media(region_tag, item_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_item_search(region_tag, release):
    fields = {
        'name.en_US': 'Thunderfury',
        'orderby': 'id',
        '_page': 1
    }
    data = item_search(region_tag, fields, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/search/item')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'
    for k, v in fields.items():
        assert k in data[1]
        assert data[1][k] == v


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_item_search_invalid_region(region_tag, release):
    fields = {
        'name.en_US': 'Thunderfury',
        'orderby': 'id',
        '_page': 1
    }
    with pytest.raises(BNetRegionNotFoundError):
        item_search(region_tag, fields, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_journal_expansion_default_index(region_tag, release):
    data = journal_expansion(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/journal-expansion/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_journal_expansion_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        journal_expansion(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, expansion_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 68, '68'))))
def test_journal_expansion_id(region_tag, release, expansion_id):
    data = journal_expansion(region_tag, expansion_id=expansion_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/journal-expansion/{expansion_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, expansion_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_journal_expansion_id_invalid_region(region_tag, release, expansion_id):
    with pytest.raises(BNetRegionNotFoundError):
        journal_expansion(region_tag, expansion_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_journal_encounter_default_index(region_tag, release):
    data = journal_encounter(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/journal-encounter/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_journal_encounter_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        journal_encounter(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, encounter_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 89, '89'))))
def test_journal_encounter_id(region_tag, release, encounter_id):
    data = journal_encounter(region_tag, encounter_id=encounter_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/journal-encounter/{encounter_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, encounter_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_journal_encounter_id_invalid_region(region_tag, release, encounter_id):
    with pytest.raises(BNetRegionNotFoundError):
        journal_encounter(region_tag, encounter_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_journal_encounter_search(region_tag, release):
    fields = {
        'instance.name.en_US': 'Deadmines',
        'orderby': 'id:desc',
        '_page': 1
    }

    data = journal_encounter_search(region_tag, fields, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/search/journal-encounter')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'
    for k, v in fields.items():
        assert k in data[1]
        assert data[1][k] == v


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_journal_encounter_search_invalid_region(region_tag, release):
    fields = {
        'instance.name.en_US': 'Deadmines',
        'orderby': 'id:desc',
        '_page': 1
    }
    with pytest.raises(BNetRegionNotFoundError):
        journal_encounter_search(region_tag, fields, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_journal_instance_default_index(region_tag, release):
    data = journal_instance(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/journal-instance/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_journal_instance_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        journal_instance(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, instance_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 63, '63'))))
def test_journal_instance_id(region_tag, release, instance_id):
    data = journal_instance(region_tag, instance_id=instance_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/journal-instance/{instance_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, instance_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_journal_instance_id_invalid_region(region_tag, release, instance_id):
    with pytest.raises(BNetRegionNotFoundError):
        journal_instance(region_tag, instance_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, journal_instance_id',
                         list(product(VALID_REGIONS, Release.all(), (6, '6'))))
def test_journal_instance_media(region_tag, release, journal_instance_id):
    data = journal_instance_media(region_tag, instance_id=journal_instance_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/media/journal-instance/{journal_instance_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, instance_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_journal_instance_media_id_invalid_region(region_tag, release, instance_id):
    with pytest.raises(BNetRegionNotFoundError):
        journal_instance_media(region_tag, instance_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_media_search(region_tag, release):
    fields = {
        'tags': 'item',
        'orderby': 'id',
        '_page': 1
    }
    data = media_search(region_tag, fields, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/search/media')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'
    for k, v in fields.items():
        assert k in data[1]
        assert data[1][k] == v


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_media_search_invalid_region(region_tag, release):
    fields = {
        'tags': 'item',
        'orderby': 'id',
        '_page': 1
    }
    with pytest.raises(BNetRegionNotFoundError):
        media_search(region_tag, fields, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_modified_crafting_default_index(region_tag, release):
    data = modified_crafting(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/modified-crafting')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_modified_crafting_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        modified_crafting(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_modified_crafting_category_default_index(region_tag, release):
    data = modified_crafting_category(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/modified-crafting/category/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_modified_crafting_category_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        modified_crafting_category(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, category_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 6, '6'))))
def test_modified_crafting_category_id(region_tag, release, category_id):
    data = modified_crafting_category(region_tag, category_id=category_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/modified-crafting/category/{category_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, category_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_modified_crafting_category_id_invalid_region(region_tag, release, category_id):
    with pytest.raises(BNetRegionNotFoundError):
        modified_crafting_category(region_tag, category_id=category_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_modified_crafting_reagent_slot_type_default_index(region_tag, release):
    data = modified_crafting_reagent_slot_type(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/modified-crafting/reagent-slot-type/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_modified_crafting_reagent_slot_type_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        modified_crafting_reagent_slot_type(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, reagent_slot_type_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_modified_crafting_reagent_slot_type_id(region_tag, release, reagent_slot_type_id):
    data = modified_crafting_reagent_slot_type(region_tag, slot_type_id=reagent_slot_type_id, release=release,
                                               locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/modified-crafting/reagent-slot-type/{reagent_slot_type_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, reagent_slot_type_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_modified_crafting_reagent_slot_type_id_invalid_region(region_tag, release, reagent_slot_type_id):
    with pytest.raises(BNetRegionNotFoundError):
        modified_crafting_reagent_slot_type(region_tag, slot_type_id=reagent_slot_type_id, release=release,
                                            locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_mount_default_index(region_tag, release):
    data = mount(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/mount/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_mount_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        mount(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, mount_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_mount_id(region_tag, release, mount_id):
    data = mount(region_tag, mount_id=mount_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/mount/{mount_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, mount_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_mount_id_invalid_region(region_tag, release, mount_id):
    with pytest.raises(BNetRegionNotFoundError):
        mount(region_tag, mount_id=mount_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_mount_search(region_tag, release):
    fields = {
        'name.en_US': 'Turtle',
        'orderby': 'id',
        '_page': 1
    }
    data = mount_search(region_tag, fields, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/search/mount')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'
    for k, v in fields.items():
        assert k in data[1]
        assert data[1][k] == v


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_mount_search_invalid_region(region_tag, release):
    fields = {
        'name.en_US': 'Turtle',
        'orderby': 'id',
        '_page': 1
    }
    with pytest.raises(BNetRegionNotFoundError):
        mount_search(region_tag, fields, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_mythic_keystone_affix_default_index(region_tag, release):
    data = mythic_keystone_affix(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/keystone-affix/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_mythic_keystone_affix_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        mythic_keystone_affix(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, mythic_keystone_affix_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_mythic_keystone_affix_id(region_tag, release, mythic_keystone_affix_id):
    data = mythic_keystone_affix(region_tag, affix_id=mythic_keystone_affix_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/keystone-affix/{mythic_keystone_affix_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, mythic_keystone_affix_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_mythic_keystone_affix_id_invalid_region(region_tag, release, mythic_keystone_affix_id):
    with pytest.raises(BNetRegionNotFoundError):
        mythic_keystone_affix(region_tag, affix_id=mythic_keystone_affix_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, mythic_keystone_affix_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_mythic_keystone_affix_media(region_tag, release, mythic_keystone_affix_id):
    data = mythic_keystone_affix_media(region_tag, mythic_keystone_affix_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/media/keystone-affix/{mythic_keystone_affix_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, mythic_keystone_affix_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_mythic_keystone_affix_media_id_invalid_region(region_tag, release, mythic_keystone_affix_id):
    with pytest.raises(BNetRegionNotFoundError):
        mythic_keystone_affix(region_tag, affix_id=mythic_keystone_affix_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_mythic_keystone_dungeon_default_index(region_tag, release):
    data = mythic_keystone_dungeon(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/mythic-keystone/dungeon/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_mythic_keystone_dungeon_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        mythic_keystone_dungeon(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, mythic_keystone_dungeon_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_mythic_keystone_dungeon_id(region_tag, release, mythic_keystone_dungeon_id):
    data = mythic_keystone_dungeon(region_tag, dungeon_id=mythic_keystone_dungeon_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/mythic-keystone/dungeon/{mythic_keystone_dungeon_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, mythic_keystone_dungeon_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_mythic_keystone_dungeon_id_invalid_region(region_tag, release, mythic_keystone_dungeon_id):
    with pytest.raises(BNetRegionNotFoundError):
        mythic_keystone_dungeon(region_tag, dungeon_id=mythic_keystone_dungeon_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_mythic_keystone_index(region_tag, release):
    data = mythic_keystone_index(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/mythic-keystone/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_mythic_keystone_index_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        mythic_keystone_index(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_mythic_keystone_period_default_index(region_tag, release):
    data = mythic_keystone_period(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/mythic-keystone/period/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_mythic_keystone_period_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        mythic_keystone_period(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, mythic_keystone_period_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_mythic_keystone_period_id(region_tag, release, mythic_keystone_period_id):
    data = mythic_keystone_period(region_tag, period_id=mythic_keystone_period_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/mythic-keystone/period/{mythic_keystone_period_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, mythic_keystone_period_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_mythic_keystone_period_id_invalid_region(region_tag, release, mythic_keystone_period_id):
    with pytest.raises(BNetRegionNotFoundError):
        mythic_keystone_period(region_tag, period_id=mythic_keystone_period_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_mythic_keystone_season_default_index(region_tag, release):
    data = mythic_keystone_season(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/mythic-keystone/season/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_mythic_keystone_season_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        mythic_keystone_season(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, mythic_keystone_season_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_mythic_keystone_season_id(region_tag, release, mythic_keystone_season_id):
    data = mythic_keystone_season(region_tag, season_id=mythic_keystone_season_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/mythic-keystone/season/{mythic_keystone_season_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, mythic_keystone_season_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_mythic_keystone_season_id_invalid_region(region_tag, release, mythic_keystone_season_id):
    with pytest.raises(BNetRegionNotFoundError):
        mythic_keystone_season(region_tag, season_id=mythic_keystone_season_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, cr_id',
                         list(product(VALID_REGIONS, Release.all(), (4, '4', 5, '5', 4372, '4372', 5064, '5064'))))
def test_mythic_keystone_leaderboard_default_index(region_tag, release, cr_id):
    data = mythic_keystone_leaderboard(region_tag, cr_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/connected-realm/{cr_id}/mythic-leaderboard/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_mythic_keystone_leaderboard_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        mythic_keystone_leaderboard(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, cr_id, dungeon_id, period_id,',
                         list(product(VALID_REGIONS, Release.all(), (4, '4', 5, '5', 4372, '4372', 5064, '5064'),
                                      (1, '1', 1234, '1234'), (1, 2, 3, 4))))
def test_mythic_keystone_leaderboard_id(region_tag, release, cr_id, dungeon_id, period_id):
    data = mythic_keystone_leaderboard(region_tag, cr_id, dungeon_id=dungeon_id, period_id=period_id, release=release,
                                       locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f"wow/connected-realm/{cr_id}/mythic-leaderboard/{dungeon_id}/period/{period_id}")
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, mythic_keystone_leaderboard_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_mythic_keystone_leaderboard_id_invalid_region(region_tag, release, mythic_keystone_leaderboard_id):
    with pytest.raises(BNetRegionNotFoundError):
        mythic_keystone_leaderboard(region_tag, leaderboard_id=mythic_keystone_leaderboard_id, release=release,
                                    locale='enus')


@pytest.mark.parametrize('region_tag, release, raid_name, faction',
                         list(product(VALID_REGIONS, Release.all(),
                                      ('castle nathria', 'sanctum of domination', 'sepulcher of the first ones'),
                                      ('alliance', 'horde'))))
def test_mythic_raid_leaderboard_id(region_tag, release, raid_name, faction):
    data = mythic_raid_leaderboard(region_tag, raid_name, faction, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/leaderboard/hall-of-fame/{utils.slugify(raid_name)}/{faction}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, raid_name, faction',
                         list(product(INVALID_REGIONS, Release.all(),
                                      ('castle nathria', 'sanctum of domination', 'sepulcher of the first ones'),
                                      ('alliance', 'horde'))))
def test_mythic_raid_leaderboard_id_invalid_region(region_tag, release, raid_name, faction):
    with pytest.raises(BNetRegionNotFoundError):
        mythic_raid_leaderboard(region_tag, raid_name, faction, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_pet_default_index(region_tag, release):
    data = pet(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/pet/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_pet_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        pet(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, pet_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_pet_id(region_tag, release, pet_id):
    data = pet(region_tag, pet_id=pet_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/pet/{pet_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, pet_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_pet_id_invalid_region(region_tag, release, pet_id):
    with pytest.raises(BNetRegionNotFoundError):
        pet(region_tag, pet_id=pet_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, pet_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_pet_media(region_tag, release, pet_id):
    data = pet_media(region_tag, pet_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/media/pet/{pet_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, pet_id',
                         list(product(INVALID_REGIONS, Release.all(), (1019, '19019'))))
def test_pet_media_id_invalid_region(region_tag, release, pet_id):
    with pytest.raises(BNetRegionNotFoundError):
        pet_media(region_tag, pet_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_pet_ability_default_index(region_tag, release):
    data = pet_ability(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/pet-ability/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_pet_ability_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        pet_ability(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, pet_ability_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_pet_ability_id(region_tag, release, pet_ability_id):
    data = pet_ability(region_tag, pet_ability_id=pet_ability_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/pet-ability/{pet_ability_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, pet_ability_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_pet_ability_id_invalid_region(region_tag, release, pet_ability_id):
    with pytest.raises(BNetRegionNotFoundError):
        pet_ability(region_tag, pet_ability_id=pet_ability_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, pet_ability_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_pet_ability_media(region_tag, release, pet_ability_id):
    data = pet_ability_media(region_tag, pet_ability_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/media/pet-ability/{pet_ability_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, pet_ability_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_pet_ability_media_id_invalid_region(region_tag, release, pet_ability_id):
    with pytest.raises(BNetRegionNotFoundError):
        pet_ability_media(region_tag, pet_ability_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_playable_class_default_index(region_tag, release):
    data = playable_class(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/playable-class/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_playable_class_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        playable_class(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, playable_class_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_playable_class_id(region_tag, release, playable_class_id):
    data = playable_class(region_tag, class_id=playable_class_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/playable-class/{playable_class_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, class_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_playable_class_id_invalid_region(region_tag, release, class_id):
    with pytest.raises(BNetRegionNotFoundError):
        playable_class(region_tag, class_id=class_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, playable_class_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_playable_class_media(region_tag, release, playable_class_id):
    data = playable_class_media(region_tag, playable_class_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/media/playable-class/{playable_class_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, class_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_playable_class_media_id_invalid_region(region_tag, release, class_id):
    with pytest.raises(BNetRegionNotFoundError):
        playable_class_media(region_tag, class_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, class_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_pvp_talent_slots_id(region_tag, release, class_id):
    data = pvp_talent_slots(region_tag, class_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/playable-class/{class_id}/pvp-talent-slots')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, class_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_pvp_talent_slots_id_invalid_region(region_tag, release, class_id):
    with pytest.raises(BNetRegionNotFoundError):
        pvp_talent_slots(region_tag, class_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_playable_race_default_index(region_tag, release):
    data = playable_race(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/playable-race/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_playable_race_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        playable_race(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, playable_race_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_playable_race_id(region_tag, release, playable_race_id):
    data = playable_race(region_tag, race_id=playable_race_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/playable-race/{playable_race_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, race_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_playable_race_id_invalid_region(region_tag, release, race_id):
    with pytest.raises(BNetRegionNotFoundError):
        playable_race(region_tag, race_id=race_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_playable_spec_default_index(region_tag, release):
    data = playable_spec(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/playable-specialization/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_playable_spec_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        playable_spec(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, playable_spec_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_playable_spec_id(region_tag, release, playable_spec_id):
    data = playable_spec(region_tag, spec_id=playable_spec_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/playable-specialization/{playable_spec_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, spec_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_playable_spec_id_invalid_region(region_tag, release, spec_id):
    with pytest.raises(BNetRegionNotFoundError):
        playable_spec(region_tag, spec_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, playable_spec_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_playable_spec_media(region_tag, release, playable_spec_id):
    data = playable_spec_media(region_tag, playable_spec_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/media/playable-specialization/{playable_spec_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, spec_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_playable_spec_media_id_invalid_region(region_tag, release, spec_id):
    with pytest.raises(BNetRegionNotFoundError):
        playable_spec_media(region_tag, spec_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_power_type_default_index(region_tag, release):
    data = power_type(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/power-type/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_power_type_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        power_type(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, power_type_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_power_type_id(region_tag, release, power_type_id):
    data = power_type(region_tag, power_id=power_type_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/power-type/{power_type_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, type_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_power_type_id_invalid_region(region_tag, release, type_id):
    with pytest.raises(BNetRegionNotFoundError):
        power_type(region_tag, type_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_profession_default_index(region_tag, release):
    data = profession(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/profession/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_profession_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        profession(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, profession_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_profession_id(region_tag, release, profession_id):
    data = profession(region_tag, profession_id=profession_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/profession/{profession_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, profession_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_profession_id_invalid_region(region_tag, release, profession_id):
    with pytest.raises(BNetRegionNotFoundError):
        profession(region_tag, profession_id=profession_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, profession_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_profession_media(region_tag, release, profession_id):
    data = profession_media(region_tag, profession_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/media/profession/{profession_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, profession_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_profession_media_id_invalid_region(region_tag, release, profession_id):
    with pytest.raises(BNetRegionNotFoundError):
        profession_media(region_tag, profession_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, profession_id, tier_id',
                         list(product(VALID_REGIONS, Release.all(), (1, '1', 1234, '1234'), (1, '1', 5, '10'))))
def test_profession_skill_tier_skill_tier_id(region_tag, release, profession_id, tier_id):
    data = profession_skill_tier(region_tag, profession_id, tier_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/profession/{profession_id}/skill-tier/{tier_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, profession_id, tier_id',
                         list(product(INVALID_REGIONS, Release.all(), (1, '1', 1234, '1234'), (1, '1', 5, '10'))))
def test_profession_skill_tier_id_invalid_region(region_tag, release, profession_id, tier_id):
    with pytest.raises(BNetRegionNotFoundError):
        profession_skill_tier(region_tag, profession_id, tier_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, recipe_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_recipe_id(region_tag, release, recipe_id):
    data = recipe(region_tag, recipe_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/recipe/{recipe_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, recipe_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_recipe_id_invalid_region(region_tag, release, recipe_id):
    with pytest.raises(BNetRegionNotFoundError):
        recipe(region_tag, recipe_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, recipe_id',
                         list(product(VALID_REGIONS, Release.all(), (1, '1', 1234, '1234'))))
def test_recipe_media(region_tag, release, recipe_id):
    data = recipe_media(region_tag, recipe_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/media/recipe/{recipe_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, recipe_id',
                         list(product(INVALID_REGIONS, Release.all(), (1, '1', 1234, '1234'))))
def test_recipe_media_id_invalid_region(region_tag, release, recipe_id):
    with pytest.raises(BNetRegionNotFoundError):
        recipe_media(region_tag, recipe_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_pvp_season_default_index(region_tag, release):
    data = pvp_season(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/pvp-season/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_pvp_season_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        pvp_season(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, pvp_season_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_pvp_season_id(region_tag, release, pvp_season_id):
    data = pvp_season(region_tag, season_id=pvp_season_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/pvp-season/{pvp_season_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, pvp_season_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_pvp_season_id_invalid_region(region_tag, release, pvp_season_id):
    with pytest.raises(BNetRegionNotFoundError):
        pvp_season(region_tag, season_id=pvp_season_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_pvp_region_default_index(region_tag, release):
    data = pvp_regions(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/pvp-region/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_pvp_regions_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        pvp_regions(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, region_id',
                         list(product(VALID_REGIONS, Release.all(), (1, '1', 1234, '1234'))))
def test_pvp_regional_season_default_index(region_tag, release, region_id):
    data = pvp_regional_season(region_tag, region_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/pvp-region/{region_id}/pvp-season/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, region_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_pvp_regional_season_default_index_invalid_region(region_tag, release, region_id):
    with pytest.raises(BNetRegionNotFoundError):
        pvp_regional_season(region_tag, region_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, region_id, season_id',
                         list(product(VALID_REGIONS, Release.all(), (1, '1', 1234, '1234'), ('index', 1, 2, 34, 789))))
def test_pvp_regional_season_id(region_tag, release, region_id, season_id):
    data = pvp_regional_season(region_tag, region_id, pvp_season_id=season_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/pvp-region/{region_id}/pvp-season/{season_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, region_id, season_id',
                         list(product(INVALID_REGIONS, Release.all(), (1, 3, 5), ('index', 1019, '19019'))))
def test_pvp_regional_season_id_invalid_region(region_tag, release, region_id, season_id):
    with pytest.raises(BNetRegionNotFoundError):
        pvp_regional_season(region_tag, region_id, pvp_season_id=season_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, region_id, season_id',
                         list(product(VALID_REGIONS, Release.all(),  (1, 2, 3, 4), (11, 22, 33, 44))))
def test_pvp_leaderboard_default_index(region_tag, release, region_id, season_id):
    data = pvp_leaderboard(region_tag, region_id, season_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/pvp-region/{region_id}/pvp-season/{season_id}/pvp-leaderboard/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, region_id, season_id',
                         list(product(INVALID_REGIONS, Release.all(), (1, 2, 3, 4), (11, 22, 33, 44))))
def test_pvp_leaderboard_default_index_invalid_region(region_tag, release, region_id, season_id):
    with pytest.raises(BNetRegionNotFoundError):
        pvp_leaderboard(region_tag, region_id, season_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, region_id, season_id, bracket',
                         list(product(VALID_REGIONS, Release.all(), (1, 2, 3, 4), (11, 22, 33, 44),
                                      ('index', '2v2', '3v3', '5v5', 'rbg'))))
def test_pvp_leaderboard_id(region_tag, release, region_id, season_id, bracket):
    data = pvp_leaderboard(region_tag, region_id, season_id, pvp_bracket=bracket, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/pvp-region/{region_id}/pvp-season/{season_id}/pvp-leaderboard/{bracket}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, region_id, season_id, bracket',
                         list(product(INVALID_REGIONS, Release.all(), (1, 2, 3, 4), ("index", 11, 22, 33, 44),
                                      ('index', '2v2', '3v3', '5v5', 'rbg'))))
def test_pvp_leaderboard_id_invalid_region(region_tag, release, region_id, season_id, bracket):
    with pytest.raises(BNetRegionNotFoundError):
        pvp_leaderboard(region_tag, region_id, season_id, pvp_bracket=bracket, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, region_id, season_id',
                         list(product(VALID_REGIONS, Release.all(), (1, 2, 3, 4), (23, 45, 67, 108))))
def test_pvp_reward_default_index(region_tag, release, region_id, season_id):
    data = pvp_rewards_index(region_tag, region_id, season_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/pvp-region/{region_id}/pvp-season/{season_id}/pvp-reward/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, region_id, season_id',
                         list(product(INVALID_REGIONS, Release.all(), (1, 3, 5), (23, 45, 67, 108))))
def test_pvp_rewards_index_invalid_region(region_tag, release, region_id, season_id):
    with pytest.raises(BNetRegionNotFoundError):
        pvp_rewards_index(region_tag, region_id, pvp_season_id=season_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_pvp_tier_default_index(region_tag, release):
    data = pvp_tier(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/pvp-tier/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_pvp_tier_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        pvp_tier(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, pvp_tier_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_pvp_tier_id(region_tag, release, pvp_tier_id):
    data = pvp_tier(region_tag, tier_id=pvp_tier_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/pvp-tier/{pvp_tier_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, tier_id',
                         list(product(INVALID_REGIONS, Release.all(), (23, 45, 67, 108))))
def test_pvp_tier_id_invalid_region(region_tag, release, tier_id):
    with pytest.raises(BNetRegionNotFoundError):
        pvp_tier(region_tag, tier_id=tier_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, pvp_tier_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_pvp_tier_media(region_tag, release, pvp_tier_id):
    data = pvp_tier_media(region_tag, pvp_tier_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/media/pvp-tier/{pvp_tier_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, tier_id',
                         list(product(INVALID_REGIONS, Release.all(), (23, 45, 67, 108))))
def test_pvp_tier_media_id_invalid_region(region_tag, release, tier_id):
    with pytest.raises(BNetRegionNotFoundError):
        pvp_tier_media(region_tag, tier_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_quest_default_index(region_tag, release):
    data = quest(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/quest/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_quest_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        quest(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, quest_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_quest_id(region_tag, release, quest_id):
    data = quest(region_tag, quest_id=quest_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/quest/{quest_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, quest_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1019, '19019'))))
def test_quest_id_invalid_region(region_tag, release, quest_id):
    with pytest.raises(BNetRegionNotFoundError):
        quest(region_tag, quest_id=quest_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_quest_category_default_index(region_tag, release):
    data = quest_category(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/quest/category/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_quest_category_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        quest_category(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, quest_category_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_quest_category_id(region_tag, release, quest_category_id):
    data = quest_category(region_tag, quest_category_id=quest_category_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/quest/category/{quest_category_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, quest_category_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_quest_category_id_invalid_region(region_tag, release, quest_category_id):
    with pytest.raises(BNetRegionNotFoundError):
        quest_category(region_tag, quest_category_id=quest_category_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_quest_area_default_index(region_tag, release):
    data = quest_area(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/quest/area/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_quest_area_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        quest_area(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, quest_area_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_quest_area_id(region_tag, release, quest_area_id):
    data = quest_area(region_tag, quest_area_id=quest_area_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/quest/area/{quest_area_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, quest_area_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_quest_area_id_invalid_region(region_tag, release, quest_area_id):
    with pytest.raises(BNetRegionNotFoundError):
        quest_area(region_tag, quest_area_id=quest_area_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_quest_type_default_index(region_tag, release):
    data = quest_type(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/quest/type/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_quest_type_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        quest_type(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, quest_type_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_quest_type_id(region_tag, release, quest_type_id):
    data = quest_type(region_tag, quest_type_id=quest_type_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/quest/type/{quest_type_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, quest_type_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_quest_type_id_invalid_region(region_tag, release, quest_type_id):
    with pytest.raises(BNetRegionNotFoundError):
        quest_type(region_tag, quest_type_id=quest_type_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_realm_default_index(region_tag, release):
    data = realm(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/realm/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_realm_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        realm(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, realm_slug',
                         list(product(VALID_REGIONS, Release.all(),
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'))))
def test_realm_id(region_tag, release, realm_slug):
    data = realm(region_tag, realm_slug=realm_slug, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/realm/{utils.slugify(realm_slug)}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, realm_slug',
                         list(product(INVALID_REGIONS, Release.all(),
                                      ('index', 1, '1', 1234, '1234', 'Area 52', 'Baelgun', 'Zul\'jin'))))
def test_realm_id_invalid_region(region_tag, release, realm_slug):
    with pytest.raises(BNetRegionNotFoundError):
        realm(region_tag, realm_slug=realm_slug, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_realm_search(region_tag, release):
    fields = {
        'name.en_US': 'Baelgun',
        'orderby': 'name',
        '_page': 1
    }

    data = realm_search(region_tag, fields, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/search/realm')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'
    if release.lower() == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release.lower()}-{region_tag.lower()}'
    for k, v in fields.items():
        assert k in data[1]
        assert data[1][k] == v


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_realm_search_invalid_region(region_tag, release):
    fields = {
        'name.en_US': 'Baelgun',
        'orderby': 'name',
        '_page': 1
    }
    with pytest.raises(BNetRegionNotFoundError):
        realm_search(region_tag, fields, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_region_default_index(region_tag, release):
    data = region(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/region/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_region_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        region(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, region_req',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_region_id(region_tag, release, region_req):
    data = region(region_tag, region_req=region_req, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/region/{utils.slugify(region_req)}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'dynamic-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'dynamic-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, region_req',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_region_id_invalid_region(region_tag, release, region_req):
    with pytest.raises(BNetRegionNotFoundError):
        region(region_tag, region_req=region_req, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_reputation_faction_default_index(region_tag, release):
    data = reputation_faction(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/reputation-faction/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_reputation_faction_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        reputation_faction(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, faction_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_reputation_faction_id(region_tag, release, faction_id):
    data = reputation_faction(region_tag, faction_id=faction_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/reputation-faction/{utils.slugify(faction_id)}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, faction_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_reputation_faction_id_invalid_region(region_tag, release, faction_id):
    with pytest.raises(BNetRegionNotFoundError):
        reputation_faction(region_tag, faction_id=faction_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_reputation_tier_default_index(region_tag, release):
    data = reputation_tier(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/reputation-tiers/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_reputation_tier_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        reputation_tier(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, reputation_tier_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_reputation_tier_id(region_tag, release, reputation_tier_id):
    data = reputation_tier(region_tag, tier_id=reputation_tier_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/reputation-tiers/{reputation_tier_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, tier_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_reputation_tier_id_invalid_region(region_tag, release, tier_id):
    with pytest.raises(BNetRegionNotFoundError):
        reputation_tier(region_tag, tier_id=tier_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, spell_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_spell_id(region_tag, release, spell_id):
    data = spell(region_tag, spell_id=spell_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/spell/{spell_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, spell_id',
                         list(product(INVALID_REGIONS, Release.all(), (1, '1', 1234, '1234'))))
def test_spell_id_invalid_region(region_tag, release, spell_id):
    with pytest.raises(BNetRegionNotFoundError):
        spell(region_tag, spell_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, spell_id',
                         list(product(VALID_REGIONS, Release.all(), (1, '1', 1234, '1234'))))
def test_spell_media(region_tag, release, spell_id):
    data = spell_media(region_tag, spell_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/media/spell/{spell_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, spell_id',
                         list(product(INVALID_REGIONS, Release.all(), (1019, '19019'))))
def test_spell_media_id_invalid_region(region_tag, release, spell_id):
    with pytest.raises(BNetRegionNotFoundError):
        spell_media(region_tag, spell_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_spell_search(region_tag, release):
    fields = {
        'name.en_US': 'Holy Shield',
        'orderby': 'id',
        '_page': 1
    }
    data = spell_search(region_tag, fields, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/search/spell')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'
    if release.lower() == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release.lower()}-{region_tag.lower()}'
    for k, v in fields.items():
        assert k in data[1]
        assert data[1][k] == v


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_spell_search_invalid_region(region_tag, release):
    fields = {
        'name.en_US': 'Holy Shield',
        'orderby': 'id',
        '_page': 1
    }
    with pytest.raises(BNetRegionNotFoundError):
        spell_search(region_tag, fields, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_talent_default_index(region_tag, release):
    data = talent(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/talent/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_talent_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        talent(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, talent_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_talent_id(region_tag, release, talent_id):
    data = talent(region_tag, talent_id=talent_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/talent/{talent_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, talent_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_talent_id_invalid_region(region_tag, release, talent_id):
    with pytest.raises(BNetRegionNotFoundError):
        talent(region_tag, talent_id=talent_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_pvp_talent_default_index(region_tag, release):
    data = pvp_talent(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/pvp-talent/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_pvp_talent_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        pvp_talent(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, pvp_talent_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_pvp_talent_id(region_tag, release, pvp_talent_id):
    data = pvp_talent(region_tag, pvp_talent_id=pvp_talent_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/pvp-talent/{pvp_talent_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, pvp_talent_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_pvp_talent_id_invalid_region(region_tag, release, pvp_talent_id):
    with pytest.raises(BNetRegionNotFoundError):
        pvp_talent(region_tag, pvp_talent_id=pvp_talent_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_tech_talent_tree_default_index(region_tag, release):
    data = tech_talent_tree(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/tech-talent-tree/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_tech_talent_tree_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        tech_talent_tree(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, tech_talent_tree_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_tech_talent_tree_id(region_tag, release, tech_talent_tree_id):
    data = tech_talent_tree(region_tag, tree_id=tech_talent_tree_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/tech-talent-tree/{tech_talent_tree_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, tech_talent_tree_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_tech_talent_tree_id_invalid_region(region_tag, release, tech_talent_tree_id):
    with pytest.raises(BNetRegionNotFoundError):
        tech_talent_tree(region_tag, tree_id=tech_talent_tree_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_tech_talent_default_index(region_tag, release):
    data = tech_talent(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/tech-talent/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_tech_talent_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        tech_talent(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, tech_talent_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_tech_talent_id(region_tag, release, tech_talent_id):
    data = tech_talent(region_tag, talent_id=tech_talent_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/tech-talent/{tech_talent_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, tech_talent_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_tech_talent_id_invalid_region(region_tag, release, tech_talent_id):
    with pytest.raises(BNetRegionNotFoundError):
        tech_talent(region_tag, tree_id=tech_talent_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, tech_talent_id',
                         list(product(VALID_REGIONS, Release.all(), (1, '1', 1234, '1234'))))
def test_tech_talent_media(region_tag, release, tech_talent_id):
    data = tech_talent_media(region_tag, tech_talent_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/media/tech-talent/{tech_talent_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, tech_talent_id',
                         list(product(INVALID_REGIONS, Release.all(), (1019, '19019'))))
def test_tech_talent_media_id_invalid_region(region_tag, release, tech_talent_id):
    with pytest.raises(BNetRegionNotFoundError):
        tech_talent_media(region_tag, tech_talent_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_title_default_index(region_tag, release):
    data = title(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/title/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_title_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        title(region_tag, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release, title_id',
                         list(product(VALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_title_id(region_tag, release, title_id):
    data = title(region_tag, title_id=title_id, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith(f'wow/title/{title_id}')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release, title_id',
                         list(product(INVALID_REGIONS, Release.all(), ('index', 1, '1', 1234, '1234'))))
def test_title_id_invalid_region(region_tag, release, title_id):
    with pytest.raises(BNetRegionNotFoundError):
        title(region_tag, title_id=title_id, release=release, locale='enus')


@pytest.mark.parametrize('region_tag, release',
                         list(product(VALID_REGIONS, Release.all())))
def test_wow_token_default_index(region_tag, release):
    data = wow_token_index(region_tag, release=release, locale='enus')
    assert isinstance(data, tuple)
    assert data[0].endswith('wow/token/index')
    assert isinstance(data[1], dict)
    assert 'namespace' in data[1]
    assert 'locale' in data[1]
    if release == 'retail':
        assert data[1]['namespace'] == f'static-{region_tag.lower()}'
    else:
        assert data[1]['namespace'] == f'static-{release}-{region_tag.lower()}'
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, release',
                         list(product(INVALID_REGIONS, Release.all())))
def test_wow_token_index_default_index_invalid_region(region_tag, release):
    with pytest.raises(BNetRegionNotFoundError):
        wow_token_index(region_tag, release=release, locale='enus')
