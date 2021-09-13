import pytest

from battlenet_client.util import slugify, localize, currency_convertor


def test_localize():
    locale = localize('EnuS')
    assert(type(locale) == str)
    assert(locale[:2] == 'en')
    assert(locale[-2:] == 'US')


@pytest.mark.parametrize("test_input", [
    ['EnuS', 'EngB'],
    ('EnuS', 'EngB'),
    {'lang': 'en', 'country': 'US'}
])
def test_localize_wrong_type(test_input):
    with pytest.raises(TypeError):
        localize(test_input)


@pytest.mark.parametrize("test_value", [
    'zzus',
    'enZZ'
])
def test_localize_wrong_lang_country(test_value):
    with pytest.raises(ValueError):
        localize(test_value)


def test_slugify():
    assert(slugify("Zul'jin") == 'zuljin')
    assert(slugify("Zul'jin").islower())


@pytest.mark.parametrize("test_input", [
    ['EnuS', 'EngB'],
    ('EnuS', 'EngB'),
    {'lang': 'en', 'country': 'US'}
])
def test_slugify_type_error(test_input):
    with pytest.raises(TypeError):
        slugify(test_input)


def test_slugify_no_apostrophe():
    assert(slugify("Zul'jin").find('\'') == -1)


def test_slugify_no_space():
    assert(slugify('Moon Guard').find(' ') == -1)


def test_currency_convertor_positive():
    money = currency_convertor(394567)
    assert(type(money) in (list, tuple))
    assert(len(money) == 3)
    assert(money == (39, 45, 67))


def test_currency_convertor_zero():
    money = currency_convertor('0')
    assert(type(money) in (list, tuple))
    assert(len(money) == 3)
    assert(money == (0, 0, 0))


def test_currency_convertor_negative():
    with pytest.raises(ValueError):
        currency_convertor(-1)


@pytest.mark.parametrize("test_input", [
    [1, 3, 4],
    (1, 3, 4),
    {'g': 1, 's': 3, 'c': 4}
])
def test_currency_convertor_wrong_types(test_input):
    with pytest.raises(TypeError):
        currency_convertor(test_input)
