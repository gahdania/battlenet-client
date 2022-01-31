from sc2.decorators import verify_client
from sc2.exceptions import SC2RegionError


class LadderAPI:

    def __init__(self, client):
        self.client = client

    @verify_client
    def grandmaster(self, locale, region_id):
        return self.client.community(locale, 'ladder', 'grandmaster', region_id)

    @verify_client
    def season(self, locale, region_id):
        return self.client.community(locale, 'ladder', 'season', region_id)


class CNLadderAPI:

    def __init__(self, client):
        if client.tag != 'cn':
            raise SC2RegionError("Invalid region for API")

        self.client = client

    @verify_client
    def ladder(self, locale, profile_id):

        return self.client.community(locale, 'ladder', profile_id)

