try:
    import unittest2 as unittest
except ImportError:
    import unittest

from battlenet_client.bnet.constants import UNITED_STATES

from src.sc2_client import SC2Client
from src.sc2_client import *


class TestBaseClass(unittest.TestCase):
    def setUp(self):
        self.client = SC2Client(UNITED_STATES)

    def tearDown(self):
        self.client.close()
