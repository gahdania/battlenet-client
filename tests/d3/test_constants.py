from battlenet_client.d3.constants import Region
from battlenet_client.constants import Region as BaseRegion


def test_region_class():
    assert issubclass(Region, BaseRegion)
