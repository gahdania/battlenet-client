try:
    import unittest2 as unittest
except ImportError:
    import unittest

from battlenet_client.constants import UNITED_STATES, SC2
from battlenet_client.client import BattleNetClient

from decouple import config

from src.sc2_client import SC2Client
from src.sc2_client import *
from src.sc2_client import US


class TestBaseClass(unittest.TestCase):

    def setUp(self):
        self.client = SC2Client(UNITED_STATES)

    def tearDown(self):
        self.client.close()

