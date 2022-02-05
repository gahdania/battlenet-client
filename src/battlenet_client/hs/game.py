"""Provides access to the cards API endpoint, allowing the searching of cards"""

from typing import Optional, Any, TYPE_CHECKING, Dict, List

if TYPE_CHECKING:
    from client import HSClient


class Hearthstone:
    def __init__(self, client: "HSClient") -> None:
        self.client = client

    __class_name = "game"

    def card_search(
        self,
        locale: str,
        game_mode: Optional[str] = "constructed",
        field_values: Optional[List[Dict[str, Any]]] = None,
    ) -> Dict[str, Any]:
        """Searches for cards that match `field_values'

        Args:
            locale (str): locale to use with the API
            game_mode (str): the game mode for the cards, default is 'constructed'
            field_values (dict): search criteria, as key/value pairs
                For more information for the field names and options:
                https://develop.battle.net/documentation/hearthstone/game-data-apis

        Returns:
            dict: json decoded search results that match `field_values'

        Raises:
            HSClientError: when a client other than HSClient is used.
        """

        if field_values:
            return self.client.search(
                locale, "cards", fields=field_values, params={"gameMode": game_mode}
            )

        return self.client.search(locale, "cards", params={"gameMode": game_mode})

    def card(
        self, locale: str, card_id: str, game_mode: Optional[str] = "constructed"
    ) -> Dict[str, Any]:
        """Returns the card provided by `card_id'

        Args:
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
        if game_mode not in ("constructed", "battlegrounds", "mercenaries"):
            raise ValueError("Invalid game mode specified")

        return self.client.game_data(
            locale, "cards", card_id, params={"gameMode": game_mode}
        )

    def card_back_search(
        self, locale: str, field_values: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """Searches for cards that match `field_values'

        Args:
            locale (str): locale to use with the API
            field_values (dict): search criteria, as key/value pairs
                For more information for the field names and options:
                https://develop.battle.net/documentation/hearthstone/guides/card-backs

        Returns:
            dict: json decoded search results that match `field_values'

        Raises:
            HSClientError: when a client other than HSClient is used.
        """
        if field_values:
            return self.client.search(locale, "cardbacks", fields=field_values)

        return self.client.search(locale, "cardbacks")

    def card_back(self, locale: str, card_back_id: str) -> Dict[str, Any]:
        """Returns an index of Azerite Essences, or a specific Azerite Essence

        Args:
            locale (str): which locale to use for the request
            card_back_id (int, str): the ID or full slug of the card

        Returns:
            dict: json decoded data for the index/individual azerite essence(s)

        Raises:
            HSClientError: when a client other than HSClient is used.
        """
        return self.client.game_data(locale, "cardbacks", card_back_id)

    def card_deck(
        self, locale, field_values: Optional[List[Dict[str, Any]]]
    ) -> Dict[str, Any]:
        """Searches for cards that match `field_values'

        Args:
            locale (str): locale to use with the API
            field_values (dict): search criteria, as key/value pairs
                For more information for the field names and options:
                https://develop.battle.net/documentation/hearthstone/guides/decks

        Returns:
            dict: json decoded search results that match `field_values'

        Raises:
            HSClientError: when a client other than HSClient is used.
        """
        return self.client.search(locale, "deck", field_values)

    def metadata(self, locale: str, meta_data: Optional[str] = None) -> Dict[str, Any]:
        """Returns an index of Azerite Essences, or a specific Azerite Essence

        Args:
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
        if meta_data:
            return self.client.game_data(locale, "metadata", meta_data)

        return self.client.game_data(locale, "metadata")
