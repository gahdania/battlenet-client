import functools
from .client import Client
from .exceptions import ClientError


def verify_client(func):
    @functools.wraps(func)
    def wrapper_client(*args, **kwargs):

        if not isinstance(args[0], Client):
            raise ClientError("Client is not an instance of WoWClient")

        return func(*args, **kwargs)

    return wrapper_client
