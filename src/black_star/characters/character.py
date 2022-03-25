"""
Module for game character.
"""
import time

from tools import terminal as term


class Character:
    """
    Base Character class that defines and creates a
    new character with all of the character attributes
    """

    def __init__(
        self,
        name: str,
        gender: str,
        inventory: list,
        level: int,
        exp: int,
        head: str = None,
        body: str = None,
        weapon: str = None,
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
            term.wprint(f"head: {self.head}")
        else:
            term.pprint(f"head: {self.head}")
        if self.body is None:
            term.wprint(f"body: {self.body}")
        else:
            term.pprint(f"body: {self.body}")
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
                    self.equip_body(i.name, i.armor)
                    inventory.remove(i)
                elif i.item_type == "weapon":
                    self.equip_weapon(i.name, i.damage)
                    inventory.remove(i)
                return
        term.pprint(f"---Oops! {item} is not in your inventory!---")

    def equip_head(self, name, new_value):
        self.head = name.title()
        self.armor += new_value

    def equip_body(self, name, new_value):
        self.body = name.title()
        self.armor += new_value

    def equip_weapon(self, name, new_value):
        self.weapon = name.title()
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
        inventory: list = [],
        level: int = 1,
        exp: int = 0,
        head: str = None,
        body: str = None,
        weapon: str = None,
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


class Alien(Character):
    """
    Class for the Alien Race.
    High damage race, but easily takes damage
    """

    def __init__(
        self,
        name: str,
        gender: str,
        inventory: list = [],
        level: int = 1,
        exp: int = 0,
        head: str = None,
        body: str = None,
        weapon: str = None,
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
        inventory: list = [],
        level: int = 1,
        exp: int = 0,
        head: str = None,
        body: str = None,
        weapon: str = None,
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
