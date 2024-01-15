"""
Module for game objects.
"""


from enum import Enum

from black_star.tools import terminal as term


class ItemTypes(Enum):
    head = "head"
    body = "body"
    weapon = "weapon"
    other = "other"


# class for Items to use and equip in-game:
class Item:
    """
    Item class that defines usable objects in the game like armor and weapons.
    Also other items like health elixirs and notes.
    """

    def __init__(
        self, name: str, item_type: ItemTypes, armor=0, damage=0, description=""
    ):
        self.name = name
        self.item_type = item_type
        self.armor = armor
        self.damage = damage
        self.description = description

    def view_item(self):
        """
        [Prints item details and attributes to the screen]
        """
        if not self.name or self.name == "none":
            term.wprint("No items on ground to inspect")
        else:
            term.bprint(f"---Item details: ({self.name.title()})---")
            term.pprint(
                f"Type: {self.item_type}\n"
                f"Armor: {self.armor}\n"
                f"Damage: {self.damage}\n"
                f"Description: {self.description}"
            )
