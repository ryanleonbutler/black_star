import unittest

from characters import characters as char
from world import items, world


class MyTestCase(unittest.TestCase):
    current_room = world.room_map[2]
    robe = items.robe
    my_character = char.Character("Ryan")
    my_inventory = char.Inventory()
    test_inventory = [robe.name]

    # Test adding items to inventory
    def test_add_to_inventory(self):
        MyTestCase.my_inventory.take_item(MyTestCase.robe)
        self.assertCountEqual(MyTestCase.my_inventory.items, MyTestCase.test_inventory)

    # Test to equip items from inventory to character
    def test_equip_item(self):
        MyTestCase.my_inventory.equip_item(MyTestCase.robe)
        self.assertEqual(MyTestCase.my_character.chest, "Robe")


if __name__ == "__main__":
    unittest.main()
