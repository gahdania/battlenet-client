"""Defines the base class "BNetClient"

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of Battle.net and any data
    retrieved from this API.
"""
from requests import Response
from requests.exceptions import HTTPError
from time import sleep
from decouple import config
from urllib.parse import unquote
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from typing import Optional, List

from . import exceptions, constants
from battlenet_client import utils


class BNetClient(OAuth2Session):
    """Handles the communication using OAuth v2 client to the Battle.net REST API

    Args:
        region (str): region abbreviation for use with the APIs

    Keyword Args:
        client_id (str): the client ID from the developer portal
        client_secret (str): the client secret from the developer portal
        scope (list, optional): the scope or scopes to use during the endpoints that require the Web Application Flow
        redirect_uri (str, optional): the URI to return after a successful authentication between the user and Blizzard

    Attributes:
        tag (str): the region tag (abbreviation) of the client
    """

    __MAJOR__ = 2
    __MINOR__ = 1
    __PATCH__ = 1

    def __init__(
        self,
        region: str,
        *,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        scope: Optional[List[str]] = None,
        redirect_uri: Optional[str] = None,
    ) -> None:

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

        if redirect_uri and scope:
            super().__init__(
                client_id=client_id, scope=scope, redirect_uri=redirect_uri
            )
        else:
            super().__init__(client=BackendApplicationClient(client_id=client_id))
            self.fetch_token(
                token_url=f"{utils.auth_host(self.tag)}/oauth/token",
                client_id=client_id,
                client_secret=client_secret,
            )

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.tag.upper()} {self.version} API Client"

    def __repr__(self) -> str:
        return f"{self.__str__()} ({'Auth Code Flow' if self.auth_code else 'Credential Client Flow'})"

    @property
    def auth_code(self):
        return self._client.grant_type == "authorization_code"

    @property
    def version(self):
        return f"v{self.__MAJOR__}.{self.__MINOR__}.{self.__PATCH__}"

    def validate_token(self) -> bool:
        """Checks with the API if the token is good or not.

        Returns:
            bool: True of the token is valid, false otherwise.
        """

        url = f"{utils.auth_host(self.tag)}/oauth/check_token"
        retry = 0
        while retry < 5:
            try:
                data = self.post(
                    url,
                    params={"token": self._client.access_token},
                    headers={"Battlenet-Namespace": None},
                )
                data.raise_for_status()
            except HTTPError as err:
                if err.response.status_cod == 429:
                    sleep(1)
                    retry += 1
            else:
                return (
                    data.status_code == 200
                    and data.json()["client_id"] == self.client_id
                )

    def authorization_url(self, **kwargs) -> str:
        """Prepares and returns the authorization URL to the Battle.net authorization servers

        Returns:
            str: the URL to the Battle.net authorization server
        """
        if not self.auth_flow:
            raise ValueError("Requires Authorization Workflow")

        authorization_url, self._client.state = super().authorization_url(
            url=f"{utils.auth_host(self.tag)}/oauth/authorize", **kwargs
        )
        return unquote(authorization_url)
