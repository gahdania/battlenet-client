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

from battlenet_client.bnet.client import BNetClient
from battlenet_client.bnet.constants import D3

from constants import MODULES


class D3Client(BNetClient):
    """Defines the client workflow class for the World of Warcraft API

    Args:
        region (str): region abbreviation for use with the APIs

    Keyword Args:
        scope (list of str, optional): the scope or scopes to use during the data that require the
            Web Application Flow
        redirect_uri (str, optional): the URI to return after a successful authentication between the user and Blizzard
        client_id (str, optional): the client ID from the developer portal
        client_secret (str, optional): the client secret from the developer portal
    """

    def __init__(
        self,
        region,
        *,
        scope=None,
        redirect_uri=None,
        client_id=None,
        client_secret=None,
    ):

        if not client_id:
            client_id = config("CLIENT_ID")

        if not client_secret:
            client_secret = config("CLIENT_SECRET")

        super().__init__(
            region,
            D3,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
            redirect_uri=redirect_uri,
        )

        # load the API endpoints programmatically
        for mod_name in MODULES:
            mod = importlib.import_module(f"battlenet_client.d3.{mod_name}")
            for cls_name in dir(mod):
                if not cls_name.startswith("__") and isinstance(
                    getattr(mod, cls_name), type
                ):
                    setattr(self, mod_name, getattr(mod, cls_name)(self))

    def game_data(self, locale, *args, **kwargs):
        if args[0].startswith("https"):
            uri = args[0]
        else:
            uri = f"{self.api_host}/data/d3/{'/'.join([str(arg) for arg in args if arg is not None])}"

        kwargs["params"]["locale"] = self.localize(locale)

        return self._get(uri, **kwargs)

    def community(self, locale, *args, **kwargs):
        if args[0].startswith("https"):
            uri = args[0]
        else:
            uri = f"{self.api_host}/d3/data/{'/'.join([str(arg) for arg in args if arg is not None])}"
        kwargs["params"]["locale"] = self.localize(locale)
        return self._get(uri, **kwargs)

    def profile_api(self, locale, *args, **kwargs):
        if args[0].startswith("https"):
            uri = args[0]
        else:
            uri = f"{self.api_host}/d3/profile/{'/'.join([str(arg) for arg in args if arg is not None])}"

        kwargs["params"]["locale"] = self.localize(locale)
        return self.get(uri, **kwargs)
