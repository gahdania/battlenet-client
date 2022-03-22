from battlenet_client.hs.constants import Region
from battlenet_client.constants import Region as BaseRegion


def test_region_class():
    assert issubclass(Region, BaseRegion)
