# ------------------------------------------------------------------------------------------------------------------
# Text-Based RPG Game
# Author: Ryan Butler
# Developer notes: I am a massive fan of Star Wars and programming. Eager to learn Python,
# I thought it would be an awesome idea to develop a game, taking Star Wars as the inspiration.
# ------------------------------------------------------------------------------------------------------------------
"""
[Module for game play/actions]
"""

import os
import time
import game_terminal as term

# class Character:
# TODO: Create Character class
class Character:
    NAME = ""
    LEVEL = 0
    HEALTH = 0
    ARMOR = 0
    DAMAGE = 0
    HEAD = "None"
    CHEST = "None"
    WEAPON = "None"


# class Object:
# TODO: Create Object class
class Object:
    NAME = ""
    ARMOR = 0
    DAMAGE = 0
    USE = ""
    Note = ""


# class Inventory:
# Inventory has 8 slots
# TODO: Create Inventory class
class Inventory:
    BAG = [""]


# class Enemy:
# TODO: Create Enemy class
class Enemy:
    NAME = ""
    LEVEL = 1
    HEALTH = 100
    ARMOR = 1
    DAMAGE = 1


# TODO: Character create
def character_create(character_profile):
    """[Character creation function]

    Arguments:
        character_profile {[dict]} -- [contains name, level and other attributes]

    Returns:
        [dict] -- [returns dict with all character info]
    """
    term.bprint("Enter your character's name:")
    character_profile['Name'] = input(str("> "))
    character_profile['Level'] = '1'
    character_profile['Health'] = '100'
    character_profile['Damage'] = '5'
    character_profile['Armor'] = '1'
    character_profile['Head'] = 'Empty'
    character_profile['Chest'] = 'Empty'
    character_profile['Weapon'] = 'Empty'
    character_profile['Bag']='Empty'
    term.clear()
    term.bprint(f"Welcome young {character_profile['Name']}, may the force be with you...")
    time.sleep(1)
    term.clear()
    time.sleep(1)
    return character_profile


def player_help():
    term.wprint("Help Menu:")
    term.wprint("- type 'look' to look around in this area")
    term.wprint("- type 'take' to take object into inventory")
    term.wprint(
        "- type 'inventory' to see what is in your bag, current gear on player and status"
    )
    term.wprint("- type 'up', 'down', 'left' and 'right' to move around in this area")


def player_look(name, up, down, left, right, item):
    term.bprint(f"You are in a {name}")
    term.yprint(f"Up: {up}")
    term.yprint(f"Down: {down}")
    term.yprint(f"Left: {left}")
    term.yprint(f"Right: {right}")
    term.gprint(f"Ground: {item}")


def inventory_func():
    term.gprint(
        f"\n---INVENTORY---\nHead: {Character.HEAD}\tChest: {Character.CHEST}\n"
        f"Weapon: {Character.WEAPON}"
    )
    term.gprint(f"Bag: {Inventory.BAG[-1]}")
    term.bprint(f"\n---STATUS---\nLevel: {Character.LEVEL}\tHealth: {Character.HEALTH}")
    term.rprint(
        f"\n---ATTRIBUTES---\nDamage: {Character.DAMAGE}\tArmor: {Character.ARMOR}\n"
    )
