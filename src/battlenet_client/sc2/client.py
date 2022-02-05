"""Defines the client for connected to the World of Warcraft/Classic/TBC Classic

This module contains the client class definitions for accessing World of Warcraft API data.
There are two flavors of client, one implements the client credential workflow, which happens
to be the most common.  The other implements the user authorization workflow

Examples:
    > from wow_api import WoWCredentialClient
    > client = WoWCredentialClient(<region>, <locale>, client_id='<client ID>', client_secret='<client secret>')

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of WoW and WoW Classic
    and any data pertaining thereto

.. moduleauthor:: David "Gahd" Couples <gahdania@gahd.io>
"""
import importlib
from decouple import config

from typing import Optional, List, Dict, Any

from battlenet_client.bnet.client import BNetClient
from battlenet_client.bnet.constants import SC2

from .constants import MODULES


class SC2Client(BNetClient):
    """Defines the client workflow class for the World of Warcraft API

    Args:
        region (str): region abbreviation for use with the APIs

    Keyword Args:
        scope (list, optional): the scope or scopes to use during the data that require the
            Web Application Flow
        redirect_uri (str, optional): the URI to return after a successful authentication between the user and Blizzard
        client_id (str, optional): the client ID from the developer portal
        client_secret (str, optional): the client secret from the developer portal
    """

    def __init__(
        self,
        region: str,
        *,
        scope: Optional[List[str]] = None,
        redirect_uri: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
    ):

        if not client_id:
            client_id = config("CLIENT_ID")

        if not client_secret:
            client_secret = config("CLIENT_SECRET")

        super().__init__(
            region,
            SC2,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
            redirect_uri=redirect_uri,
        )

        # load the API endpoints programmatically
        if self.tag == "cn":
            mod_group = "cn"
        else:
            mod_group = "noncn"

        for mod_name, classes in MODULES[mod_group].items():
            mod = importlib.import_module(f"battlenet_client.sc2.{mod_name}")
            for cls in classes:
                setattr(self, getattr(mod, cls).__class_name, getattr(mod, cls)(self))

    def game_data(self, locale: str, *args, **kwargs) -> Dict[str, Any]:

        kwargs["params"]["locale"] = self.localize(locale)

        if args[0].startswith("https"):
            uri = args[0]
        else:
            uri = f"{self.api_host}/data/sc2/{'/'.join([str(arg) for arg in args if arg is not None])}"

        return self._get(uri, **kwargs)

    def community(self, locale: str, *args, **kwargs):

        kwargs["params"]["locale"] = self.localize(locale)

        if args[0].startswith("https"):
            uri = args[0]
        else:
            uri = f"{self.api_host}/sc2/{'/'.join([str(arg) for arg in args if arg is not None])}"

        return self._get(uri, **kwargs)
