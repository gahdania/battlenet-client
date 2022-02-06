"""Defines the client for connected to the Diablo III API

Examples:
    > from battlenet_client import d3
    > client = d3.D3Client(<region>, client_id='<client ID>', client_secret='<client secret>')

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of Diablo III and any data
    retrieved from this API.
"""
from typing import List, Optional, Any, Dict
import importlib
from decouple import config

from battlenet_client.bnet.client import BNetClient
from battlenet_client.constants import D3

from ..misc import localize


class D3Client(BNetClient):
    """Defines the client workflow class for Diablo III

    Args:
        region (str): region abbreviation for use with the s

    Keyword Args:
        scope (list of str, optional): the scope or scopes to use during the data that require the
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
    ) -> None:

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

        mod = importlib.import_module(f"battlenet_client.d3.community")
        if self.tag == "cn":
            setattr(
                self,
                getattr(mod, "CommunityCN").class_name,
                getattr(mod, "CommunityCN")(self),
            )
        else:
            setattr(
                self,
                getattr(mod, "Community").class_name,
                getattr(mod, "Community")(self),
            )

        mod = importlib.import_module(f"battlenet_client.d3.game_data")
        for cls_name in dir(mod):
            if not cls_name.startswith("__") and isinstance(
                getattr(mod, cls_name), type
            ):
                setattr(
                    self,
                    getattr(mod, cls_name).class_name,
                    getattr(mod, cls_name)(self),
                )

    def game_data(self, locale: str, *args, **kwargs) -> Dict[str, Any]:
        """Generates then necessary game data API URI and keyword args for to pasted on to the client get method

        Args:
            locale (str): the localization to use for the request

        Returns:
            dict: the resultant JSON decoded dict
        """
        if args[0].startswith("https"):
            uri = args[0]
        else:
            uri = f"{self.api_host}/data/d3/{'/'.join([str(arg) for arg in args if arg is not None])}"

        kwargs["params"]["locale"] = localize(locale)

        return self._get(uri, **kwargs)

    def community(self, locale: str, *args, **kwargs) -> Dict[str, Any]:
        """Generates then necessary community API URI and keyword args for to pasted on to the client get method

        Args:
            locale (str): the localization to use for the request

        Returns:
            dict: the resultant JSON decoded dict
        """
        if args[0].startswith("https"):
            uri = args[0]
        else:
            uri = f"{self.api_host}/d3/data/{'/'.join([str(arg) for arg in args if arg is not None])}"
        kwargs["params"]["locale"] = localize(locale)
        return self._get(uri, **kwargs)

    def profile_api(self, locale: str, *args, **kwargs) -> Dict[str, Any]:
        """Generates then necessary profile API URI and keyword args for to pasted on to the client get method

        Args:
            locale (str): the localization to use for the request

        Returns:
            dict: the resultant JSON decoded dict
        """
        if args[0].startswith("https"):
            uri = args[0]
        else:
            uri = f"{self.api_host}/d3/profile/{'/'.join([str(arg) for arg in args if arg is not None])}"

        kwargs["params"]["locale"] = localize(locale)
        return self._get(uri, **kwargs)
