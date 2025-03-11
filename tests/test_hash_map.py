from src.hash_map import HashMap
from src.player import Player

import unittest


class TestHashMap(unittest.TestCase):

    def setUp(self):
        self.hash_map = HashMap()
        self.test_player_name = "Jane Doe"

        self.players = [Player(f"ID-{i}", self.test_player_name) for i in range(10)]

    def test_add_one_item_correctly_adds_to_item_in_array(self):
        self.hash_map.add(self.players[0])

        index = Player.pearson_hash(self.players[0].uid) % self.hash_map.size
        self.assertIn(self.players[0], self.hash_map._array[index])

    def test_correct_length_before_adding_items(self):
        self.assertEqual(len(self.hash_map), 0)

    def test_correct_length_after_adding_items(self):

        self.hash_map.add(self.players[0])
        self.assertEqual(len(self.hash_map), 1)

        self.hash_map.add(self.players[1])
        self.assertEqual(len(self.hash_map), 2)

        self.hash_map.add(self.players[2])
        self.assertEqual(len(self.hash_map), 3)

    def test_correct_length_after_removing_items(self):

        self.hash_map.add(self.players[0])
        self.assertEqual(len(self.hash_map), 1)

        self.hash_map.add(self.players[1])
        self.hash_map.add(self.players[2])

        self.hash_map.remove(self.players[1].uid)
        self.assertEqual(len(self.hash_map), 2)

    def test_get_filled_hashmap_valid_key_returns_correct_player(self):
        for player in self.players:
            self.hash_map.add(player)

        for player in self.players:
            self.assertEqual(self.hash_map.get(player.uid), player)

    def test_get_empty_hashmap_raises_key_error(self):
        with self.assertRaises(KeyError):
            self.hash_map.get('1234')

    def test_get_filled_hashmap_invalid_key_raises_key_error(self):
        for player in self.players:
            self.hash_map.add(player)

        with self.assertRaises(KeyError):
            self.hash_map.get('ID-11')

        with self.assertRaises(KeyError):
            self.hash_map.get('ID')

    def test_remove_empty_raises_key_error(self):
        with self.assertRaises(KeyError):
            self.hash_map.remove("ID-0")

    def test_remove_invalid_key_raises_key_error(self):

        self.hash_map.add(self.players[0])
        self.hash_map.add(self.players[1])
        self.hash_map.add(self.players[2])
        self.hash_map.add(self.players[3])
        self.hash_map.add(self.players[4])

        with self.assertRaises(KeyError):
            self.hash_map.remove("ID-14389038")

    def test_put_invalid_key_raises_key_error(self):
        self.hash_map.add(self.players[0])
        self.hash_map.add(self.players[1])
        self.hash_map.add(self.players[2])

        with self.assertRaises(KeyError):
            self.hash_map.put("Hello", "World!")

    def test_put_only_item_updates_player_name(self):
        self.hash_map.add(self.players[0])

        self.hash_map.put(self.players[0].uid, "Hello, World!")
        self.assertEqual(self.hash_map.get(self.players[0].uid).name, "Hello, World!")

    def test_put_multiple_item_updates_only_correct_player_name(self):
        self.hash_map.add(self.players[0])
        self.hash_map.add(self.players[1])
        self.hash_map.add(self.players[2])

        self.hash_map.put(self.players[2].uid, "Hello, World!")
        self.assertEqual(self.hash_map.get(self.players[2].uid).name, "Hello, World!")

        self.assertEqual(self.hash_map.get(self.players[0].uid).name, "Jane Doe")
        self.assertEqual(self.hash_map.get(self.players[1].uid).name, "Jane Doe")
