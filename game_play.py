import os
import time
import game_terminal as gt

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


# TODO: Player Help
def character_create():
    gt.bprint("Enter your character's name:")
    Character.NAME = input(str("> "))
    Character.LEVEL = 1
    Character.HEALTH = 150
    Character.DAMAGE = 5
    Character.ARMOR = 1
    Character.HEAD = "Empty"
    Character.CHEST = "Tunic"
    Character.WEAPON = "Empty"
    Inventory.BAG[-1] = "Empty"
    gt.clear()
    gt.bprint(f"Welcome young {Character.NAME}, may the force be with you...")
    time.sleep(1)
    gt.clear()
    time.sleep(1)


def player_help():
    gt.wprint("Help Menu:")
    gt.wprint("- type 'look' to look around in this area")
    gt.wprint("- type 'take' to take object into inventory")
    gt.wprint(
        "- type 'inventory' to see what is in your bag, current gear on player and status"
    )
    gt.wprint("- type 'up', 'down', 'left' and 'right' to move around in this area")


def look_func():
    gt.bprint(f"You are in a {Room.NAME}")
    gt.yprint(f"Up: {Room.UP}")
    gt.yprint(f"Down: {Room.DOWN}")
    gt.yprint(f"Left: {Room.LEFT}")
    gt.yprint(f"Right: {Room.RIGHT}")
    gt.gprint(f"Ground: {Room.OBJECT[-1]}")


def inventory_func():
    gt.gprint(
        f"\n---INVENTORY---\nHead: {Character.HEAD}\tChest: {Character.CHEST}\n"
        f"Weapon: {Character.WEAPON}"
    )
    gt.gprint(f"Bag: {Inventory.BAG[-1]}")
    gt.bprint(f"\n---STATUS---\nLevel: {Character.LEVEL}\tHealth: {Character.HEALTH}")
    gt.rprint(
        f"\n---ATTRIBUTES---\nDamage: {Character.DAMAGE}\tArmor: {Character.ARMOR}\n"
    )
