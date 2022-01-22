"""
Main of game.
"""

import time
from re import M

from characters import character as char
from characters import dialog
from tools import menu
from tools import terminal as term
from world import maps, world
from world.commands import Commands


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
    gender = term.player_input("Please enter your gender -> Male(1) or Female(2)")
    while True:
        if gender == "1":
            return "Male"
        elif gender == "2":
            return "Female"
        else:
            gender = term.player_input("Please enter your gender -> Male(1) or Female(2)")


def set_race() -> str:
    while True:
        race = term.player_input("Please enter your race -> Human(1) or Alien(2) or Robot(3)")
        if race == "1":
            return "Human"
        elif race == "2":
            return "Alien"
        elif race == "3":
            return "Robot"
        else:
            race = term.player_input("Please enter your race -> Human(1) or Alien(2) or Robot(3)")


def create_char():
    name = set_name()
    gender = set_gender()
    race = set_race()
    if race == "Human":
        new_char = char.Human(name, gender)
    elif race == "Alien":
        new_char = char.Alien(name, gender)
    elif race == "Robot":
        new_char = char.Robot(name, gender)
    term.clear()
    term.bprint(f"Welcome {new_char.name}!\n" f"You have chosen to be a {new_char.gender} {new_char.race}.\n")
    term.player_input("Press enter to continue...")
    term.bprint("Good luck out there!")
    time.sleep(1)
    return new_char


def main() -> None:
    """Main game loop"""

    # Menu
    player_input = menu.game_menu()

    # Starting game if player_input == 1 in def player_menu(game_menu.py)
    start_game = False
    if player_input == "1":
        start_game = True
        my_char = create_char()
        current_room: int = 1
        player_action = Commands(my_char, current_room, player_input)
        dialog.start_prison_cell_dialog()
    elif player_input == "2":
        start_game = False

    while start_game:
        player_input = term.player_input("")

        if not player_action.is_valid_command(player_input):
            term.player_hint()
            continue

        # quit game
        if player_input == "q" or player_input == "quit":
            start_game = Commands.quit(player_input)

        # help menu
        elif player_input == "h" or player_input == "help":
            term.player_help()

        # view room
        elif player_input == "v" or player_input == "view":
            world.room_map[current_room]["room"].describe_room()

        # check status
        elif player_input == "s" or player_input == "status":
            my_char.describe_character()

        # check inventory
        elif player_input == "i" or player_input == "inventory":
            my_char.view_inventory()

        # take item
        elif player_input == "t" or player_input == "take":
            Commands.take(current_room, my_char)

        # equip item
        elif player_input == "e" or player_input == "equip":
            Commands.equip(my_char)

        # inspect items in room
        elif player_input == "y" or player_input == "inspect":
            Commands.inspect(current_room)

        # view map
        elif player_input == "m" or player_input == "map":
            maps.unknown_spaceship()

        # move player
        elif player_input in world.room_map[current_room]:
            current_room = Commands.move(current_room, player_input)

        # clear terminal
        elif player_input == "c" or player_input == "clear":
            term.clear()

        # attack enemy
        elif player_input == "a" or player_input == "attack":
            Commands.attack(my_char, current_room)

        else:
            start_game = True


if __name__ == "__main__":
    # Clear current terminal
    term.clear()
    # Game intro
    game_intro()
    # Starting game
    main()
