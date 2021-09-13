import pytest

from battlenet_client.util import slugify, localize, currency_convertor


def test_localize():
    locale = localize('EnuS')
    assert(type(locale) == str)
    assert(locale[:2] == 'en')
    assert(locale[-2:] == 'US')


def test_localize_wrong_type():
    with pytest.raises(TypeError):
        localize(1)
        localize(['EnuS', 'EngB'])
        localize(('EnuS', 'EngB'))
        localize({'lang': 'en', 'country': 'US'})


def test_localize_wrong_lang_country():
    with pytest.raises(ValueError):
        localize('zzus')
        localize('enZZ')


def test_slugify():
    assert(slugify("Zul'jin") == 'zuljin')
    assert(slugify("Zul'jin").islower())


def test_slugify_type_error():
    with pytest.raises(TypeError):
        slugify(1)
        slugify(['EnuS', 'EngB'])
        slugify(('EnuS', 'EngB'))
        slugify({'lang': 'en', 'country': 'US'})


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


def test_currency_convertor_wrong_types():
    with pytest.raises(TypeError):
        currency_convertor([1, 3, 4])
        currency_convertor((1, 3, 4))
        currency_convertor({'g': 1, 's': 3, 'c': 4})
