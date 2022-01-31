import pytest

from wow.constants import CLASSIC, TBC_CLASSIC
from wow import WoWReleaseError
from wow import ItemAPI
from wow import AccountAPI
from wow import CharacterAPI


@pytest.mark.usefixtures("cred_client")
class TestClient:

    @pytest.mark.era(CLASSIC)
    class TestClassic:
        @pytest.mark.parametrize("equals,attr,value", [
            (False, 'release', 'retail'),
            (False, 'static', 'static-us'),
            (False, 'dynamic', 'dynamic-us'),
            (False, 'profile', 'profile-us'),
            (False, 'release', 'classic'),
            (False, 'static', 'static-classic-us'),
            (False, 'dynamic', 'dynamic-classic-us'),
            (False, 'profile', 'profile-classic-us'),
            (True, 'release',  'classic1x'),
            (True, 'static', 'static-classic1x-us'),
            (True, 'dynamic', 'dynamic-classic1x-us'),
            (True, 'profile', 'profile-classic1x-us'),
        ])
        def test_client(self, cred_client, equals, attr, value):
            if equals:
                assert(getattr(cred_client, attr) == value)
            else:
                assert(getattr(cred_client, attr) != value)
    
        def test_get_data(self, cred_client):
            data = ItemAPI(cred_client).item('enus', 19019)
            assert(isinstance(data, dict))
            assert('id' in data)
            assert(data['id'] == 19019)
    
        def test_media(self, cred_client):
            data = ItemAPI(cred_client).item_media('enus', 19019)
            assert(isinstance(data, dict))
            assert('assets' in data)
            assert(isinstance(data['assets'], list))
    
        def test_search(self, cred_client):
            fields = {'name.en_US': 'Thunderfury', 'orderby': 'name', '_page': 1}
            data = ItemAPI(cred_client).item_search('enus',  fields)
            assert(isinstance(data, dict))
            assert('results' in data)
            assert(isinstance(data['results'], list))

        @pytest.mark.usefixtures("oauth_client")
        @pytest.mark.skip(reason='Automated Testing using Oauth not implemented')
        def test_protected_data(self, oauth_client):
            with pytest.raises(WoWReleaseError):
                AccountAPI(oauth_client).account_profile_summary('enus')
                    
        def test_profile(self, cred_client):
            with pytest.raises(WoWReleaseError):
                CharacterAPI(cred_client).profile('enus', 'baelgun', 'Gahdania')

    @pytest.mark.era(TBC_CLASSIC)
    class TestTBC:
        @pytest.mark.parametrize("equals,attr,value", [
            (False, 'release', 'retail'),
            (False, 'static', 'static-us'),
            (False, 'dynamic', 'dynamic-us'),
            (False, 'profile', 'profile-us'),
            (True, 'release', 'classic'),
            (True, 'static', 'static-classic-us'),
            (True, 'dynamic', 'dynamic-classic-us'),
            (True, 'profile', 'profile-classic-us'),
            (False, 'release',  'classic1x'),
            (False, 'static', 'static-classic1x-us'),
            (False, 'dynamic', 'dynamic-classic1x-us'),
            (False, 'profile', 'profile-classic1x-us'),
        ])
        def test_client(self, cred_client, equals, attr, value):
            if equals:
                assert(getattr(cred_client, attr) == value)
            else:
                assert(getattr(cred_client, attr) != value)

        def test_game_data(self, cred_client):
            data = ItemAPI(cred_client).item('enus', 19019)
            assert(isinstance(data, dict))
            assert('id' in data)
            assert(data['id'] == 19019)

        def test_media(self, cred_client):
            data = ItemAPI(cred_client).item_media('enus', 19019)
            assert(isinstance(data, dict))
            assert('assets' in data)
            assert(isinstance(data['assets'], list))

        def test_search(self, cred_client):
            fields = {'name.en_US': 'Thunderfury', 'orderby': 'name', '_page': 1}
            data = ItemAPI(cred_client).item_search('enus',  fields)
            assert(isinstance(data, dict))
            assert('results' in data)
            assert(isinstance(data['results'], list))

        @pytest.mark.usefixtures("oauth_client")
        @pytest.mark.skip(reason='Automated Testing using Oauth not implemented')
        def test_protected_data(self, oauth_client):
            with pytest.raises(WoWReleaseError):
                AccountAPI(oauth_client).account_profile_summary('enus')

        def test_profile(self, cred_client):
            with pytest.raises(WoWReleaseError):
                CharacterAPI(cred_client).profile('enus', 'baelgun', 'Gahdania')

    class TestRetail:
        @pytest.mark.parametrize("equals,attr,value", [
            (True, 'release', 'retail'),
            (True, 'static', 'static-us'),
            (True, 'dynamic', 'dynamic-us'),
            (True, 'profile', 'profile-us'),
            (False, 'release', 'classic'),
            (False, 'static', 'static-classic-us'),
            (False, 'dynamic', 'dynamic-classic-us'),
            (False, 'profile', 'profile-classic-us'),
            (False, 'release',  'classic1x'),
            (False, 'static', 'static-classic1x-us'),
            (False, 'dynamic', 'dynamic-classic1x-us'),
            (False, 'profile', 'profile-classic1x-us'),
        ])
        def test_client(self, cred_client, equals, attr, value):
            if equals:
                assert(getattr(cred_client, attr) == value)
            else:
                assert(getattr(cred_client, attr) != value)

        def test_game_data(self, cred_client):
            data = ItemAPI(cred_client).item('enus', 19019)
            assert(isinstance(data, dict))
            assert('id' in data)
            assert(data['id'] == 19019)

        def test_media(self, cred_client):
            data = ItemAPI(cred_client).item_media('enus', 19019)
            assert (isinstance(data, dict))
            assert ('assets' in data)
            assert (isinstance(data['assets'], list))

        def test_search(self, cred_client):
            fields = {'name.en_US': 'Thunderfury', 'orderby': 'name', '_page': 1}
            data = ItemAPI(cred_client).item_search('enus',  fields)
            assert(isinstance(data, dict))
            assert('results' in data)
            assert(isinstance(data['results'], list))

        @pytest.mark.usefixtures("oauth_client")
        @pytest.mark.skip(reason='Automated Testing using Oauth not implemented')
        def test_protected_data(self, oauth_client):
            data = AccountAPI(oauth_client).account_profile_summary('enus')
            assert('id' in data)
            assert('wow_accounts' in data)
            assert(isinstance(data['wow_accounts'], list))

        def test_profile(self, cred_client):
            data = CharacterAPI(cred_client).profile('enus', 'baelgun', 'Gahdania')
            assert(isinstance(data, dict))
            assert('id' in data)
            assert('name' in data)
            assert('faction' in data)
            assert('race' in data)
