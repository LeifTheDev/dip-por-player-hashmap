import unittest

from src.player_node import PlayerNode
from src.player import Player


class TestPlayerNode(unittest.TestCase):
    def setUp(self):
        node_player = Player("ID_1234", "Jane Doe")
        self.player_node = PlayerNode(player=node_player)

        reference_node_player = Player("ID_4321", "John Doe")
        self.reference_player_node = PlayerNode(player=reference_node_player)

    def test_key_returns_player_key(self):
        self.assertEqual(self.player_node.key, self.player_node.player.uid)

    def test_next_property_write_not_player_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.player_node.next = 123

    def test_last_property_write_not_player_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.player_node.last = 123

    def test_next_property_write_player_updates_player(self):
        self.player_node.next = self.reference_player_node
        self.assertEqual(self.reference_player_node.player.name, self.player_node.next.player.name)
        self.assertEqual(self.reference_player_node.player.uid, self.player_node.next.player.uid)

    def test_last_property_write_player_updates_player(self):
        self.player_node.last = self.reference_player_node
        self.assertEqual(self.reference_player_node.player.name, self.player_node.last.player.name)
        self.assertEqual(self.reference_player_node.player.uid, self.player_node.last.player.uid)


if __name__ == '__main__':
    unittest.main()