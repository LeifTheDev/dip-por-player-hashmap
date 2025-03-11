import unittest

from src.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("1234", "Jane Doe")

    def test_player_uid_property_read(self):
        self.assertEqual(self.player.uid, '1234')

    def test_player_uid_property_write_raised_attribute_error(self):
        with self.assertRaises(AttributeError):
            self.player.uid = "4321"

    def test_player_name_property_read(self):
        self.assertEqual(self.player.name, "Jane Doe")

    def test_player_name_property_write_updates_name(self):
        self.player.name = "John Doe"
        self.assertEqual(self.player.name, "John Doe")


if __name__ == '__main__':
    unittest.main()