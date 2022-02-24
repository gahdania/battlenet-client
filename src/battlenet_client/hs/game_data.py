"""Generates the URI/querystring and headers for the Hearthsone API endpoints

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of HearthstoneI and any data
    retrieved from this API.
"""

from typing import Optional, Any, Dict

from battlenet_client import utils


class Hearthstone:
    @staticmethod
    def card_search(
        client,
        region_tag: str,
        field_values: Dict[str, Any],
        locale: Optional[str] = None,
    ):
        """Searches for cards that match `field_values'

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            field_values (dict): search criteria, as key/value pairs
                For more information for the field names and options:
                https://develop.battle.net/documentation/hearthstone/game-data-apis

        Returns:
            dict: json decoded search results that match `field_values'

        Raises:
            HSClientError: when a client other than HSClient is used.
        """
        if "gameMode" not in field_values.keys():
            field_values["gameMode"] = "constructed"

        uri = f"{utils.api_host(region_tag)}/hearthstone/cards"

        #  adding locale and namespace key/values pairs to field_values to make a complete params list
        field_values.update({"locale": utils.localize(locale)})

        return client.get(uri, params=field_values).json()

    @staticmethod
    def card(
        client,
        region_tag: str,
        card_id: str,
        locale: Optional[str] = None,
        game_mode: Optional[str] = "constructed",
    ):
        """Returns the card provided by `card_id'

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            card_id (int, str): the ID or full slug of the card
            game_mode (str, optional): the game mode
                See for more information:
                https://develop.battle.net/documentation/hearthstone/guides/game-modes

        Returns:
            dict: json decoded data for the index/individual azerite essence(s)

        Raises:
            HSClientError: when a client other than HSClient is used.
        """
        uri = f"{utils.api_host(region_tag)}/hearthstone/cards/{card_id}"

        return client.get(
            uri, params={"locale": utils.localize(locale), "gameMode": game_mode}
        ).json()

    @staticmethod
    def card_back_search(
        client,
        region_tag: str,
        field_values: Dict[str, Any],
        locale: Optional[str] = None,
    ):
        """Searches for cards that match `field_values'

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            field_values (dict): search criteria, as key/value pairs
                For more information for the field names and options:
                https://develop.battle.net/documentation/hearthstone/guides/card-backs

        Returns:
            dict: json decoded search results that match `field_values'

        Raises:
            HSClientError: when a client other than HSClient is used.
        """
        uri = f"{utils.api_host(region_tag)}/hearthstone/cardbacks"

        #  adding locale and namespace key/values pairs to field_values to make a complete params list
        field_values.update({"locale": utils.localize(locale)})

        return client.get(uri, params=field_values).json()

    @staticmethod
    def card_back(
        client, region_tag: str, card_back_id: str, locale: Optional[str] = None
    ):
        """Returns an index of Azerite Essences, or a specific Azerite Essence

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            card_back_id (int, str): the ID or full slug of the card

        Returns:
            dict: json decoded data for the index/individual azerite essence(s)

        Raises:
            HSClientError: when a client other than HSClient is used.
        """
        uri = f"{utils.api_host(region_tag)}/hearthstone/cards/{card_back_id}"

        return client.get(uri, params={"locale": utils.localize(locale)}).json()

    @staticmethod
    def card_deck(
        client,
        region_tag: str,
        field_values: Optional[Dict[str, Any]],
        locale: Optional[str] = None,
    ):
        """Searches for cards that match `field_values'

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            field_values (dict): search criteria, as key/value pairs
                For more information for the field names and options:
                https://develop.battle.net/documentation/hearthstone/guides/decks

        Returns:
            dict: json decoded search results that match `field_values'

        Raises:
            HSClientError: when a client other than HSClient is used.
        """
        uri = f"{utils.api_host(region_tag)}/hearthstone/deck"

        #  adding locale and namespace key/values pairs to field_values to make a complete params list
        field_values.update({"locale": utils.localize(locale)})

        return client.get(uri, params=field_values).json()

    @staticmethod
    def metadata(
        client,
        region_tag: str,
        meta_data: Optional[str] = None,
        locale: Optional[str] = None,
    ):
        """Returns an index of Azerite Essences, or a specific Azerite Essence

        Args:
            client (obj: oauth): OpenID/OAuth instance
            region_tag (str): region_tag abbreviation
            locale (str): which locale to use for the request
            meta_data (str, optional): what metadata to filter
                Please see below for more information
                https://develop.battle.net/documentation/hearthstone/guides/metadata
                valid options: 'sets', 'setGroups', 'types', 'rarities', 'classes',
                    'minionTypes', 'keywords'

        Returns:
            dict: json decoded data for the index/individual azerite essence(s)

        Raises:
            HSClientError: when a client other than HSClient is used.
        """
        uri = f"{utils.api_host(region_tag)}/hearthstone/metadata"

        if meta_data:
            uri += f"/{meta_data}"

        return client.get(uri, params={"locale": utils.localize(locale)}).json()