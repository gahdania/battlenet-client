import pytest

from battlenet_client.constants import Region


@pytest.mark.parametrize('attribute, value', (
        ('NORTH_AMERICA', 'us'),
        ('TAIWAN', 'tw'),
        ('EUROPE', 'eu'),
        ('KOREA', 'kr'),
        ('CHINA', 'cn'))
)
def test_region_tag(attribute, value):
    assert getattr(Region.Tag, attribute) == value
