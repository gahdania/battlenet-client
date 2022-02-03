import functools
from .client import SC2Client
from .exceptions import SC2ClientError


def verify_client(func):
    @functools.wraps(func)
    def wrapper_client(*args, **kwargs):

        if not isinstance(args[0], SC2Client):
            raise SC2ClientError("Client is not an instance of WoWClient")

        args = [arg.lower() if isinstance(arg, str) else arg for arg in args]

        return func(*args, **kwargs)

    return wrapper_client
