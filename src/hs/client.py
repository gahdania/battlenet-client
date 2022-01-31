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
from typing import List, Optional, Any, Dict, Union

from battlenet_client.client import BattleNetClient
from battlenet_client.constants import HS

from hs.exceptions import HSClientError

MODULES = ['game']


class HSClient(BattleNetClient):
    """Defines the client workflow class for HearthStone

    Args:
        region (str): region abbreviation for use with the APIs

    Keyword Args:
        release (str, optional): the release to use.
            'classic1x` for original World of Warcraft Classic
            'classic' for The Burning Crusade
            None for current retail version
        scope (list of str, optional): the scope or scopes to use during the data that require the
            Web Application Flow
        redirect_uri (str, optional): the URI to return after a successful authentication between the user and Blizzard
        client_id (str, optional): the client ID from the developer portal
        client_secret (str, optional): the client secret from the developer portal

    Attributes:
        dynamic (str): the namespace to use for dynamic elements of the API (ie: characters, and guilds)
        static (str): the namespace to use for static elements of the API (ie: realms, connected_realms)
        profile (str): the namespace to use for profile based elements (ie: player info, protected char info)
    """

    def __init__(self, region: str, *,  client_id: Optional[str] = None,
                 client_secret: Optional[str] = None) -> None:

        super().__init__(region, HS, client_id=client_id, client_secret=client_secret)

        # load the API endpoints programmatically
        for mod_name in MODULES:
            mod = getattr(self, mod_name)
            for cls_name in dir(mod):
                if not cls_name.startswith('__') and isinstance(getattr(mod, cls_name), type):
                    setattr(self, mod_name, getattr(mod, cls_name)(self))

    def __repr__(self):
        return f"{self.__class__.__name__} Instance: {self.game['abbrev']} {self.tag}"

    def game_data(self, locale: str, namespace: str, *args: Union[str, int]) -> Any:
        """Used to retrieve data from the source data APIs

        Args:
            locale (str): the locale to use, example: en_US
            namespace (str): namespace the API requires, example: static

        Returns:
            dict: data returned by the API
        """
        if isinstance(args[0], str) and args[0].startswith('http'):
            uri = args[0]
        else:
            uri = f"{self.api_host}/data/wow/{'/'.join([str(arg) for arg in args if arg is not None])}"

        return self._get(uri, params={'locale': locale}, headers={'Battlenet-Namespace': getattr(self, namespace)})

    def media_data(self, locale: str, namespace: str, *args: Union[str, int]) -> Any:
        """Used to retrieve media data including URLs for them

        Args:
            locale (str): the locale to use, example: en_US
            namespace (str): namespace the API requires, example: static

        Returns:
            dict: data returned by the API
        """
        join_args = [self.slugify(str(arg)) for arg in args if arg is not None]
        uri = f"{self.api_host}/data/wow/media/{'/'.join(join_args)}"
        return self._get(uri, params={'locale': locale}, headers={'Battlenet-Namespace': getattr(self, namespace)})

    def search(self, locale: str, namespace: str, document: str, fields: Dict[str, Any]) -> Any:
        """Used to perform searches where available

        Args:
            locale (str): the locale to use, example: en_US
            namespace (str): namespace the API requires, example: static
            document (str): the document tree to be searched
            fields (dict): the criteria to search

        Returns:
            dict: data returned by the API
        """
        uri = f"{self.api_host}/data/wow/search/{self.slugify(document)}"
        return self._get(uri, params={'locale': locale}, headers={'Battlenet-Namespace': getattr(self, namespace)},
                         fields=fields)
