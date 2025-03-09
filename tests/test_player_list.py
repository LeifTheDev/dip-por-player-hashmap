import unittest

from src.player import Player
from src.player_node import PlayerNode
from src.player_list import PlayerList


class TestPlayerList(unittest.TestCase):
    def setUp(self):
        self.test_player_one = Player("ID_1", "Bob")
        self.test_player_two = Player("ID_2", "Jane")
        self.test_player_three = Player("ID_3", "John")

        self.player_list = PlayerList()

    def test_append_player_empty_list_sets_head(self):
        self.player_list.append(self.test_player_one)

        self.assertEqual(self.player_list.head.player, self.test_player_one,
                         "PlayerList.head does not reference the expected Player value"
                         )

    def test_append_player_one_item_in_list_sets_tail(self):
        self.player_list.append(self.test_player_one)
        self.player_list.append(self.test_player_two)

        self.assertEqual(self.player_list.tail.player, self.test_player_two,
                         "PlayerList.tail does not reference the expected Player value"
                         )

    def test_append_player_two_items_in_list_appends_correctly_with_list_continuity(self):
        self.player_list.append(self.test_player_one)
        self.player_list.append(self.test_player_two)
        self.player_list.append(self.test_player_three)

        self.assertEqual(self.player_list.head.player, self.test_player_one,
                         "PlayerList.head does not point to first item appended"
                         )
        self.assertEqual(self.player_list.tail.player, self.test_player_three,
                         "PlayerList.tail does not reference last item appended"
                         )

        self.assertEqual(self.player_list.head.next.player, self.test_player_two,
                         "PlayerList.head.next does not point to second item appended"
                         )

        self.assertEqual(self.player_list.tail.last.player, self.test_player_two,
                         "PlayerList.tail.last does not point to second item appended"
                         )

        self.assertEqual(self.player_list.head.next.last, self.player_list.head,
                         "Second item appended does not point to PlayerList.head"
                         )
        self.assertEqual(self.player_list.head.next.next, self.player_list.tail,
                         "Second item appended does not point to PlayerList.tail")

    def test_prepend_empty_list_sets_head(self):
        self.player_list.prepend(self.test_player_one)

        self.assertEqual(self.player_list.head.player, self.test_player_one,
                         "PlayerList.head does not reference the expected Player value"
                         )

    def test_prepend_empty_list_sets_head_and_tail(self):
        self.player_list.prepend(self.test_player_one)
        self.player_list.prepend(self.test_player_two)

        self.assertEqual(self.player_list.head.player, self.test_player_two,
                         "PlayerList.head does not reference the second prepended Player"
                         )

        self.assertEqual(self.player_list.tail.player, self.test_player_one,
                         "PlayerList.tail does not reference the second prepended Player"
                         )

    def test_prepend_two_items_in_list_prepends_correctly_with_list_continuity(self):
        self.player_list.prepend(self.test_player_one)
        self.player_list.prepend(self.test_player_two)
        self.player_list.prepend(self.test_player_three)

        self.assertEqual(self.player_list.tail.player, self.test_player_one,
                         "PlayerList.tail does not reference the first prepended Player"
                         )

        self.assertEqual(self.player_list.head.player, self.test_player_three,
                         "PlayerList.head does not reference the last prepended Player"
                         )

        self.assertEqual(self.player_list.head.next.last, self.player_list.head,
                         "Second prepended Player does not point to PlayerList.head"
                         )

        self.assertEqual(self.player_list.head.next.next, self.player_list.tail,
                         "Second prepended Player does not point to PlayerList.tail"
                         )

    def test_is_empty_empty_list_returns_true(self):
        self.assertEqual(self.player_list.is_empty, True)

    def test_is_empty_populated_list_returns_false(self):
        self.player_list.append(self.test_player_one)
        self.assertEqual(self.player_list.is_empty, False)

    def test_remove_at_head_one_item_sets_head_and_tail_to_None(self):
        self.player_list.append(self.test_player_one)

        self.player_list.remove_at_head()
        self.assertEqual(self.player_list.head, None)
        self.assertEqual(self.player_list.tail, None)

    def test_remove_at_tail_one_item_sets_head_and_tail_to_None(self):
        self.player_list.append(self.test_player_one)

        self.player_list.remove_at_tail()
        self.assertEqual(self.player_list.head, None)
        self.assertEqual(self.player_list.tail, None)

    def test_remove_at_head_multiple_items_removes_head(self):
        self.player_list.append(self.test_player_one)
        self.player_list.append(self.test_player_two)
        self.player_list.append(self.test_player_three)

        self.player_list.remove_at_head()

        self.assertEqual(self.player_list.head.player, self.test_player_two)
        self.assertEqual(self.player_list.head.last, None)

    def test_remove_at_tail_multiple_items_removes_tail(self):
        self.player_list.append(self.test_player_one)
        self.player_list.append(self.test_player_two)
        self.player_list.append(self.test_player_three)

        self.player_list.remove_at_tail()

        self.assertEqual(self.player_list.tail.player, self.test_player_two)
        self.assertEqual(self.player_list.tail.next, None)

    def test_remove_by_key_item_in_list_removed(self):
        self.player_list.append(self.test_player_one)
        self.player_list.append(self.test_player_two)
        self.player_list.append(self.test_player_three)

        self.player_list.remove("ID_2")

        self.assertEqual(self.player_list.head.next, self.player_list.tail)
        self.assertEqual(self.player_list.tail.last, self.player_list.head)

    def test_remove_key_item_not_in_list_raised_key_error(self):
        self.player_list.append(self.test_player_one)
        self.player_list.append(self.test_player_two)
        self.player_list.append(self.test_player_three)

        with self.assertRaises(KeyError):
            self.player_list.remove("1234")

    def test_remove_key_item_is_head_item_removed(self):
        self.player_list.append(self.test_player_one)
        self.player_list.append(self.test_player_two)
        self.player_list.append(self.test_player_three)

        self.player_list.remove("ID_1")

        self.assertEqual(self.player_list.head.player, self.test_player_two)

    def test_remove_key_item_is_tail_item_removed(self):
        self.player_list.append(self.test_player_one)
        self.player_list.append(self.test_player_two)
        self.player_list.append(self.test_player_three)

        self.player_list.remove("ID_3")

        self.assertEqual(self.player_list.tail.player, self.test_player_two)


if __name__ == "__main__":
    unittest.main()