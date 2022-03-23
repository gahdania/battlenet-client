import pytest
from battlenet_client.wow import utils
from battlenet_client.exceptions import BNetValueError


@pytest.mark.parametrize(('api_type', 'release', 'expected'),
                         [('static', 'retail', 'static-us'),
                          ('dynamic', 'retail', 'dynamic-us'),
                          ('profile', 'retail', 'profile-us'),
                          ('static', 'classic1x', 'static-classic1x-us'),
                          ('dynamic', 'classic1x', 'dynamic-classic1x-us'),
                          ('profile', 'classic1x', 'profile-classic1x-us'),
                          ('static', 'classic', 'static-classic-us'),
                          ('dynamic', 'classic', 'dynamic-classic-us'),
                          ('profile', 'classic', 'profile-classic-us')])
def test_namespace_valid_params(api_type, release, expected):
    data = utils.namespace('us', api_type, release)
    assert data == expected


@pytest.mark.parametrize(('api_type', 'release', 'region'),
                         [('flat', 'retail', 'us'),
                          ('square', 'retail', 'us'),
                          ('circle', 'retail', 'us'),
                          ('static', 'classic-x', 'us'),
                          ('dynamic', 'classic-x', 'us'),
                          ('profile', 'classic-x', 'us')])
def test_namespace_invalid_api_type_or_release(api_type, release, region):
    with pytest.raises(BNetValueError):
        utils.namespace(region, api_type, release)
