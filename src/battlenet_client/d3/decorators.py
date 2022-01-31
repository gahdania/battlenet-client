import functools
from .client import D3Client
from .exceptions import D3ClientError


def verify_client(func):
    @functools.wraps(func)
    def wrapper_client(*args, **kwargs):

        if not isinstance(args[0], D3Client):
            raise D3ClientError("Client is not an instance of WoWClient")

        return func(*args, **kwargs)
    return wrapper_client
