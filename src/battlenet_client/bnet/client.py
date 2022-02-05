"""Generates the final Battle.net REST API requests


Classes:
    BNetClient
"""
import importlib
from typing import Optional, Any, Dict, Tuple, List, Union

from decouple import config
from io import BytesIO
from time import sleep
from urllib.parse import unquote

import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

from .. import constants
from . import exceptions


class BNetClient(OAuth2Session):
    """Handles the communication using OAuth v2 client to the Battle.net REST API

    Args:
        region (str): region abbreviation for use with the APIs
        game (dict): the game for the request

    Keyword Args:
        client_id (str): the client ID from the developer portal
        client_secret (str): the client secret from the developer portal
        scope (list, optional): the scope or scopes to use during the endpoints that require the Web Application Flow
        redirect_uri (str, optional): the URI to return after a successful authentication between the user and Blizzard

    Attributes:
        tag (str): the region tag (abbreviation) of the client
        api_host (str): the host to use for accessing the API endpoints
        auth_host (str): the host to use for authentication
        render_host (str): the hose to use for images
        game (dict): holds basic info about the game
    """

    def __init__(
        self,
        region: str,
        game: Dict[str, str],
        *,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        scope: Optional[List[str]] = None,
        redirect_uri: Optional[str] = None,
    ) -> None:

        self._state = None

        if not client_id:
            client_id = config("CLIENT_ID")

        if not client_secret:
            client_secret = config("CLIENT_SECRET")

        try:
            self.tag = getattr(constants, region)
        except AttributeError:
            if region.strip().lower() in ("us", "eu", "kr", "tw", "cn"):
                self.tag = region.strip().lower()
            else:
                raise exceptions.BNetRegionNotFoundError("Region not available")

        self.game = game

        self._client_secret = client_secret

        if self.tag == "cn":
            self.api_host = "https://gateway.battlenet.com.cn"
            self.auth_host = "https://www.battlenet.com.cn"
            self.render_host = "https://render.worldofwarcraft.com.cn"
        elif self.tag in ("kr", "tw"):
            self.api_host = f"https://{self.tag}.api.blizzard.com"
            self.auth_host = "https://apac.battle.net"
            self.render_host = f"https://render-{self.tag}.worldofwarcraft.com"
        else:
            self.api_host = f"https://{self.tag}.api.blizzard.com"
            self.auth_host = f"https://{self.tag}.battle.net"
            self.render_host = f"https://render-{self.tag}.worldofwarcraft.com"

        if redirect_uri and scope:
            self.auth_flow = True
            super().__init__(
                client_id=client_id, scope=scope, redirect_uri=redirect_uri
            )

            mod = importlib.import_module("battlenet_client.oauth")
            if self.tag == "cn":
                setattr(
                    self,
                    getattr(mod, "BNetOauthCN").__class__name__,
                    getattr(mod, "BNetOauthCN")(self),
                )
            else:
                setattr(
                    self,
                    getattr(mod, "BNetOauth").__class__name,
                    getattr(mod, "BNetOauth")(self),
                )

        else:
            super().__init__(client=BackendApplicationClient(client_id=client_id))
            # set the mode indicator of the client to "Backend Application Flow"
            self.fetch_token()
            self.auth_flow = False

    def __str__(self) -> str:
        return f"{self.game['name']} API Client"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} Instance: {self.game['abbrev']}"

    def _get(self, uri: str, **kwargs) -> Dict[str, Any]:
        """Convenience function for the GET method

        Args:
            uri (str): the URI to request

        Keyword Args:
            params (dict): query string parameters for the API
            headers (dict, optional): the headers to add to the request
            fields (dict, optional): the fields and values for searches

        Returns:
              dict:  The response from the Battle.net API
        """
        return self.__endpoint("get", uri, **kwargs)

    def _post(self, uri: str, **kwargs) -> Dict[str, Any]:
        """Convenience function for the POST method

        Args:
            uri (str): the URI to request

        Keyword Args:
            params (dict): query string parameters for the API
            headers (dict, optional): the headers to add to the request
            fields (dict, optional): the fields and values for searches

        Returns:
              dict:  The response from the Battle.net API
        """
        return self.__endpoint("post", uri, **kwargs)

    def __endpoint(
        self,
        method: str,
        uri: str,
        *,
        retries: Optional[int] = 5,
        params: Dict[str, Any] = None,
        headers: Optional[Dict[str, Any]] = None,
        fields: Optional[Dict[str, Any]] = None,
    ) -> Union[Dict[str, Any], BytesIO]:
        """Processes the API request into the appropriate headers and parameters

        Args:
            method (str): the HTTP method to use
            uri (str): the URI for the API endpoint

        Keyword Args:
            retries (int, optional): the number of retries at getting to the API endpoint (default is 5)
            params (dict): dict of the parameters to be passed via query string to the endpoint
            headers (dict, optional):  Additional headers to sent with the request
            fields (dict, optional): search parameters to form

        Returns:
          dict:  The response from the Battle.net API
        """

        if not params:
            params = {}

        if fields:
            params.update({key: value for key, value in fields.items()})

        for _ in range(retries):
            try:
                raw_data = super().request(method, uri, params=params, headers=headers)
                raw_data.raise_for_status()
            except requests.exceptions.Timeout:
                sleep(2.5)
            except requests.exceptions.HTTPError as error:
                if error.response.status_code == 429:
                    sleep(1.0)
                else:
                    raise error
            else:
                if raw_data.headers["content-type"].startswith("application/json"):
                    return raw_data.json()
                else:
                    return BytesIO(raw_data.content)

    def validate_token(self) -> bool:
        """Checks with the API if the token is good or not.

        Returns:
            bool: True of the token is valid, false otherwise.
        """

        url = f"{self.auth_host}/oauth/check_token"
        data = super().post(
            url,
            params={"token": self.access_token},
            headers={"Battlenet-Namespace": None},
        )
        result: bool = (
            data.status_code == 200 and data.json()["client_id"] == self.client_id
        )
        return result

    def authorization_url(self, **kwargs) -> str:
        """Prepares and returns the authorization URL to the Battle.net authorization servers

        Returns:
            str: the URL to the Battle.net authorization server
        """
        if not self.auth_flow:
            raise ValueError("Requires Authorization Workflow")

        auth_url = f"{self.auth_host}/oauth/authorize"
        authorization_url, self._state = super().authorization_url(
            url=auth_url, **kwargs
        )
        return unquote(authorization_url)

    def fetch_token(self, **kwargs) -> None:
        """Retrieves the OAUTH token from API

        Returns:
            None
        """
        token_url = f"{self.auth_host}/oauth/token"
        super().fetch_token(
            token_url=token_url,
            client_id=self.client_id,
            client_secret=self._client_secret,
            **kwargs,
        )
