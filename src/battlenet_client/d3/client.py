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
from decouple import config

import battlenet_client


class D3Client(battlenet_client.BattleNetClient):
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

    def __init__(self, region, *,  scope=None, redirect_uri=None, client_id=None, client_secret=None):

        if not client_id:
            client_id = config('CLIENT_ID')

        if not client_secret:
            client_secret = config('CLIENT_SECRET')

        super().__init__(region, battlenet_client.D3, client_id, client_secret, scope=scope, redirect_uri=redirect_uri)

    def game_data(self, locale, *args, **kwargs):
        if args[0].startswith('https'):
            uri = args[0]
        else:
            uri = f"{self.api_host}/data/d3/{'/'.join([str(arg) for arg in args if arg is not None])}"

        return self.api_get(uri, locale, **kwargs)

    def community(self, locale, *args, **kwargs):
        if args[0].startswith('https'):
            uri = args[0]
        else:
            uri = f"{self.api_host}/d3/data/{'/'.join([str(arg) for arg in args if arg is not None])}"

        return self.api_get(uri, locale, **kwargs)

    def profile_api(self, locale, *args, **kwargs):
        if args[0].startswith('https'):
            uri = args[0]
        else:
            uri = f"{self.api_host}/d3/profile/{'/'.join([str(arg) for arg in args if arg is not None])}"

        return self.api_get(uri, locale, **kwargs)
