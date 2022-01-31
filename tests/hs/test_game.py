try:
    import unittest2 as unittest
except ImportError:
    import unittest

from battlenet_client.constants import UNITED_STATES
from hs_client.client import HSClient
from hs_client import game




class TestCardSearch(TestBase):

    def test_blank_search(self):
        data = card_search(self.client, 'enus')
        self.assertIsInstance(data, dict)
        self.assertIn('cards', data)
        self.assertIsInstance(data['cards'], list)
        self.assertIn('cardCount', data)
        self.assertGreater(data['cardCount'], 0)
        self.assertIn('pageCount', data)
        self.assertIn('page', data)

    def test_detailed_search(self):
        fields = {'set': 'rise-of-shadows', 'class': 'mage', 'manaCost': 10, 'attack': 4, 'health': 10,
                  'collectible': 1, 'rarity': 'legendary', 'type': 'minion', 'minionType': 'dragon',
                  'keyword': 'battlecry', 'textFilter': 'kalecgos', 'gameMode': 'constructed', 'page': 1, 'pageSize': 5,
                  'sort': 'name:asc'}
        data = card_search(self.client, 'enus', fields)
        self.assertIsInstance(data, dict)
        self.assertIn('cards', data)
        self.assertIsInstance(data['cards'], list)
        self.assertGreater(len(data['cards']), 0)
        self.assertIn('cardCount', data)
        self.assertIn('pageCount', data)
        self.assertEqual(data['page'], 1)

    def test_battlegrounds_card_search(self):
        fields = {'gameMode': 'battlegrounds', 'tier': 'hero,3'}
        data = card_search(self.client, 'enus', fields)
        self.assertIsInstance(data, dict)
        self.assertIn('cards', data)
        self.assertIsInstance(data['cards'], list)
        self.assertGreater(len(data['cards']), 0)
        self.assertIn('cardCount', data)
        self.assertIn('pageCount', data)
        self.assertEqual(data['page'], 1)


class TestCard(TestBase):

    def test_id(self):
        data = card(self.client, 'enus', 52119)
        self.assertIsInstance(data, dict)
        self.assertIn('id', data)
        self.assertEqual(data['id'], 52119)
        self.assertIn('collectible', data)
        self.assertIn('slug', data)
        self.assertIn('artistName', data)
        self.assertIn('image', data)

    def test_slug(self):
        data = card(self.client, 'enus', '52119-arch-villain-rafaam')
        self.assertIsInstance(data, dict)
        self.assertIn('id', data)
        self.assertEqual(data['id'], 52119)
        self.assertIn('collectible', data)
        self.assertIn('slug', data)
        self.assertIn('artistName', data)
        self.assertIn('image', data)


class TestCardBackSearch(TestBase):

    def card_back_search(self):
        fields = {'sort': 'dateAdded:desc'}
        data = card_back_search(self.client, 'enus', fields)
        self.assertIsInstance(data, dict)
        self.assertIn('cardBacks', data)
        self.assertIsInstance(data['cardBacks'], list)
        self.assertIn('cardCount', data)
        self.assertIn('pageCount', data)


class TestCardBack(TestBase):
    
    def test_id(self):
        data = card_back(self.client, 'enus', 155)
        self.assertIsInstance(data, dict)
        self.assertIn('id', data)
        self.assertEqual(data['id'], 155)
        self.assertIn('sortCategory', data)
        self.assertIn('text', data)
        self.assertIn('name', data)
        self.assertIn('image', data)
        self.assertIn('slug', data)
        self.assertEqual(data['slug'], '155-pizza-stone')

    def test_slug(self):
        data = card_back(self.client, 'enus', '155-pizza-stone')
        self.assertIsInstance(data, dict)
        self.assertIn('id', data)
        self.assertEqual(data['id'], 155)
        self.assertIn('sortCategory', data)
        self.assertIn('text', data)
        self.assertIn('name', data)
        self.assertIn('image', data)
        self.assertIn('slug', data)
        self.assertEqual(data['slug'], '155-pizza-stone')


class TestCardDeck(TestBase):

    def test_code(self):
        fields = {'code': 'AAECAQcG+wyd8AKS+AKggAOblAPanQMMS6IE/web8wLR9QKD+wKe+wKz/AL1gAOXlAOalAOSnwMA'}
        data = card_deck(self.client, 'enus', fields)
        self.assertIn('deckCode', data)
        self.assertEqual(data['deckCode'], fields['code'])
        self.assertIn('version', data)
        self.assertIn('hero', data)
        self.assertIn('heroPower', data)
        self.assertIn('class', data)
        self.assertIn('cards', data)

    def test_card_list(self):
        ids = (906, 1099, 1363, 1367, 46706, 48099, 48759, 49184, 50071, 50278, 51714, 52109, 52632, 52715, 53409,
               53413, 53756, 53969, 54148, 54425, 54431, 54874, 54898, 54917, 55166, 55245, 55438, 55441, 55907, 57416)
        fields = {'ids': ','.join([str(idx) for idx in ids]), 'hero': 813}
        data = card_deck(self.client, 'enus', fields)
        self.assertIn('deckCode', data)
        self.assertIn('version', data)
        self.assertIn('hero', data)
        self.assertIn('heroPower', data)
        self.assertIn('class', data)
        self.assertIn('cards', data)


class TestMetaData(TestBase):

    # sets, setGroups, types, rarities, classes, minionTypes, keywords
    def test_all(self):
        data = metadata(self.client, 'enus')
        self.assertIsInstance(data, dict)
        self.assertIn('sets', data)
        self.assertIsInstance(data['sets'], list)
        self.assertIn('setGroups', data)
        self.assertIsInstance(data['setGroups'], list)
        self.assertIn('types', data)
        self.assertIsInstance(data['types'], list)
        self.assertIn('rarities', data)
        self.assertIsInstance(data['rarities'], list)
        self.assertIn('classes', data)
        self.assertIsInstance(data['classes'], list)
        self.assertIn('minionTypes', data)
        self.assertIsInstance(data['minionTypes'], list)
        self.assertIn('keywords', data)
        self.assertIsInstance(data['keywords'], list)

    def test_type(self):
        data = metadata(self.client, 'enus', 'sets')
        self.assertIsInstance(data, list)
        self.assertIn('id', data[0])
        self.assertIn('name', data[0])
