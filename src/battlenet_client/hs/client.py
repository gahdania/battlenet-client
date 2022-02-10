"""Defines the client for connected to Hearthstone

Classes:
    HSClient

Examples:
    > from battlenet_client import hs
    > client = hs.HSClient(<region>, <locale>, client_id='<client ID>', client_secret='<client secret>')

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of WoW and WoW Classic
    and any data pertaining thereto

"""
from typing import Optional, Any, Dict

from requests import exceptions, Response
from time import sleep

from ..bnet.client import BNetClient
from ..bnet.misc import localize, slugify


class HSClient(BNetClient):
    """Defines the client workflow class for HearthStone

    Args:
        region (str): region abbreviation for use with the APIs

    Keyword Args:
        client_id (str, optional): the client ID from the developer portal
        client_secret (str, optional): the client secret from the developer portal
    """

    def __init__(
        self,
        region: str,
        *,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
    ) -> None:

        super().__init__(region, client_id=client_id, client_secret=client_secret)

    def __repr__(self):
        return f"{self.__class__.__name__} Instance: HS {self.tag}"

    def game_data(self, locale: str, *args, **kwargs) -> Response:
        """Used to retrieve data from the source data APIs

        Args:
            locale (str): the locale to use, example: en_US


        Returns:
            dict: data returned by the API
        """
        uri = f"{self.api_host}/hearthstone/{'/'.join([slugify(arg) for arg in args])}"

        retries = 0

        kwargs["params"]["locale"] = localize(locale)

        while retries < 5:
            try:
                response = self.get(uri, **kwargs)
                response.raise_for_status()
            except exceptions.HTTPError as err:
                if err.response.status_code == 429:
                    retries += 1
                    sleep(1)
            else:
                return response.json()

    def search(
        self,
        locale: str,
        document: str,
        fields: Dict[str, Any],
        game_mode: Optional[str] = "constructed",
    ) -> Response:
        """Used to perform searches where available

        Args:
            locale (str): the locale to use, example: en_US
            document (str): the document tree to be searched
            fields (dict): the criteria to search
            game_mode (str): the game mode to search through

        Returns:
            dict: data returned by the API
        """
        uri = f"{self.api_host}/hearthstone/{slugify(document)}"

        retries = 0
        params = {"locale": localize(locale)}

        if document == "cards" and game_mode.lower() in (
            "constructed",
            "battlegrounds",
            "mercenaries",
        ):
            params.update({"gameMode": game_mode})
        else:
            raise ValueError("Invalid Game Mode")

        params.update(fields)

        while retries < 5:
            try:
                response = self.get(uri, params=params)
                response.raise_for_status()
            except exceptions.HTTPError as err:
                if err.response.status_code == 429:
                    retries += 1
                    sleep(1)
            else:
                return response.json()
