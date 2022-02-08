"""Defines the client for connected to the World of Warcraft/Classic/TBC Classic

This module contains the client class definitions for accessing World of Warcraft API data.
There are two flavors of client, one implements the client credential workflow, which happens
to be the most common.  The other implements the user authorization workflow

Examples:
    > # for credential work flows (most of the APIs)
    > from battlenet_client import wow
    > client = wow.WoWClient(<region>, release=<release>, client_id='<client ID>', client_secret='<client secret>')
    > wow.Achievement(client).achievement_category('en_US', 81)
    {'_links': {'self': {'href': 'https://us.api.blizzard.com/data/wow/achievement-category/81? ...

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
from typing import List, Optional, Any, Dict, Union, Tuple

from io import BytesIO

from ..bnet.client import BNetClient
from ..misc import slugify

from .exceptions import WoWClientError


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

    Attributes:
        dynamic (str): the namespace to use for dynamic elements of the API (ie: characters, and guilds)
        static (str): the namespace to use for static elements of the API (ie: realms, connected_realms)
        profile (str): the namespace to use for profile based elements (ie: player info, protected char info)
    """

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

        self.release = release.lower()

        if release.lower() == "retail":
            self.dynamic = f"dynamic-{self.tag}"
            self.static = f"static-{self.tag}"
            self.profile = f"profile-{self.tag}"

        if release.lower() != "retail":
            self.dynamic = f"dynamic-{self.release}-{self.tag}"
            self.static = f"static-{self.release}-{self.tag}"
            self.profile = f"profile-{self.release}-{self.tag}"

    name = "World of Warcraft"
    abbrev = "WOW"

    def __str__(self) -> str:
        return f"{self.name} API Client"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} Instance: {self.abbrev} {self.release} {self.tag}"

    def game_data(
        self, locale: str, namespace: str, *args: Union[str, int]
    ) -> Dict[str, Any]:
        """Used to retrieve data from the source data APIs

        Args:
            locale (str): the locale to use, example: en_US
            namespace (str): namespace the API requires, example: static

        Returns:
            dict: data returned by the API
        """
        if isinstance(args[0], str) and args[0].startswith("http"):
            uri = args[0]
        else:
            uri = f"{self.api_host}/data/wow/{'/'.join([str(arg) for arg in args if arg is not None])}"

        return self._get(
            uri,
            params={"locale": locale},
            headers={"Battlenet-Namespace": getattr(self, namespace)},
        )

    def profile_data(self, locale: str, namespace: str, *args: Union[str, int]) -> Any:
        """Used to retrieve data from the profile APIs which do not require authentication from the user

        Args:
            locale (str): the locale to use, example: en_US
            namespace (str): namespace the API requires, example: static

        Returns:
            dict: data returned by the   API
        """
        if isinstance(args[0], str) and args[0].startswith("http"):
            uri = args[0]
        else:
            uri = f"{self.api_host}/profile/wow/{'/'.join([str(arg) for arg in args if arg is not None])}"

        return self._get(
            uri,
            params={"locale": locale},
            headers={"Battlenet-Namespace": getattr(self, namespace)},
        )

    def protected_data(
        self, locale: str, namespace: str, *args: Union[str, int]
    ) -> Any:
        """Used to retrieve data from the profile APIs which do require authentication from the user

        Args:
            locale (str): the locale to use, example: en_US
            namespace (str): namespace the API requires, example: static

        Returns:
            dict: data returned by the API
        """
        if not self.auth_flow:
            raise WoWClientError("Requires Authorization Workflow")

        if isinstance(args[0], str) and args[0].startswith("http"):
            uri = args[0]
        else:
            uri = f"{self.api_host}/profile/user/wow{'/'.join([str(arg) for arg in args if arg is not None])}"

        return self._post(
            uri, params={"namespace": getattr(self, namespace), "locale": locale}
        )

    def media_data(
        self, locale: str, namespace: str, *args: Union[str, int]
    ) -> Union[Dict[str, Any], BytesIO]:
        """Used to retrieve media data including URLs for them

        Args:
            locale (str): the locale to use, example: en_US
            namespace (str): namespace the API requires, example: static

        Returns:
            dict: data returned by the API
        """
        join_args = [slugify(str(arg)) for arg in args if arg is not None]
        uri = f"{self.api_host}/data/wow/media/{'/'.join(join_args)}"
        return self._get(
            uri,
            params={"locale": locale},
            headers={"Battlenet-Namespace": getattr(self, namespace)},
        )

    def search(
        self, locale: str, namespace: str, document: str, fields: List[Dict[str, Any]]
    ) -> Any:
        """Used to perform searches where available

        Args:
            locale (str): the locale to use, example: en_US
            namespace (str): namespace the API requires, example: static
            document (str): the document tree to be searched
            fields (dict): the criteria to search

        Returns:
            dict: data returned by the API
        """
        uri = f"{self.api_host}/data/wow/search/{slugify(document)}"
        return self._get(
            uri,
            params={"locale": locale},
            headers={"Battlenet-Namespace": getattr(self, namespace)},
            fields=fields,
        )

    @staticmethod
    def currency_convertor(value: int) -> Tuple[int, int, int]:
        """Returns the value into gold, silver and copper

        Args:
            value (int/str): the value to be converted

        Returns:
            tuple: gold, silver and copper values
        """
        value = int(value)

        if value < 0:
            raise ValueError("Value cannot be negative")

        return value // 10000, (value % 10000) // 100, value % 100
