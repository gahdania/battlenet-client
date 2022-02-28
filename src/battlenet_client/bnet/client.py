"""Defines the base class "BNetClient"

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of Battle.net and any data
    retrieved from this API.
"""
from oic.oic import Client
from oic.utils.authn.client import CLIENT_AUTHN_METHOD
from oic.oic.message import (
    ProviderConfigurationResponse,
    RegistrationResponse,
    AuthorizationResponse,
)
from oic import rndstr
from oic.oauth2 import REQUEST2ENDPOINT
from oic.oauth2.message import CCAccessTokenRequest
from decouple import config
from urllib.parse import unquote

from typing import Optional, List

from . import exceptions, constants
from battlenet_client import utils


class BNetClient(Client):
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

    __author__ = 'David "Gahd" Couples'
    __version__ = "3.0.0"

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

        if not scope:
            REQUEST2ENDPOINT[
                "CCAccessTokenRequest"
            ] = "https://us.battle.net/oauth/token"

        super().__init__(client_id=client_id, client_authn_method=CLIENT_AUTHN_METHOD)
        self._state = rndstr()
        self._nonce = rndstr()

        op_data = {
            "version": "1.0",
            "issuer": "https://us.battle.net/oauth",
            "token_endpoint": "https://us.battle.net/oauth/token",
        }

        if scope:
            op_data.update(
                {
                    "authorization_endpoint": "https://us.battle.net/oauth/authorize",
                    "userinfo_endpoint": "https://us.battle.net/oauth/userinfo",
                }
            )

            if "openid" in scope:
                op_data.update({"jwks_uri": "https://us.battle.net/oauth/jwks/certs"})

        op_info = ProviderConfigurationResponse(**op_data)
        info = {
            "client_id": "59bdfd31c9fd40689e3d0b0a8652692c",
            "client_secret": "67twDpFpruwpMUyQ56AfYE0YVxeoa40j",
        }
        self.handle_provider_config(op_info, op_info["issuer"])
        client_reg = RegistrationResponse(**info)
        self.store_registration_info(client_reg)

        if not scope:
            args = {
                "response_type": "code",
            }

            token_r = self.do_any(
                CCAccessTokenRequest,
                request_args=args,
                endpoint="https://us.battle.net/oauth/token",
                authn_method="client_secret_basic",
            )

    def __str__(self) -> str:
        return f"{self.__class__.__name__} {self.tag.upper()} {self.version} API Client"

    @property
    def version(self):
        return f"v{self.__version__}"

    def authorization_url(self, **kwargs):
        """Prepares and returns the authorization URL to the Battle.net authorization servers

        Returns:
            str: the URL to the Battle.net authorization server
        """
        args = {
            "client_id": self.client_id,
            "response_type": "code",
            "scope": ["openid", "wow.profile"],
            "nonce": self._nonce,
            "redirect_uri": "dummy",
            "state": self._state,
        }

        auth_req = self.construct_AuthorizationRequest(request_args=args, **kwargs)
        return auth_req.request(self.authorization_endpoint)

    def authorization_response(self, response: str):
        aresp = self.parse_response(
            AuthorizationResponse, info=response, sformat="urlencoded"
        )
        assert aresp["state"] == self._state

        args = {"code": aresp["code"]}

        resp = self.do_access_token_request(
            state=aresp["state"], request_args=args, authn_method="client_secret_basic"
        )
