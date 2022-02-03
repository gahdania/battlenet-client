import pytest

from battlenet_client.wow import currency_convertor


@pytest.mark.parametrize(
    "value",
    [(1723, 40, 32), [1723, 40, 32], {"gold": 1723, "silver": 40, "copper": 32}],
)
def test_currency_convertor_invalid_type(value):
    with pytest.raises(TypeError):
        currency_convertor(value)


@pytest.mark.parametrize("value", ["17234032", 17234032])
def test_currency_convertor_str(value):
    value = currency_convertor(value)
    assert isinstance(value, tuple)
    assert value == (1723, 40, 32)
