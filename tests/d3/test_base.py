try:
    import unittest2 as unittest
except ImportError:
    import unittest

from battlenet_client.constants import UNITED_STATES

from src.d3_api import D3Client


class TestBaseClass(unittest.TestCase):
    def setUp(self):
        self.client = D3Client(UNITED_STATES)

    def tearDown(self):
        self.client.close()
