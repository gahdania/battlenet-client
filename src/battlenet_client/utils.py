"""Miscellaneous functions to support world of warcraft

Functions:
    currency_convertor
"""
from typing import Tuple, Optional, Union


WOW_CLASSICS = ("classic1x", "classic")


def currency_convertor(value: int) -> Tuple[int, int, int]:
    """Returns the value into gold, silver and copper

    Args:
        value (int/str): the value to be converted

    Returns:
        tuple: gold, silver and copper values
    """
    value = int(value)

    if value < 0:
        raise ValueError("Value cannot be negative")

    return value // 10000, (value % 10000) // 100, value % 100


def slugify(value: str) -> str:
    """Returns the 'slugified' string

    Args:
        value (str): the string to be converted into a slug

    Returns:
        str: the slug of :value:
    """
    return value.lower().replace("'", "").replace(" ", "-")


def localize(locale: Optional[str] = None) -> Union[None, str]:
    """Returns the standardized locale

    Args:
        locale (str): the locality to be standardized

    Returns:
        str: the locale in the format of "<lang>_<COUNTRY>"

    Raise:
        TypeError: when locale is not a string
        ValueError: when the lang and country are not in the given lists
    """
    if locale is None:
        return None

    if not isinstance(locale, str):
        raise TypeError("Locale must be a string")

    if locale[:2].lower() not in ("en", "es", "pt", "fr", "ru", "de", "it", "ko", "zh"):
        raise ValueError("Invalid language bnet")

    if locale[-2:].lower() not in (
        "us",
        "mx",
        "br",
        "gb",
        "es",
        "fr",
        "ru",
        "de",
        "pt",
        "it",
        "kr",
        "tw",
        "cn",
    ):
        raise ValueError("Invalid country bnet")

    return f"{locale[:2].lower()}_{locale[-2:].upper()}"


def api_host(region: str):
    if region.lower() == "cn":
        return "https://gateway.battlenet.com.cn"

    return f"https://{region.lower()}.api.blizzard.com"


def auth_host(region: str):
    if region.lower() == "cn":
        return "https://www.battlenet.com.cn"

    if region.lower() in ("kr", "tw"):
        return "https://apac.battle.net"

    return f"https://{region.lower()}.battle.net"


def render_host(region: str):
    if region.lower() == "cn":
        return "https://render.worldofwarcraft.com.cn"

    return f"https://render-{region.lower()}.worldofwarcraft.com"
