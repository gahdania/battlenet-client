"""Defines package base Region

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of Battle.net and any data
    retrieved from this API.
"""


class Region:
    class Tag:
        """Defines the region's abbreviation (tag)"""

        #: Region abbreviation for North America
        NORTH_AMERICA = "us"

        #: Region abbreviation for North Europe
        EUROPE = "eu"

        #: Region abbreviation for Taiwan
        TAIWAN = "tw"

        #: Region abbreviation for Korea
        KOREA = "kr"

        #: Region abbreviation for China
        CHINA = "cn"
