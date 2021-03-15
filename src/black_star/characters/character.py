"""
Module for game character.
"""

import time
from tools import terminal as term


class Character:
    """
    [Character class that defines and creates a
    new character with all of the character attributes]
    """

    def __init__(
        self,
        name=None,
        gender=None,
        race=None,
        level=1,
        health=10,
        armor=1,
        damage=1,
        head=None,
        chest=None,
        weapon=None,
    ):
        self.name = name
        self.gender = gender
        self.race = race
        self.level = level
        self.health = health
        self.armor = armor
        self.damage = damage
        self.head = head
        self.chest = chest
        self.weapon = weapon

    def set_name(self):
        self.name = term.player_input("Please enter your name")

    def describe_character(self) -> dict:
        term.bprint(f"--- My Character({self.name.title()})---")
        term.wprint(f"Level: {self.level}")
        term.gprint(f"Health: {self.health}")
        term.yprint(f"Armor: {self.armor}")
        term.rprint(f"Damage: {self.damage}\n")
        term.bprint(f"--- Items Equiped({self.name.title()})---")
        if self.head == "none":
            term.wprint(f"head: {self.head}")
        else:
            term.pprint(f"head: {self.head}")
        if self.chest == "none":
            term.wprint(f"chest: {self.chest}")
        else:
            term.pprint(f"chest: {self.chest}")
        if self.weapon == "none":
            term.wprint(f"weapon: {self.weapon}")
        else:
            term.pprint(f"weapon: {self.weapon}")

    def set_gender(self):
        input = term.player_input(
            "Please enter your gender -> Male(1) or Female(2)"
        )
        while True:
            if input == "1":
                self.gender = "Male"
                break
            elif input == "2":
                self.gender = "Female"
                break
            else:
                continue

    def set_race(self):
        while True:
            input = term.player_input(
                "Please enter your race -> Human(1) or Alien(2) or Robot(3)"
            )
            if input == "1":
                self.race = "Human"
                break
            elif input == "2":
                self.race = "Alien"
                break
            elif input == "3":
                self.race = "Robot"
                break
            else:
                continue

    def change_armor(self, name, new_value):
        self.chest = name
        self.armor = new_value + 1


class Inventory:
    """
    [Inventory class that manages a list of inventory items kept in the players bag]
    """

    def __init__(self, items=[]):
        self.items = items

    def view_inventory(self):
        if not self.items:
            term.bprint("Inventory: Empty")
        else:
            term.bprint("Inventory:")
            for item in self.items:
                term.pprint(f"- {item.name.title()}")

    def take_item(self, item):
        """
        [Adds a item to the inventory list.]
        """
        if not item:
            term.wprint("No items on ground to take")
        else:
            self.items.append(item)
            term.pprint(f"---Item ({item.name.title()}) added to inventory---")

    def equip_item(self, item):
        # TODO: Finish equip item action.
        inv_list = []
        for i in self.items:
            inv_list.append(i.name)
            if item in inv_list:
                if i.item_type == "Armor":
                    Character.change_armor(i.name, i.armor)
        else:
            term.wprint("No such item in inventory to equip")


def create_char() -> tuple:
    my_char = Character()
    my_char.set_name()
    my_char.set_gender()
    my_char.set_race()
    inv_items = []
    my_inv = Inventory(inv_items)
    term.clear()
    term.bprint(
        f"Welcome {my_char.name}!\n"
        f"You have chosen to be a {my_char.gender} {my_char.race}.\n"
    )
    term.player_input("Press enter to continue...")
    term.bprint("Good luck out there!")
    time.sleep(1)
    return (my_char, my_inv)
