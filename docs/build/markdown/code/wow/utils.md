# Utility Functions

Miscellaneous functions to support for World of Warcraft

Functions:

    namespace(api_type, release, region)

Misc Variables:

    __version__
    __author__

Author: David “Gahd” Couples
License: GPL v3
Copyright: February 24, 2022


### battlenet_client.wow.utils.namespace(region: str, api_type: str, release: str)
Returns the namespace required by the WoW API endpoint


* **Returns**

    the namespace string



* **Return type**

    str



* **Raises**

    **BNetValueError** – when api type is not of static, dynamic or profile, or an invalid release
