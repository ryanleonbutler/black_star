"""
Module for in-game commands
"""

from tools import terminal as term
from world import world

class Commands:

    def is_valid_command(player_input):
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


    def attack(my_char, current_room):
        if "enemy" not in world.room_map[current_room]:
            term.wprint("There is no enemy around")
        else:
            try:
                my_char.attack(world.room_map[current_room]["enemy"])
                world.room_map[current_room]["enemy"] = False
            except AttributeError:
                term.wprint("The enemy has been killed")
    

    def equip(my_char):
        item = term.player_input("Enter item name in inventory that you wish to equip:")
        my_char.equip_item(item, my_char.inventory)


    def inspect(current_room):
        if "item" not in world.room_map[current_room]:
            term.wprint("No items on ground to inspect")
        elif world.room_map[current_room]["item"] == False:
            term.wprint("No items on ground to inspect")
        elif world.room_map[current_room]["room"].item == False:
            term.wprint("No items on ground to inspect")
        else:
            world.room_map[current_room]["item"].view_item()


    def move(current_room, player_input):
        current_room_test = world.room_map[current_room][player_input]
        if current_room_test == "nothing":
            term.rprint("You cannot go there")
            return current_room
        elif current_room_test == "Window":
            term.bprint("It is dark outside, you see nothing")
            return current_room
        else:
            world.room_map[current_room_test]["room"].print_room()
            world.room_map[current_room_test]["room"].describe_room()
            return current_room_test


    def take(current_room, my_char):
        if "item" not in world.room_map[current_room]:
            term.wprint("No items on ground to take")
        else:
            my_char.take_item(world.room_map[current_room]["item"])
            world.room_map[current_room]["item"] = False
            world.room_map[current_room]["room"].item = False

    def quit():
        player_input = term.player_input("Are you sure you wish to quit? (Y/N)")
        if player_input == "y" or player_input == "Y":
            term.bprint("Goodbye, see you again soon...")
            return False
        else:
            return True
