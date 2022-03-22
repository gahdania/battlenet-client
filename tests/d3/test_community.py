import pytest
from itertools import product
from urllib.parse import quote as urlquote

from battlenet_client.constants import VALID_REGIONS
from battlenet_client.exceptions import BNetRegionNotFoundError, BNetValueError
from battlenet_client.utils import slugify
from battlenet_client.d3.community import act, artisan, recipe, follower, character_class, api_skill
from battlenet_client.d3.community import item_type, item, api_account, api_hero
from ..constants import INVALID_REGIONS


@pytest.mark.parametrize('region_tag', VALID_REGIONS)
def test_act_index(region_tag):
    data = act(region_tag, locale='en_US')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith('d3/data/act')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag', INVALID_REGIONS)
def test_act_index_invalid_region(region_tag):
    with pytest.raises(BNetRegionNotFoundError):
        act(region_tag, locale='en_US')


@pytest.mark.parametrize('region_tag, act_id', list(product(VALID_REGIONS, (1, '1', 5, '5', 99, '99', 'index'))))
def test_act_id_int(region_tag, act_id):
    data = act(region_tag, act_id=act_id, locale='en_US')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'd3/data/act/{act_id}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, act_id', list(product(INVALID_REGIONS, (1, '1', 5, '5', 99, '99', 'index'))))
def test_act_id_invalid_region(region_tag, act_id):
    with pytest.raises(BNetRegionNotFoundError):
        act(region_tag, act_id=act_id, locale='en_US')


@pytest.mark.parametrize('region_tag, artisan_name', list(product(VALID_REGIONS, ('Blacksmith', 'Jeweler', 'Mystic'))))
def test_artisan(region_tag, artisan_name):
    data = artisan(region_tag, artisan_slug=artisan_name, locale="enus")
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'd3/data/artisan/{slugify(artisan_name)}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, artisan_name', list(product(INVALID_REGIONS,
                                                                  ('Blacksmith', 'Jeweler', 'Mystic'))))
def test_artisan_invalid_region(region_tag, artisan_name):
    with pytest.raises(BNetRegionNotFoundError):
        artisan(region_tag, artisan_slug=artisan_name, locale="enus")


@pytest.mark.parametrize('region_tag, artisan_name, recipe_name',
                         list(product(VALID_REGIONS, ('Blacksmith', 'Jeweler', 'Mystic'),
                                      ('Apprentice Boots', 'Apprentice Flamberge', 'Journeyman Chain Boots'))))
def test_recipe(region_tag, artisan_name, recipe_name):
    data = recipe(region_tag, artisan_slug=artisan_name, recipe_slug=recipe_name, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'd3/data/artisan/{slugify(artisan_name)}/recipe/{slugify(recipe_name)}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, artisan_name, recipe_name',
                         list(product(INVALID_REGIONS, ('Blacksmith', 'Jeweler', 'Mystic'),
                                      ('Apprentice Boots', 'Apprentice Flamberge', 'Journeyman Chain Boots'))))
def test_recipe_invalid_region(region_tag, artisan_name, recipe_name):
    with pytest.raises(BNetRegionNotFoundError):
        recipe(region_tag, artisan_slug=artisan_name, recipe_slug=recipe_name, locale='enus')


@pytest.mark.parametrize('region_tag, class_name', list(product(VALID_REGIONS,
                                                        ('Barbarian', 'Crusader', 'Demon Hunter', 'Monk',
                                                         'Necromancer', 'Witch Docter', 'Wizard'))))
def test_character_class_valid_region(region_tag, class_name):
    data = character_class(region_tag, class_slug=class_name, locale="enus")
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'd3/data/hero/{slugify(class_name)}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, class_name',
                         list(product(INVALID_REGIONS, ('Barbarian', 'Crusader', 'Demon Hunter', 'Monk',
                                                        'Necromancer', 'Witch Docter', 'Wizard'))))
def test_character_class_invalid_region(region_tag, class_name):
    with pytest.raises(BNetRegionNotFoundError):
        character_class(region_tag, class_slug=class_name, locale="enus")


@pytest.mark.parametrize('region_tag, class_name, skill_name', list(product(VALID_REGIONS,
                                                                    ('Barbarian', 'Crusader', 'Demon Hunter', 'Monk',
                                                                     'Necromancer', 'Witch Docter', 'Wizard'),
                                                                    ('Bash', 'Punish', 'Shield Bash',
                                                                     'Hungering Arrow'))))
def test_api_skill_valid_region(region_tag, class_name, skill_name):
    data = api_skill(region_tag, class_slug=class_name, skill_slug=skill_name, locale="enus")
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'd3/data/hero/{slugify(class_name)}/skill/{slugify(skill_name)}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, class_name, skill_name', list(product(INVALID_REGIONS,
                                                                    ('Barbarian', 'Crusader', 'Demon Hunter', 'Monk',
                                                                     'Necromancer', 'Witch Docter', 'Wizard'),
                                                                    ('Bash', 'Punish', 'Shield Bash',
                                                                     'Hungering Arrow'))))
def test_api_skill_invalid_region(region_tag, class_name, skill_name):
    with pytest.raises(BNetRegionNotFoundError):
        api_skill(region_tag, class_slug=class_name, skill_slug=skill_name, locale="enus")


@pytest.mark.parametrize('region_tag, follower_name', list(product(VALID_REGIONS,
                                                                   ('Enchantress', 'Templar', 'Scoundrel'))))
def test_follower_valid_region(region_tag, follower_name):
    data = follower(region_tag, follower_slug=follower_name, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'd3/data/follower/{slugify(follower_name)}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, follower_name', list(product(INVALID_REGIONS,
                                                                   ('Enchantress', 'Templar', 'Scoundrel'))))
def test_follower_invalid_region(region_tag, follower_name):
    with pytest.raises(BNetRegionNotFoundError):
        follower(region_tag, follower_slug=follower_name, locale='enus')


@pytest.mark.parametrize('region_tag', VALID_REGIONS)
def test_item_type_index(region_tag):
    data = item_type(region_tag, locale="enus")
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith('d3/data/item-type')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag', INVALID_REGIONS)
def test_item_type_index_invalid_region(region_tag):
    with pytest.raises(BNetRegionNotFoundError):
        item_type(region_tag, locale="enus")


@pytest.mark.parametrize('region_tag, item_category', list(product(VALID_REGIONS,
                                                                   ('Sword1h', 'Mace1h', 'Sword2h'))))
def test_item_type(region_tag, item_category):
    data = item_type(region_tag, item_type_slug=item_category, locale="enus")
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'd3/data/item-type/{slugify(item_category)}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, item_category', list(product(INVALID_REGIONS,
                                                                   ('Sword1h', 'Mace1h', 'Sword2h'))))
def test_item_type_invalid_region(region_tag, item_category):
    with pytest.raises(BNetRegionNotFoundError):
        item_type(region_tag, item_type_slug=item_category, locale="enus")


@pytest.mark.parametrize('region_tag, item_name', list(product(VALID_REGIONS,
                                                               ('corrupted-ashbringer-Unique_Sword_2H_104_x1',))))
def test_item(region_tag, item_name):
    data = item(region_tag, item_slug=item_name, locale="enus")
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'd3/data/item/{item_name}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, item_name', list(product(INVALID_REGIONS,
                                                               ('corrupted-ashbringer-Unique_Sword_2H_104_x1',))))
def test_item_invalid_region(region_tag, item_name):
    with pytest.raises(BNetRegionNotFoundError):
        item(region_tag, item_slug=item_name, locale="enus")


@pytest.mark.parametrize('region_tag, account_name', list(product(VALID_REGIONS,
                                                                  ('Rando#12345', 'Modnar#98786'))))
def test_api_account(region_tag, account_name):
    data = api_account(region_tag, account_name, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'd3/profile/{urlquote(account_name)}/')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, account_name', list(product(INVALID_REGIONS,
                                                                  ('Rando#12345', 'Modnar#98786'))))
def test_api_account_invalid_region(region_tag, account_name):
    with pytest.raises(BNetRegionNotFoundError):
        api_account(region_tag, account_name, locale='enus')


@pytest.mark.parametrize('region_tag, account_name, hero_id', list(product(VALID_REGIONS,
                                                                   ('Rando#12345', 'Modnar#98786'),
                                                                   (12345678, '12345678'))))
def test_api_hero(region_tag, account_name, hero_id):
    data = api_hero(region_tag, account_name, hero_id, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'd3/profile/{urlquote(account_name)}/hero/{hero_id}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, account_name, hero_id', list(product(INVALID_REGIONS,
                                                                   ('Rando#12345', 'Modnar#98786'),
                                                                   (12345678, '12345678'))))
def test_api_hero_invalid_region(region_tag, account_name, hero_id):
    with pytest.raises(BNetRegionNotFoundError):
        api_hero(region_tag, account_name, hero_id, locale='enus')


@pytest.mark.parametrize('region_tag, account_name, hero_id, category',
                         list(product(VALID_REGIONS, ('Rando#12345', 'Modnar#98786'),
                                      (12345678, '12345678'), ('items', 'follower-items'))))
def test_api_hero_categories(region_tag, account_name, hero_id, category):
    data = api_hero(region_tag, account_name, hero_id, category=category, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'd3/profile/{urlquote(account_name)}/hero/{hero_id}/{category.lower()}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, account_name, hero_id, category',
                         list(product(INVALID_REGIONS, ('Rando#12345', 'Modnar#98786'),
                                      (12345678, '12345678'), ('items', 'follower-items'))))
def test_api_hero_category_invalid_region(region_tag, account_name, hero_id, category):
    with pytest.raises(BNetRegionNotFoundError):
        api_hero(region_tag, account_name, hero_id, category=category, locale='enus')


@pytest.mark.parametrize('region_tag, account_name, hero_id, category',
                         list(product(VALID_REGIONS, ('Rando#12345', 'Modnar#98786'),
                                      (12345678, '12345678'), ('pets', 'mounts'))))
def test_api_hero_category_invalid_category(region_tag, account_name, hero_id, category):
    with pytest.raises(BNetValueError):
        api_hero(region_tag, account_name, hero_id, category=category, locale='enus')
