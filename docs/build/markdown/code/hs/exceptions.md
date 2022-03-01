# Exceptions

Defines exceptions related to the Diablo III API wrappers

Disclaimer:

    All rights reserved, Blizzard is the intellectual property owner of Diablo III and any data
    retrieved from this API.


### exception battlenet_client.hs.exceptions.HSClientError()
Exception used when using the wrong client, ie using Hearthstone’s
client with the HS APIs, or when using the client credential workflow
instead of the authorization workflow for certain APIs


### exception battlenet_client.hs.exceptions.HSError()
Base Exception for the HS API Wrappers


### exception battlenet_client.hs.exceptions.HSReleaseError()
Exception used when the release does not work with an API
