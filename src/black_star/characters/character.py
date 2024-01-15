"""
Module for game character.
"""
import time
from typing import List

from black_star.tools import terminal as term
from black_star.world.items import Item, ItemTypes


class Character:
    """
    Base Character class that defines and creates a
    new character with all of the character attributes
    """

    def __init__(
        self,
        name: str,
        gender: str,
        inventory: List[Item],
        level: int,
        exp: int,
        head: str = "",
        body: str = "",
        weapon: str = "",
        health: int = 0,
        armor: int = 0,
        damage: int = 0,
    ):
        self.name = name
        self.gender = gender
        self.inventory = inventory
        self.level = level
        self.exp = exp
        self.head = head
        self.body = body
        self.weapon = weapon
        self.health = health
        self.armor = armor
        self.damage = damage

    def describe_character(self):
        term.bprint(f"--- My Character({self.name.title()})---")
        term.wprint(f"Level: {self.level}")
        term.gprint(f"Health: {self.health}")
        term.yprint(f"Armor: {self.armor}")
        term.rprint(f"Damage: {self.damage}\n")
        term.bprint(f"--- Items Equiped({self.name.title()})---")
        if self.head is None:
            term.wprint(f"head: {self.head.title()}")
        else:
            term.pprint(f"head: {self.head.title()}")
        if self.body is None:
            term.wprint(f"body: {self.body.title()}")
        else:
            term.pprint(f"body: {self.body.title()}")
        if self.weapon is None:
            term.wprint(f"weapon: {self.weapon.title()}")
        else:
            term.pprint(f"weapon: {self.weapon.title()}")

    def view_inventory(self):
        if not self.inventory:
            term.bprint("Inventory: Empty")
        else:
            term.bprint("Inventory:")
            for item in self.inventory:
                term.pprint(f"- {item.name.title()}")

    def take_item(self, item: Item):
        """
        [Adds a item to the inventory list.]
        """
        if not item:
            term.wprint("No items on ground to take")
        else:
            self.inventory.append(item)
            term.pprint(f"---Item ({item.name.title()}) added to inventory---")

    def equip_item(self, item_name: str) -> None:
        for i in self.inventory:
            if item_name == i.name:
                if i.item_type == ItemTypes.head:
                    self.equip_head(i.name, i.armor)
                    self.inventory.remove(i)
                elif i.item_type == ItemTypes.body:
                    self.equip_body(i.name, i.armor)
                    self.inventory.remove(i)
                elif i.item_type == ItemTypes.weapon:
                    self.equip_weapon(i.name, i.damage)
                    self.inventory.remove(i)
                elif i.item_type == ItemTypes.other:
                    term.pprint(
                        f"---Oops! Item({item_name.title()}) cannot be equipped!---"
                    )
                return

        term.pprint(f"---Oops! Item({item_name.title()}) is not in your inventory!---")

    def equip_head(self, name, new_value):
        self.head = name
        self.armor += new_value

    def equip_body(self, name, new_value):
        self.body = name
        self.armor += new_value

    def equip_weapon(self, name, new_value):
        self.weapon = name
        self.damage += new_value

    def attack(self, enemy):
        if not enemy:
            term.wprint("There is no enemy around")
        else:
            term.rprint("Attacking... ")
            while enemy.health > 0:
                time.sleep(1)
                term.rprint(f"Hit: {self.damage}")
                time.sleep(1)
                enemy.health -= self.damage
                term.rprint(f"Enemy Health: {enemy.health}")
            time.sleep(1)
            term.gprint(f"{enemy.name} killed")


class Human(Character):
    """
    Class for the Human Race.
    Strong and heavy armored Race.
    """

    def __init__(
        self,
        name: str,
        gender: str,
        inventory: List[Item] = [],
        level: int = 1,
        exp: int = 0,
        head: str = "",
        body: str = "",
        weapon: str = "",
        race: str = "Human",
        health: int = 15,
        armor: int = 7,
        damage: int = 3,
    ):
        super().__init__(name, gender, inventory, level, exp, head, body, weapon)
        self.race = race
        self.health = health
        self.armor = armor
        self.damage = damage

    def __repr__(self) -> str:
        return f"{self.name}"


class Alien(Character):
    """
    Class for the Alien Race.
    High damage race, but easily takes damage
    """

    def __init__(
        self,
        name: str,
        gender: str,
        inventory: List[Item] = [],
        level: int = 1,
        exp: int = 0,
        head: str = "",
        body: str = "",
        weapon: str = "",
        race: str = "Alien",
        health: int = 9,
        armor: int = 3,
        damage: int = 13,
    ):
        super().__init__(name, gender, inventory, level, exp, head, body, weapon)
        self.race = race
        self.health = health
        self.armor = armor
        self.damage = damage


class Robot(Character):
    """
    Class for the Robot Race.
    Well balanced race, can give and take damage equally.
    """

    def __init__(
        self,
        name: str,
        gender: str,
        inventory: List[Item] = [],
        level: int = 1,
        exp: int = 0,
        head: str = "",
        body: str = "",
        weapon: str = "",
        race: str = "Robot",
        health: int = 12,
        armor: int = 5,
        damage: int = 8,
    ):
        super().__init__(name, gender, inventory, level, exp, head, body, weapon)
        self.race = race
        self.health = health
        self.armor = armor
        self.damage = damage
