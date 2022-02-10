from src.sc2_client import league_data
from .test_base import *


class TestLeagueData(TestBaseClass):
    def test_league(self):
        data = league_data(self.client, "enus", 37, 201, 0, 6)
        self.assertIsInstance(data, dict)
        self.assertIn("key", data)
        self.assertIsInstance(data["key"], dict)
        self.assertIn("tier", data)
        self.assertIsInstance(data["tier"], list)
