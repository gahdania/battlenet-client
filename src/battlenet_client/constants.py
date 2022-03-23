"""Defines the generic Region

Classes:
    Region

Misc Variables:
    __version__
    __author__

Author: David "Gahd" Couples
License: GPL v3
Copyright: February 24, 2022
"""

__version__ = '1.0.0'
__author__ = 'David \'Gahd\' Couples'


class Region:

    class Tag:
        """Defines the region's abbreviation (tag)"""

        #: Region abbreviation for North America
        NORTH_AMERICA = 'us'

        #: Region abbreviation for North Europe
        EUROPE = 'eu'

        #: Region abbreviation for Taiwan
        TAIWAN = 'tw'

        #: Region abbreviation for Korea
        KOREA = 'kr'

        #: Region abbreviation for China
        CHINA = 'cn'

    class Id:
        """Defines the Region IDs for Diablo III, Starcraft 2, and Hearthstone"""

        #: Region ID for North America
        NORTH_AMERICA = 1

        #: Region ID for Europe
        EUROPE = 2

        #: Region ID for Korea and Taiwan (APAC)
        APAC = 3

        #: Region ID for China
        CHINA = 5
