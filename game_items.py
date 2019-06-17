# ------------------------------------------------------------------------------------------------------------------
# Text-Based RPG Game
# Author: Ryan Butler
# Developer notes: I am a massive fan of Star Wars and programming. Eager to learn Python,
# I thought it would be an awesome idea to develop a game, taking Star Wars as the inspiration.
# ------------------------------------------------------------------------------------------------------------------
"""
[Module for game objects]
"""


import time
import game_terminal as term
import game_character as char


# class for Items to use and equip in-game:
class Items:
    """
    [Item class that defines usable objects in the game like armor and weapons. Also other items like health elixers and notes.]
    """
    def __init__(
        self,
        name="",
        item_type="",
        armor=0,
        damage=0,
        description="",
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
        if not self.name:
            term.wprint("No items on ground to inspect")
        elif self.name == "none":
            term.wprint("No items on ground to inspect")
        else:
            term.bprint(
                f"---Item details: ({self.name.title()})---")
            term.pprint(
                f"Type: {self.item_type}\n"
                f"Armor: {self.armor}\n"
                f"Damage: {self.damage}\n"
                f"Description: {self.description}"
            )


    def take_item(self):
        """
        [Adds a item to the inventory.]
        """
        if not self.name:
            term.wprint("No items on ground to take")
        else:
            term.pprint(
                f"---Item ({self.name.title()}) added to inventory---"
            )


# Create game itemms
key = Items("Key", "Other", 0, 0, "Opens lock on door")
robe = Items("Robe", "Armor", 5, 0, "Plain brown cotton robe")
space_sword = Items("Space Sword", "Weapon", 0, 5, "Laser energy sword that cuts through anything")