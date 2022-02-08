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
from typing import Optional, Any, Dict, List

from ..bnet.client import BNetClient
from ..misc import localize, slugify


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

    def game_data(self, locale: str, *args, **kwargs) -> Dict[str, Any]:
        """Used to retrieve data from the source data APIs

        Args:
            locale (str): the locale to use, example: en_US


        Returns:
            dict: data returned by the API
        """
        uri = f"{self.api_host}/hearthstone/{'/'.join([slugify(arg) for arg in args])}"

        kwargs["params"]["locale"] = localize(locale)

        return self._get(uri, **kwargs)

    def search(
        self,
        locale: str,
        document: str,
        fields: Optional[List[Dict[str, Any]]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """Used to perform searches where available

        Args:
            locale (str): the locale to use, example: en_US
            document (str): the document tree to be searched
            fields (dict): the criteria to search

        Returns:
            dict: data returned by the API
        """
        uri = f"{self.api_host}/hearthstone/{slugify(document)}"
        kwargs["params"]["locale"] = localize(locale)
        kwargs["fields"] = fields

        return self._get(uri, **kwargs)
