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
        name: str,
        gender: str,
        race: str,
        inventory: list,
        level=1,
        health=10,
        armor=1,
        damage=1,
        head=None,
        chest=None,
        weapon=None,
    ):
        self.name = name.title()
        self.gender = gender.title()
        self.race = race.title()
        self.inventory = inventory
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
        if self.head is None:
            term.wprint(f"head: {self.head}")
        else:
            term.pprint(f"head: {self.head}")
        if self.chest is None:
            term.wprint(f"chest: {self.chest}")
        else:
            term.pprint(f"chest: {self.chest}")
        if self.weapon is None:
            term.wprint(f"weapon: {self.weapon}")
        else:
            term.pprint(f"weapon: {self.weapon}")

    def view_inventory(self):
        if not self.inventory:
            term.bprint("Inventory: Empty")
        else:
            term.bprint("Inventory:")
            for item in self.inventory:
                term.pprint(f"- {item.name.title()}")

    def take_item(self, item):
        """
        [Adds a item to the inventory list.]
        """
        if not item:
            term.wprint("No items on ground to take")
        else:
            self.inventory.append(item)
            term.pprint(f"---Item ({item.name.title()}) added to inventory---")

    def equip_item(self, item, inventory: list):
        for i in inventory:
            if item == i.name:
                if i.item_type == "head":
                    self.equip_head(i.name, i.armor)
                    inventory.remove(i)
                elif i.item_type == "armor":
                    self.equip_armor(i.name, i.armor)
                    inventory.remove(i)
                elif i.item_type == "weapon":
                    self.equip_weapon(i.name, i.damage)
                    inventory.remove(i)

    def equip_head(self, name, new_value):
        self.head = name.title()
        self.armor = new_value + 1

    def equip_armor(self, name, new_value):
        self.chest = name.title()
        self.armor = new_value + 1

    def equip_weapon(self, name, new_value):
        self.weapon = name.title()
        self.damage = new_value + 1

    def attack(self, enemy):
        term.rprint("Attacking... ")
        while enemy.health > 0:
            time.sleep(1)
            term.rprint(f"Hit: {self.damage}")
            time.sleep(1)
            enemy.health -= self.damage
            term.rprint(f"Enemy Health: {enemy.health}")
        time.sleep(1)
        term.gprint(f"{enemy.name} killed")
