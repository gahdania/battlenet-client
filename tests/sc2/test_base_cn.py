try:
    import unittest2 as unittest
except ImportError:
    import unittest

from battlenet_client.constants import CHINA

from src.sc2_client import SC2Client
from src.sc2_client import *


class TestBaseClass(unittest.TestCase):
    def setUp(self):
        self.client = SC2Client(CHINA)

    def tearDown(self):
        self.client.close()
