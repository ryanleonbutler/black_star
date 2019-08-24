# ------------------------------------------------------------------------------------------------------------------
# Text-Based RPG Game
# Author: Ryan Butler
# Developer notes: I am a massive fan of Star Wars and
# programming. Eager to learn Python, I thought it would
# be an awesome idea to develop a game, taking Star Wars
# as the inspiration.
# ------------------------------------------------------------------------------------------------------------------
"""
[Module for game character]
"""

import game_terminal as term
import game_items


class Character:
    """
    [Character class that defines and creates a 
    new character with all of the character attributes]
    """

    def __init__(
        self,
        name,
        level=1,
        health=10,
        armor=1,
        damage=1,
        head="none",
        chest="none",
        weapon="none",
    ):
        self.name = name
        self.level = level
        self.health = health
        self.armor = armor
        self.damage = damage
        self.head = head
        self.chest = chest
        self.weapon = weapon

    def describe_character(self):
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


class Inventory:
    """
    [Inventory class that manages a list of inventory items kept in the players bag]
    """

    def __init__(self, items):
        self.items = items

    def view_inventory(self):
        if not self.items:
            term.bprint(f"Inventory: Empty")
        else:
            term.bprint(f"Inventory:")
            for item in self.items:
                term.pprint(f"- {item}")
