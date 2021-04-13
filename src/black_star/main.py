"""
Main of game.
"""

import time

from characters import character as char
from characters import dialog
from tools import menu
from tools import terminal as term
from world import maps, world


def game_intro():
    """
    [Start of the game's intro function]
    """
    term.clear()
    time.sleep(1)
    term.bprint("In the future,\nin a star system very far away...\n")
    time.sleep(1)
    term.yprint("Black Star")
    term.wprint("A Text-Based Adventure")
    term.wprint("Developed by Ryan Butler")
    time.sleep(2)
    term.clear()


def set_name() -> str:
    name = term.player_input("Please enter your name")
    return name


def set_gender() -> str:
    gender = term.player_input(
        "Please enter your gender -> Male(1) or Female(2)"
    )
    while True:
        if gender == "1":
            return "Male"
        elif gender == "2":
            return "Female"
        else:
            continue


def set_race() -> str:
    while True:
        race = term.player_input(
            "Please enter your race -> Human(1) or Alien(2) or Robot(3)"
        )
        if race == "1":
            return "Human"
        elif race == "2":
            return "Alien"
        elif race == "3":
            return "Robot"
        else:
            continue


def create_char() -> tuple:
    name = set_name()
    gender = set_gender()
    race = set_race()
    my_inventory: list = []
    my_player = char.Character(name, gender, race, my_inventory)
    term.clear()
    term.bprint(
        f"Welcome {my_player.name}!\n"
        f"You have chosen to be a {my_player.gender} {my_player.race}.\n"
    )
    term.player_input("Press enter to continue...")
    term.bprint("Good luck out there!")
    time.sleep(1)
    new_char = (my_player, my_inventory)
    return new_char


def main() -> None:
    """Main game loop"""

    # Menu
    player_input = menu.game_menu()

    # Starting game if player_input == 1 in def player_menu(game_menu.py)
    start_game = False
    if player_input == "1":
        start_game = True
        (my_player, my_inventory) = create_char()
        current_room: int = 1
        dialog.start_prison_cell_dialog()
    elif player_input == "2":
        start_game = False

    while start_game:
        player_input = term.player_input("")

        if player_input == "q" or player_input == "quit":
            player_input = term.player_input(
                "Are you sure you wish to quit? (Y/N)"
            )
            if player_input == "y" or player_input == "Y":
                term.bprint("Goodbye, see you again soon...")
                start_game = False
            else:
                start_game = True

        elif player_input == "h" or player_input == "help":
            term.player_help()

        elif player_input == "v" or player_input == "view":
            world.room_map[current_room]["room"].describe_room()

        elif player_input == "s" or player_input == "status":
            my_player.describe_character()

        elif player_input == "i" or player_input == "inventory":
            my_player.view_inventory()

        elif player_input == "t" or player_input == "take":
            if world.room_map[current_room]["item"]:
                my_player.take_item(world.room_map[current_room]["item"])
                world.room_map[current_room]["item"] = False
                world.room_map[current_room]["room"].item = False
            else:
                term.wprint("No items on ground to take")

        elif player_input == "e" or player_input == "equip":
            item = term.player_input(
                "Enter item name in inventory that you wish to equip:"
            )
            my_player.equip_item(item, my_inventory)

        elif player_input == "y" or player_input == "inspect":
            if not world.room_map[current_room]["item"]:
                term.wprint("No items on ground to inspect")
            elif world.room_map[current_room]["item"] == "none":
                term.wprint("No items on ground to inspect")
            elif world.room_map[current_room]["room"].item == "none":
                term.wprint("No items on ground to inspect")
            else:
                world.room_map[current_room]["item"].name.view_item()

        elif player_input == "m" or player_input == "map":
            maps.unknown_spaceship()

        elif player_input in world.room_map[current_room]:
            current_room_test = world.room_map[current_room][player_input]
            if current_room_test == "nothing":
                term.rprint("You cannot go there")
            elif current_room_test == "Window":
                term.bprint("It is dark outside, you see nothing")
            else:
                current_room = world.room_map[current_room][player_input]
                world.room_map[current_room]["room"].print_room()
                world.room_map[current_room]["room"].describe_room()

        elif player_input == "c" or player_input == "clear":
            term.clear()

        elif player_input == "a" or player_input == "attack":
            my_player.attack(world.room_map[current_room]["enemy"])
            world.room_map[current_room]["enemy"] = False

        else:
            start_game = True


if __name__ == "__main__":
    # Clear current terminal
    term.clear()
    # Game intro
    game_intro()
    # Starting game
    main()
