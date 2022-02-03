from functools import wraps

from .exceptions import WoWReleaseError, ClientError
from .constants import MODULES


def verify_client(func):
    """Verifies to see if the client if Client

    Raises:
        WoWReleaseError: when the specified release does not support the API
        ClientError: when the wrong client is detected
    """

    @wraps(func)
    def verify_wrapper(*args, **kwargs):

        module = func.__module__.rsplit(".", -2)[-2:]

        try:
            if args[0].client.release not in MODULES:
                raise WoWReleaseError(f"Release not implemented")
        except AttributeError:
            raise ClientError("Invalid Client")

        if module[1] not in MODULES[args[0].client.release]:
            raise WoWReleaseError(
                f"API is not available for {args[0].client.release} release"
            )

        return func(*args, **kwargs)

    return verify_wrapper
