"""
Module for in-game commands
"""

from tools import terminal as term
from world import world


class Commands:
    """
    Class that defines some of the in-game commands
    """

    def __init__(self, my_char, current_room):
        self.my_char = my_char
        self.current_room = current_room

    def is_valid_command(self, player_input):
        valid_input = {
            "a",
            "attack",
            "v",
            "view",
            "m",
            "map",
            "y",
            "inspect",
            "t",
            "take",
            "e",
            "equip",
            "s",
            "status",
            "i",
            "inventory",
            "u",
            "up",
            "d",
            "down",
            "l",
            "left",
            "r",
            "right",
            "c",
            "clear",
            "h",
            "help",
            "q",
            "quit",
        }
        return player_input in valid_input

    def attack(self):
        if "enemy" not in world.room_map[self.current_room]:
            term.wprint("There is no enemy around")
        else:
            self.my_char.attack(world.room_map[self.current_room]["enemy"])
            world.room_map[self.current_room]["enemy"] = False

    def equip(self):
        item = term.player_input("Enter item name in inventory that you wish to equip:")
        self.my_char.equip_item(item, self.my_char.inventory)

    def inspect(self):
        if "item" not in world.room_map[self.current_room]:
            term.wprint("No items on ground to inspect")
        elif not world.room_map[self.current_room]["item"]:
            term.wprint("No items on ground to inspect")
        elif not world.room_map[self.current_room]["room"].item:
            term.wprint("No items on ground to inspect")
        else:
            world.room_map[self.current_room]["item"].view_item()

    def move(self, player_input):
        current_room_test = world.room_map[self.current_room][player_input]
        if current_room_test == "nothing":
            term.rprint("You cannot go there")
        elif current_room_test == "Window":
            term.bprint("It is dark outside, you see nothing")
        else:
            world.room_map[current_room_test]["room"].print_room()
            world.room_map[current_room_test]["room"].describe_room()
            self.current_room = current_room_test
        return self.current_room

    def take(self):
        if "item" not in world.room_map[self.current_room]:
            term.wprint("There is no item in this room")
        else:
            self.my_char.take_item(world.room_map[self.current_room]["item"])
            world.room_map[self.current_room]["item"] = False
            world.room_map[self.current_room]["room"].item = False

    def view(self):
        world.room_map[self.current_room]["room"].describe_room()

    def quit(self):
        player_input = term.player_input("Are you sure you wish to quit? (Y/N)")
        if player_input == "y" or player_input == "Y":
            term.bprint("Goodbye, see you again soon...")
            return False
        else:
            return True
