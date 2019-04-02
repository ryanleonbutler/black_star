# ------------------------------------------------------------------------------------------------------------------
# Text-Based RPG Game
# Author: Ryan Butler
# Developer notes: I am a massive fan of Star Wars and programming. Eager to learn Python,
# I thought it would be an awesome idea to develop a game, taking Star Wars as the inspiration.
# ------------------------------------------------------------------------------------------------------------------
"""
[Module for game character]
"""

import time
import game_terminal as term


class Character():
    """
    [Character class that defines and creates a new character with all of the character attributes]
    """

    def __init__(self, name, level=1, health=100, armor=1, damage=1, head='Empty', chest='Empty', weapon='Empty'):
        self.name = name
        self.level = level
        self.health = health
        self.armor = armor
        self.damage = damage
        self.head = head
        self.chest = chest
        self.weapon = weapon

    def describe_character(self):
        term.gprint(f'--- My Character({self.name.title()})---\n'
        f'Level: {self.level}\n'
        f'Health: {self.health}\n'
        f'Armor: {self.armor}\n'
        f'Damage: {self.damage}'
        )


class Inventory():
    """
    [Inventory class that manages a list of inventory items kept in the players bag]
    """
    def __init__(self, items=''):
        self.items = items

    def view_inventory(self):
        for item in self.items:
            term.gprint(f"Bag: {item[-1]}")