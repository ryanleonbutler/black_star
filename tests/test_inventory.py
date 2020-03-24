import unittest

from game_characters import game_character as char
from game_world import game_items, game_world


class MyTestCase(unittest.TestCase):
    current_room = game_world.room_map[2]
    robe = game_items.robe
    my_character = char.Character("Ryan")
    my_inventory = char.Inventory()
    test_inventory = [robe.name]

    # Test adding items to inventory
    def test_add_to_inventory(self):
        MyTestCase.my_inventory.take_item(MyTestCase.robe.name)
        self.assertCountEqual(MyTestCase.my_inventory.items, MyTestCase.test_inventory)

    # Test to equip items from inventory to character
    def test_equip_item(self):
        MyTestCase.my_character.equip_item(MyTestCase.robe)
        self.assertEqual(MyTestCase.my_character.chest, "Robe")


if __name__ == '__main__':
    unittest.main()
