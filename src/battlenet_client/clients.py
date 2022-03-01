"""Defines the base class "BNetClient"

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of Battle.net and any data
    retrieved from this API.
"""

from oic.oic import Client
from oic.utils.authn.client import CLIENT_AUTHN_METHOD
from oic.oic.message import (
    RegistrationResponse,
    AuthorizationResponse,
)
from oic import rndstr
from oic.oauth2 import REQUEST2ENDPOINT
from oic.oauth2.message import ASConfigurationResponse
from decouple import config

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


from typing import Optional, List

from battlenet_client.bnet import (
    exceptions as bnet_exceptions,
    constants as bnet_constants,
)
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
            self.tag = getattr(bnet_constants, region)
        except AttributeError:
            if region.strip().lower() in ("us", "eu", "kr", "tw", "cn"):
                self.tag = region.strip().lower()
            else:
                raise bnet_exceptions.BNetRegionNotFoundError("Region not available")

        if not scope:
            REQUEST2ENDPOINT[
                "CCAccessTokenRequest"
            ] = f"{utils.auth_host(region)}oauth/token"

        super().__init__(client_id=client_id, client_authn_method=CLIENT_AUTHN_METHOD)
        self._state = rndstr()
        self._nonce = rndstr()

        op_data = {
            "version": "3.0",
            "issuer": f"{utils.auth_host(region)}/oauth",
            "token_endpoint": f"{utils.auth_host(region)}/oauth/token",
            "redirect_uri": redirect_uri,
        }

        if scope:
            op_data.update(
                {
                    "authorization_endpoint": f"{utils.auth_host(region)}/oauth/authorize",
                    "userinfo_endpoint": f"{utils.auth_host(region)}/oauth/userinfo",
                }
            )

            if "openid" in scope:
                op_data.update(
                    {"jwks_uri": f"{utils.auth_host(region)}/oauth/jwks/certs"}
                )

        op_info = ASConfigurationResponse(**op_data)
        info = {
            "client_id": client_id,
            "client_secret": client_secret,
        }
        self.handle_provider_config(op_info, op_info["issuer"])
        client_reg = RegistrationResponse(**info)
        self.store_registration_info(client_reg)

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
            "redirect_uri": self.registration_response["redirect_uris"][0],
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

        self.do_access_token_request(
            state=aresp["state"], request_args=args, authn_method="client_secret_basic"
        )

    def get(self, uri, **kwargs):
        return self.fetch_protected_resource(uri, "GET", **kwargs)

    def post(self, uri, **kwargs):
        return self.fetch_protected_resource(uri, "POST", **kwargs)


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

    __MAJOR__ = 1
    __MINOR__ = 0
    __PATCH__ = 0

    def __init__(
        self,
        region: str,
        *,
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


class HSClient(BNetClient):
    """Defines the client workflow class for HearthStone

    Args:
        region (str): region abbreviation for use with the APIs

    Keyword Args:
        client_id (str, optional): the client ID from the developer portal
        client_secret (str, optional): the client secret from the developer portal
    """

    __MAJOR__ = 1
    __MINOR__ = 0
    __PATCH__ = 0

    def __init__(
        self,
        region: str,
        *,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
    ):
        super().__init__(region, client_id=client_id, client_secret=client_secret)


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

    __MAJOR__ = 1
    __MINOR__ = 0
    __PATCH__ = 0

    def __init__(
        self,
        region: str,
        *,
        scope: Optional[List[str]] = None,
        redirect_uri: Optional[str] = None,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
    ):
        super().__init__(
            region,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
            redirect_uri=redirect_uri,
        )


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


class CredentialClient(OAuth2Session):
    """Handles the API endpoints that do not require Authorization Code Flow

    Args:
        region (str): region abbreviation for use with the APIs

    Keyword Args:
        client_id (str): the client ID from the developer portal
        client_secret (str): the client secret from the developer portal

    Attributes:
        tag (str): the region tag (abbreviation) of the client
        api_host (str): the host to use for accessing the API endpoints
        auth_host (str): the host to use for authentication
        render_host (str): the hose to use for images
    """

    __author__ = 'David "Gahd" Couples'
    __version__ = "2.1.0"

    def __init__(
        self,
        region: str,
        *,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
    ) -> None:

        self._state = None

        if not client_id:
            client_id = config("CLIENT_ID")

        if not client_secret:
            client_secret = config("CLIENT_SECRET")

        try:
            self.tag = getattr(bnet_constants, region)
        except AttributeError:
            if region.strip().lower() in ("us", "eu", "kr", "tw", "cn"):
                self.tag = region.strip().lower()
            else:
                raise bnet_exceptions.BNetRegionNotFoundError("Region not available")

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

        super().__init__(client=BackendApplicationClient(client_id=client_id))
        self.fetch_token(
            token_url=f"{self.auth_host}/oauth/token",
            client_id=client_id,
            client_secret=client_secret,
        )

    def __str__(self) -> str:
        return f"{self.__class__.__name__} Credential Client Code Flow "

    def __repr__(self) -> str:
        return self.__str__()
