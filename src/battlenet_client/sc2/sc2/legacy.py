from sc2_client.decorators import verify_client
from sc2_client.exceptions import SC2RegionError


class LegacyAPI:
    
    def __init__(self, client):
        self.client = client
    
    @verify_client
    def profile(self, locale, region_id, realm_id, profile_id):
    
        return self.client.community(locale, 'legacy', 'profile', region_id, realm_id, profile_id)
    
    @verify_client
    def ladders(self, locale, region_id, realm_id, profile_id):
    
        return self.client.community(locale, 'legacy', 'profile', region_id, realm_id, profile_id, 'ladders')
    
    @verify_client
    def match_history(self, locale, region_id, realm_id, profile_id):
    
        return self.client.community(locale, 'legacy', 'profile', region_id, realm_id, profile_id, 'matches')
    
    @verify_client
    def ladder(self, locale, region_id, ladder_id):
    
        return self.client.community(locale, 'legacy', 'ladder', region_id, ladder_id)
    

class CNLegacyAPI:

    def __init__(self, client):

        if client.tag != 'cn':
            raise SC2RegionError("Invalid region for API")

        self.client = client

    @verify_client
    def achievements(self, locale, region_id):
        return self.client.community(locale, 'legacy', 'data', 'achievements', region_id)

    @verify_client
    def rewards(self, locale, region_id):
        return self.client.community(locale, 'legacy', 'data', 'rewards', region_id)

