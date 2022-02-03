from src.d3_api import season, season_leaderboard, era, era_leaderboard
from src.d3_api import (
    act,
    artisan,
    recipe,
    follower,
    character_class,
    api_skill,
    item_type,
    item,
)
from src.d3_api import api_account, api_hero, api_hero_items, api_follower_items
from tests.test_base import *


class TestGameData(TestBaseClass):
    def test_season_index(self):
        data = season(self.client, "enus")
        self.assertIsInstance(data, dict)
        self.assertIn("season", data)
        self.assertIsInstance(data["season"], list)
        self.assertGreater(len(data["season"]), 0)

    def test_season(self):
        data = season(self.client, "enus", 1)
        self.assertIsInstance(data, dict)
        self.assertIn("leaderboard", data)
        self.assertIsInstance(data["leaderboard"], list)
        self.assertGreater(len(data["leaderboard"]), 0)
        self.assertIn("season_id", data)
        self.assertEqual(data["season_id"], 1)
        self.assertIn("last_update_time", data)
        self.assertIn("generated_by", data)

    def test_season_leaderboard(self):
        data = season_leaderboard(self.client, "enus", 1, "achievement-points")
        self.assertIsInstance(data, dict)
        self.assertIn("row", data)
        self.assertIsInstance(data["row"], list)
        self.assertGreater(len(data["row"]), 0)

    def test_era_index(self):
        data = era(self.client, "enus")
        self.assertIsInstance(data, dict)
        self.assertIn("era", data)
        self.assertIsInstance(data["era"], list)
        self.assertGreater(len(data["era"]), 0)

    def test_era(self):
        data = era(self.client, "enus", 1)
        self.assertIsInstance(data, dict)
        self.assertIn("leaderboard", data)
        self.assertIsInstance(data["leaderboard"], list)
        self.assertGreater(len(data["leaderboard"]), 0)
        self.assertIn("era_id", data)
        self.assertEqual(data["era_id"], 1)
        self.assertIn("era_start_date", data)
        self.assertGreater(data["era_start_date"], 0)
        self.assertIn("last_update_time", data)
        self.assertIn("generated_by", data)

    def test_era_leaderboard(self):
        data = era_leaderboard(self.client, "enus", 1, "rift-barbarian")
        self.assertIsInstance(data, dict)
        self.assertIn("row", data)
        self.assertIsInstance(data["row"], list)
        self.assertGreater(len(data["row"]), 0)


class TestCommunity(TestBaseClass):
    def test_act_index(self):
        data = act(self.client, "enus")
        self.assertIsInstance(data, dict)
        self.assertIn("acts", data)

    def test_act(self):
        data = act(self.client, "enus", 1)
        self.assertIsInstance(data, dict)
        self.assertIn("slug", data)
        self.assertEqual(data["slug"], "act-i")
        self.assertIn("number", data)
        self.assertEqual(data["number"], 1)
        self.assertIn("quests", data)
        self.assertIsInstance(data["quests"], list)

    def test_artisan(self):
        data = artisan(self.client, "enus", "blacksmith")
        self.assertIsInstance(data, dict)
        self.assertIn("slug", data)
        self.assertIn("name", data)
        self.assertIn("portrait", data)
        self.assertIn("training", data)
        self.assertIsInstance(data["training"], dict)

    def test_recipe(self):
        data = recipe(self.client, "enus", "blacksmith", "apprentice-flamberge")
        self.assertIsInstance(data, dict)
        self.assertIn("id", data)
        self.assertEqual(data["id"], "Sword_2H_003")
        self.assertIn("slug", data)
        self.assertIn("name", data)
        self.assertIn("cost", data)
        self.assertIn("reagents", data)

    def test_follower(self):
        data = follower(self.client, "enus", "templar")
        self.assertIsInstance(data, dict)
        self.assertIn("slug", data)
        self.assertEqual(data["slug"], "templar")
        self.assertIn("name", data)
        self.assertEqual(data["name"], "Templar")
        self.assertIn("realName", data)
        self.assertEqual(data["realName"], "Kormac")
        self.assertIn("portrait", data)
        self.assertIn("skills", data)
        self.assertIsInstance(data["skills"], list)

    def test_character_class(self):
        data = character_class(self.client, "enus", "barbarian")
        self.assertIsInstance(data, dict)
        self.assertIn("slug", data)
        self.assertEqual(data["slug"], "barbarian")
        self.assertIn("name", data)
        self.assertEqual(data["name"], "Barbarian")
        self.assertIn("icon", data)
        self.assertIn("skillCategories", data)
        self.assertIsInstance(data["skillCategories"], list)
        self.assertIn("skills", data)
        self.assertIsInstance(data["skills"], dict)

    def test_api_skill(self):
        data = api_skill(self.client, "enus", "barbarian", "bash")
        self.assertIsInstance(data, dict)
        self.assertIn("skill", data)
        self.assertIn("runes", data)

    def test_item_type_index(self):
        data = item_type(self.client, "enus")
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_item_type(self):
        data = item_type(self.client, "enus", "sword2h")
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

    def test_item(self):
        data = item(self.client, "enus", "corrupted-ashbringer-Unique_Sword_2H_104_x1")
        self.assertIsInstance(data, dict)
        self.assertEqual(data["id"], "Unique_Sword_2H_104_x1")
        self.assertEqual(data["slug"], "corrupted-ashbringer")
        self.assertEqual(data["name"], "Corrupted Ashbringer")

    def test_api_account(self):
        data = api_account(self.client, "enus", "Gahd#11691")
        self.assertIsInstance(data, dict)
        self.assertIn("battleTag", data)
        self.assertEqual(data["battleTag"], "Gahd#11691")
        self.assertIn("paragonLevel", data)
        self.assertGreater(data["paragonLevel"], 0)
        self.assertIn("heroes", data)
        self.assertIsInstance(data["heroes"], list)

    def test_api_hero(self):
        data = api_hero(self.client, "enus", "Gahd#11691", 135259470)
        self.assertIsInstance(data, dict)
        self.assertIn("id", data)
        self.assertEqual(data["id"], 135259470)
        self.assertIn("name", data)
        self.assertEqual(data["name"], "Gahdania")
        self.assertIn("class", data)
        self.assertEqual(data["class"], "witch-doctor")
        self.assertIn("skills", data)

    def test_api_hero_items(self):
        data = api_hero_items(self.client, "enus", "Gahd#11691", 135259470)
        self.assertIsInstance(data, dict)
        self.assertIn("head", data)
        self.assertIn("neck", data)
        self.assertIn("torso", data)
        self.assertIn("shoulders", data)
        self.assertIn("legs", data)
        self.assertIn("waist", data)
        self.assertIn("hands", data)
        self.assertIn("bracers", data)
        self.assertIn("feet", data)
        self.assertIn("leftFinger", data)
        self.assertIn("rightFinger", data)
        self.assertIn("mainHand", data)
        self.assertIn("offHand", data)

    def test_api_follower_items(self):
        data = api_follower_items(self.client, "enus", "Gahd#11691", 135259470)
        self.assertIsInstance(data, dict)
        self.assertIn("templar", data)
        self.assertIn("scoundrel", data)
        self.assertIn("enchantress", data)
