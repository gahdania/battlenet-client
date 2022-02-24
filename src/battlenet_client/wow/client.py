"""Defines the client for connected to the World of Warcraft/Classic/TBC Classic

This module contains the client class definitions for accessing World of Warcraft API data.
There are two flavors of client, one implements the client credential workflow, which happens
to be the most common.  The other implements the user authorization workflow

Examples:
    > # for credential work flows (most of the APIs)
    > from battlenet_client import wow
    > client = wow.WoWClient(<region>, release=<release>, client_id='<client ID>', client_secret='<client secret>')
    > wow.Achievement(client).achievement_category('en_US', 81)
    {'_links': {'self': {'href': 'https://us.api.blizzard.com/data/wow/achievement-category/81? ... }}}

    > # for authorization work flows (wow.Account) (requires a web server for the redirect)
    > from battlenet_client import wow
    > client = wow.WoWClient(<region>, scope=['wow.profile',], redirect_uri='https://localhost/redirect',
                             client_id='<client ID>', client_secret='<client secret>')
    # after authenticating with Blizzard.
    > wow.Account(client).account_profile_summary('en_US')

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of WoW and WoW Classic
    and any data pertaining thereto

"""
from typing import List, Optional

from battlenet_client.bnet.client import BNetClient


class WoWClient(BNetClient):
    """Defines the client workflow class for the World of Warcraft API

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
    """

    __MAJOR__ = 2
    __MINOR__ = 0
    __PATCH__ = 0

    def __init__(
        self,
        region: str,
        *,
        release: Optional[str] = "retail",
        scope: Optional[List[str]] = None,
        redirect_uri: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
    ) -> None:

        super().__init__(
            region,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
            redirect_uri=redirect_uri,
        )

        self._release = release.lower()

    @property
    def dynamic(self):
        if self._release.lower() != "retail":
            return f"dynamic-{self._release}-{self.tag}"

        return f"dynamic-{self.tag}"

    @property
    def static(self):
        if self._release.lower() != "retail":
            return f"static-{self._release}-{self.tag}"

        return f"static-{self.tag}"

    @property
    def profile(self):
        if self._release.lower() != "retail":
            return f"profile-{self._release}-{self.tag}"

        return f"profile-{self.tag}"
