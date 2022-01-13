"""
Module for in-game commands
"""

from tools import terminal as term
from world import world


def inspect(current_room):
    if not world.room_map[current_room]["item"]:
        term.wprint("No items on ground to inspect")
    elif world.room_map[current_room]["item"] == "none":
        term.wprint("No items on ground to inspect")
    elif world.room_map[current_room]["room"].item == "none":
        term.wprint("No items on ground to inspect")
    else:
        world.room_map[current_room]["item"].view_item()


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
    if world.room_map[current_room]["item"]:
        my_char.take_item(world.room_map[current_room]["item"])
        world.room_map[current_room]["item"] = False
        world.room_map[current_room]["room"].item = False
    else:
        term.wprint("No items on ground to take")


def quit():
    player_input = term.player_input("Are you sure you wish to quit? (Y/N)")
    if player_input == "y" or player_input == "Y":
        term.bprint("Goodbye, see you again soon...")
        return False
    else:
        return True
