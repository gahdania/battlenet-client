from functools import wraps

from wow.exceptions import WoWReleaseError, WoWClientError

MODULES = {
    'classic1x': ['connected_realm', 'creature', 'guild', 'item', 'playable_class', 'playable_race',
                  'power', 'realm', 'region', 'wow_token'],
    'classic': ['auction', 'connected_realm', 'creature', 'guild', 'item', 'media', 'playable_class',
                'playable_race', 'power', 'pvp', 'realm', 'region', 'wow_token'],
    'retail':  ['achievement', 'account', 'auction', 'azerite', 'character', 'connected_realm', 'covenant',
                'creature', 'guild', 'item', 'journal', 'media', 'modcraft', 'mount', 'mythic_plus', 'mythic_raid',
                'pet', 'playable_class', 'playable_race', 'playable_spec', 'power', 'profession', 'pvp', 'quest',
                'realm', 'region', 'reputation', 'spell', 'talent', 'tech_talent', 'title', 'wow_token']
}


def verify_client(func):
    """Verifies to see if the client if WoWClient

    Raises:
        WoWReleaseError: when the specified release does not support the API
        WoWClientError: when the wrong client is detected
    """
    @wraps(func)
    def verify_wrapper(*args, **kwargs):

        module = func.__module__.rsplit('.', -2)[-2:]

        try:
            if args[0].client.release not in MODULES:
                raise WoWReleaseError(f"Release not implemented")
        except AttributeError:
            raise WoWClientError("Invalid Client")

        if module[1] not in MODULES[args[0].client.release]:
            raise WoWReleaseError(f"API is not available for {args[0].client.release} release")

        return func(*args, **kwargs)

    return verify_wrapper
