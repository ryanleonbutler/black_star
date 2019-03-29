# ------------------------------------------------------------------------------------------------------------------
# Text-Based RPG Game
# Author: Ryan Butler
# Developer notes: I am a massive fan of Star Wars and programming. Eager to learn Python,
# I thought it would be an awesome idea to develop a game, taking Star Wars as the inspiration.
# ------------------------------------------------------------------------------------------------------------------
"""
[Module for game play/actions]
"""

import time
import game_terminal as term


class Character():
    """
    [Character class that defines and creates a new character with all of the character attributes]
    """

    def __init__(self, name, level, health, armor, damage, head, chest, weapon):
        self.name = name
        self.level = level
        self.health = health
        self.armor = armor
        self.damage = damage
        self.head = head
        self.chest = chest
        self.weapon = weapon

    def describe_character(self):
        term.gprint(f'---Character({self.name})---\n'
        f'Level: {self.level}\n'
        f'Health: {self.level}\n'
        f'Armor: {self.level}\n'
        f'Damage: {self.level}\n'
        )


# class Object:
# TODO: Create Object class
class Object:
    NAME = ""
    ARMOR = 0
    DAMAGE = 0
    USE = ""
    Note = ""

class Inventory():
    """
    [Inventory class that manages a list of inventory items kept in the players bag]
    """
    def __init__(self, items):
        self.items = []

    def view_inventory(self):
        term.gprint(
            f"\n---INVENTORY---\nHead: {Character.HEAD}\tChest: {Character.CHEST}\n"
            f"Weapon: {Character.WEAPON}"
        )
        term.gprint(f"Bag: {Inventory.BAG[-1]}")
        term.bprint(f"\n---STATUS---\nLevel: {Character.LEVEL}\tHealth: {Character.HEALTH}")
        term.rprint(
            f"\n---ATTRIBUTES---\nDamage: {Character.DAMAGE}\tArmor: {Character.ARMOR}\n"
        )


# class Enemy:
# TODO: Create Enemy class
class Enemy:
    NAME = ""
    LEVEL = 1
    HEALTH = 100
    ARMOR = 1
    DAMAGE = 1



