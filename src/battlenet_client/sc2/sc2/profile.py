from sc2_client.decorators import verify_client
from sc2_client.exceptions import SC2RegionError


class ProfileAPI:
    
    def __init__(self, client):
        self.client = client
        
    @verify_client
    def static(self, locale, region_id):
    
        return self.client.community(locale, 'static', 'profile', region_id)
    
    @verify_client
    def metadata(self, locale, region_id, realm_id, profile_id):
    
        return self.client.community(locale, 'metadata', 'profile', region_id, realm_id, profile_id)
    
    @verify_client
    def profile(self, locale, region_id, realm_id, profile_id):
        """
    
        Args:
            locale:
            region_id:
            realm_id:
            profile_id:
    
        Returns:
    
        """
        return self.client.community(locale, 'profile', region_id, realm_id, profile_id)
    
    @verify_client
    def ladder(self, locale, region_id, realm_id, profile_id, ladder_id=None):
        if ladder_id is not None:
            return self.client.community(locale, 'profile', region_id, realm_id, profile_id, 'ladder', ladder_id)
    
        return self.client.community(locale, 'profile', region_id, realm_id, profile_id, 'ladder', 'summary')


class CNProfileAPI:

    def __init__(self, client):
        if client.tag != 'cn':
            raise SC2RegionError("Invalid region for API")

        self.client = client

    @verify_client
    def profile(self, locale, profile_id, region, name):

        if self.client.tag != 5:
            raise SC2RegionError("This API is available in this region")

        return self.client.community(locale, 'profile', profile_id, region, name)

    @verify_client
    def ladders(self, locale, profile_id, region, name):
        if self.client.tag != 5:
            raise SC2RegionError("This API is available in this region")

        return self.client.community(locale, 'profile', profile_id, region, name, 'ladders')

    @verify_client
    def match_history(self, locale, profile_id, region, name):
        if self.client.tag != 5:
            raise SC2RegionError("This API is available in this region")

        return self.client.community(locale, 'profile', profile_id, region, name, 'matches')
