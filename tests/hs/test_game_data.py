from itertools import product

import pytest

from battlenet_client.constants import VALID_REGIONS
from battlenet_client.exceptions import BNetRegionNotFoundError, BNetValueError
from battlenet_client.hs.game_data import card, card_search, card_back, card_back_search, card_deck, metadata
from battlenet_client.utils import slugify
from ..constants import INVALID_REGIONS


@pytest.mark.parametrize('region_tag', VALID_REGIONS)
def test_card_back_search_textfilter_value_error(region_tag):
    field_values = {
        'textFilter': 'only',
        'sort': 'dataAdded:desc'
    }
    with pytest.raises(BNetValueError):
        card_back_search(region_tag, field_values)


@pytest.mark.parametrize('region_tag', INVALID_REGIONS)
def test_card_back_search_region_error(region_tag):
    field_values = {
        'textFilter': 'only',
        'sort': 'dataAdded:desc'
    }
    with pytest.raises(BNetRegionNotFoundError):
        card_back_search(region_tag, field_values, locale='enus')


@pytest.mark.parametrize('region_tag', VALID_REGIONS)
def test_card_back_search_textfilter_with_locale(region_tag):
    field_values = {
        'textFilter': 'only',
        'sort': 'dataAdded:desc'
    }
    data = card_back_search(region_tag, field_values, locale='en_US')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'hearthstone/cardbacks')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert 'textFilter' in data[1]
    assert 'sort' in data[1]
    assert data[1]['locale'] == 'en_US'
    for k, v in field_values.items():
        assert k in data[1]
        assert data[1][k] == v


@pytest.mark.parametrize('region_tag, card_back_name',
                         list(product(VALID_REGIONS, ('155-Pizza-Stone', '2-black-temple'))))
def test_card_back(region_tag, card_back_name):
    data = card_back(region_tag, card_back_id=card_back_name, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'hearthstone/cardbacks/{slugify(card_back_name)}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, card_back_name',
                         list(product(INVALID_REGIONS, ('155-Pizza-Stone', '2-black-temple'))))
def test_card_back_region_error(region_tag, card_back_name):
    with pytest.raises(BNetRegionNotFoundError):
        card_back(region_tag, card_back_id=card_back_name, locale='enus')


@pytest.mark.parametrize('region_tag', VALID_REGIONS)
def test_card_deck_by_valid_code(region_tag):
    data = card_deck(region_tag, {
        'code': 'AAECAQcG+wyd8AKS+AKggAOblAPanQMMS6IE/web8wLR9QKD+wKe+wKz/AL1gAOXlAOalAOSnwMA'}, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'hearthstone/deck')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert 'code' in data[1]
    assert data[1]['locale'] == 'en_US'
    assert data[1]['code'] == 'AAECAQcG+wyd8AKS+AKggAOblAPanQMMS6IE/web8wLR9QKD+wKe+wKz/AL1gAOXlAOalAOSnwMA'


@pytest.mark.parametrize('region_tag', INVALID_REGIONS)
def test_card_deck_by_region_error(region_tag):
    with pytest.raises(BNetRegionNotFoundError):
        card_deck(region_tag, {
            'code': 'AAECAQcG+wyd8AKS+AKggAOblAPanQMMS6IE/web8wLR9QKD+wKe+wKz/AL1gAOXlAOalAOSnwMA'}, locale='enus')


@pytest.mark.parametrize('region_tag', VALID_REGIONS)
def test_card_deck_by_valid_ids(region_tag):
    field_values = {
        'ids': [906, 1099, 1363, 1367, 46706, 48099, 48759, 49184, 50071, 50278, 51714, 52109, 52632, 52715, 53409,
                53413, 53756, 53969, 54148, 54425, 54431, 54874, 54898, 54917, 55166, 55245, 55438, 55441, 55907,
                57416],
        'hero': 813
    }
    data = card_deck(region_tag, field_values, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'hearthstone/deck')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert 'ids' in data[1]
    assert 'hero' in data[1]
    assert data[1]['locale'] == 'en_US'
    for k, v in field_values.items():
        assert k in data[1]
        assert data[1][k] == v


@pytest.mark.parametrize('region_tag', INVALID_REGIONS)
def test_card_deck_by_valid_ids_region_error(region_tag):
    field_values = {
        'ids': [906, 1099, 1363, 1367, 46706, 48099, 48759, 49184, 50071, 50278, 51714, 52109, 52632, 52715, 53409,
                53413, 53756, 53969, 54148, 54425, 54431, 54874, 54898, 54917, 55166, 55245, 55438, 55441, 55907,
                57416],
        'hero': 813
    }
    with pytest.raises(BNetRegionNotFoundError):
        card_deck(region_tag, field_values, locale='enus')


@pytest.mark.parametrize('region_tag', VALID_REGIONS)
def test_card_deck_by_valid_id(region_tag):
    field_values = {
        'ids': 906,
        'hero': 813
    }
    data = card_deck(region_tag, field_values, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'hearthstone/deck')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert 'ids' in data[1]
    assert 'hero' in data[1]
    assert data[1]['locale'] == 'en_US'
    for k, v in field_values.items():
        assert k in data[1]
        assert data[1][k] == v


@pytest.mark.parametrize('region_tag', INVALID_REGIONS)
def test_card_deck_by_valid_id_region_error(region_tag):
    field_values = {
        'ids': 906,
        'hero': 813
    }
    with pytest.raises(BNetRegionNotFoundError):
        card_deck(region_tag, field_values, locale='enus')


@pytest.mark.parametrize('region_tag', VALID_REGIONS)
def test_metadata_index(region_tag):
    data = metadata(region_tag, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'hearthstone/metadata')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag', INVALID_REGIONS)
def test_metadata_index_region_error(region_tag):
    with pytest.raises(BNetRegionNotFoundError):
        metadata(region_tag, locale='enus')


@pytest.mark.parametrize('region_tag, metadata_type',
                         list(product(VALID_REGIONS,
                                      ('sets', 'setGroups', 'types', 'rarities', 'classes', 'minionTypes', 'keywords'))))
def test_metadata_types(region_tag, metadata_type):
    data = metadata(region_tag, meta_data=metadata_type, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'hearthstone/metadata/{metadata_type}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, metadata_type',
                         list(product(INVALID_REGIONS,
                                      ('sets', 'setGroups', 'types', 'rarities', 'classes', 'minionTypes', 'keywords'))))
def test_metadata_types_region_error(region_tag, metadata_type):
    with pytest.raises(BNetRegionNotFoundError):
        metadata(region_tag, meta_data=metadata_type, locale='enus')


@pytest.mark.parametrize('region_tag, metadata_type',
                         list(product(VALID_REGIONS,
                                      ('typesSets', 'wrongaties', 'glasses'))))
def test_metadata_types_category_invalid(region_tag, metadata_type):
    with pytest.raises(BNetValueError):
        metadata(region_tag, meta_data=metadata_type, locale='enus')


@pytest.mark.parametrize('region_tag', VALID_REGIONS)
def test_card_search_all_cards(region_tag):
    data = card_search(region_tag, {}, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'hearthstone/cards')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag', INVALID_REGIONS)
def test_search_all_cards_region_error(region_tag):
    with pytest.raises(BNetRegionNotFoundError):
        card_search(region_tag, {}, locale='enus')


@pytest.mark.parametrize('region_tag', VALID_REGIONS)
def test_card_search_valid_fields(region_tag):
    field_values = {
        'class': 'shaman',
        'attack': 2
    }
    data = card_search(region_tag, field_values, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'hearthstone/cards')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert 'class' in data[1]
    assert 'attack' in data[1]
    assert data[1]['locale'] == 'en_US'
    for k, v in field_values.items():
        assert k in data[1]
        assert data[1][k] == v


@pytest.mark.parametrize('region_tag', INVALID_REGIONS)
def test_card_search_valid_fields_region_error(region_tag):
    field_values = {
        'class': 'shaman',
        'attack': 2
    }
    with pytest.raises(BNetRegionNotFoundError):
        card_search(region_tag, field_values, locale='enus')


@pytest.mark.parametrize('region_tag', VALID_REGIONS)
def test_card_search_invalid_fields(region_tag):
    field_values = {
        'class': 'escort',
        'attack': 2
    }
    data = card_search(region_tag, field_values, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'hearthstone/cards')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert 'class' in data[1]
    assert 'attack' in data[1]
    assert data[1]['locale'] == 'en_US'
    assert data[1]['class'] == 'escort'
    assert data[1]['attack'] == 2


@pytest.mark.parametrize('region_tag', INVALID_REGIONS)
def test_card_search_invalid_fields_region_error(region_tag):
    field_values = {
        'class': 'escort',
        'attack': 2
    }
    with pytest.raises(BNetRegionNotFoundError):
        card_search(region_tag, field_values, locale='enus')


@pytest.mark.parametrize('region_tag, card_id',
                         list(product(VALID_REGIONS,
                                      ('38913', '50019', '38531',
                                       '38913-a-light-in-the-darkness',
                                       '50019-a-new-challenger',
                                       '38531-aberrant-berserker'))))
def test_card_valid_region(region_tag, card_id):
    data = card(region_tag, card_id, locale='enus')
    assert isinstance(data, tuple)
    assert isinstance(data[0], str)
    assert data[0].endswith(f'hearthstone/cards/{slugify(card_id)}')
    assert isinstance(data[1], dict)
    assert 'locale' in data[1]
    assert 'class' in data[1]
    assert 'attack' in data[1]
    assert data[1]['locale'] == 'en_US'


@pytest.mark.parametrize('region_tag, card_id',
                         list(product(INVALID_REGIONS,
                                      ('38913', '50019', '38531',
                                       '38913-a-light-in-the-darkness',
                                       '50019-a-new-challenger',
                                       '38531-aberrant-berserker'))))
def test_card_valid_region(region_tag, card_id):
    with pytest.raises(BNetRegionNotFoundError):
        card(region_tag, card_id, locale='enus')
