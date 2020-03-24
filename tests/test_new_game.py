import unittest
from game_characters import game_character as char


class MyTestCase(unittest.TestCase):
    my_player = char.Character("Ryan")

    def test_menu(self):
        # TODO: Improve game menu testing.
        player_input = ["1", "2", "3"]
        self.assertEqual(player_input[0], "1")
        self.assertEqual(player_input[1], "2")
        self.assertEqual(player_input[2], "3")

    def test_char_defaults(self):
        # Test character initialisation and default attributes
        self.assertEqual(self.my_player.name, "Ryan")
        self.assertEqual(self.my_player.level, 1)
        self.assertEqual(self.my_player.health, 10)
        self.assertEqual(self.my_player.armor, 1)
        self.assertEqual(self.my_player.damage, 1)
        self.assertEqual(self.my_player.head, "none")
        self.assertEqual(self.my_player.chest, "none")
        self.assertEqual(self.my_player.weapon, "none")




if __name__ == '__main__':
    unittest.main()
