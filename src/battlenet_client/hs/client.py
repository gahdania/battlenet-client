"""Defines the client for connected to the World of Warcraft/Classic/TBC Classic

This module contains the client class definitions for accessing World of Warcraft API data.
There are two flavors of client, one implements the client credential workflow, which happens
to be the most common.  The other implements the user authorization workflow

Examples:
    > from battlenet_client.wow import WoWClient
    > client = WoWClient(<region>, <locale>, client_id='<client ID>', client_secret='<client secret>')

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of WoW and WoW Classic
    and any data pertaining thereto

.. moduleauthor:: David "Gahd" Couples <gahdania@gahd.io>
"""
import importlib
from typing import Optional, Any, List

from battlenet_client.bnet.client import BNetClient
from battlenet_client.bnet.constants import HS

from constants import MODULES


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

        super().__init__(region, HS, client_id=client_id, client_secret=client_secret)

        # load the API endpoints programmatically
        for mod_name in MODULES:
            mod = importlib.import_module(f"battlenet_client.hs.{mod_name}")
            for cls_name in dir(mod):
                if not cls_name.startswith("__") and isinstance(
                    getattr(mod, cls_name), type
                ):
                    setattr(self, mod_name, getattr(mod, cls_name)(self))

    def __repr__(self):
        return f"{self.__class__.__name__} Instance: {self.game['abbrev']} {self.tag}"

    def game_data(self, locale: str, *args, **kwargs) -> Any:
        """Used to retrieve data from the source data APIs

        Args:
            locale (str): the locale to use, example: en_US


        Returns:
            dict: data returned by the API
        """
        uri = f"{self.api_host}/hearthstone/{'/'.join([self.slugify(arg) for arg in args])}"

        kwargs["params"]["locale"] = self.localize(locale)

        return self._get(uri, **kwargs)

    # def media_data(self, locale: str, namespace: str, *args: Union[str, int]) -> Any:
    #     """Used to retrieve media data including URLs for them
    #
    #     Args:
    #         locale (str): the locale to use, example: en_US
    #         namespace (str): namespace the API requires, example: static
    #
    #     Returns:
    #         dict: data returned by the API
    #     """
    #     join_args = [self.slugify(str(arg)) for arg in args if arg is not None]
    #     uri = f"{self.api_host}/data/wow/media/{'/'.join(join_args)}"
    #     return self._get(uri, params={'locale': locale}, headers={'Battlenet-Namespace': getattr(self, namespace)})

    def search(
        self, locale: str, document: str, fields: Optional[List[Any]] = None
    ) -> Any:
        """Used to perform searches where available

        Args:
            locale (str): the locale to use, example: en_US
            document (str): the document tree to be searched
            fields (dict): the criteria to search

        Returns:
            dict: data returned by the API
        """
        uri = f"{self.api_host}/hearthstone/{self.slugify(document)}"
        return self._get(
            uri,
            params={"locale": self.localize(locale)},
            fields=fields,
        )
