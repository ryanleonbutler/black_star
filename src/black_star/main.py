import time

import black_star.characters.character as character
import black_star.characters.dialog as dialog
from black_star.tools import menu
from black_star.tools import terminal as term
from black_star.world import maps, world
from black_star.world.commands import Commands


def game_intro() -> None:
    """Start of the game's intro function."""
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
    """Sets the player name."""
    name = term.player_input("Please enter your name")[0]
    return name


def set_gender() -> str:
    """Sets the player gender."""
    gender = term.player_input("Please enter your gender -> Male(1) or Female(2)")[0]
    while True:
        if gender == "1":
            return "Male"
        elif gender == "2":
            return "Female"
        else:
            gender = term.player_input(
                "Please enter your gender -> Male(1) or Female(2)"
            )


def set_race() -> str:
    """Sets the player race."""
    while True:
        race = term.player_input(
            "Please enter your race -> Human(1) or Alien(2) or Robot(3)"
        )[0]
        if race == "1":
            return "Human"
        elif race == "2":
            return "Alien"
        elif race == "3":
            return "Robot"
        else:
            race = term.player_input(
                "Please enter your race -> Human(1) or Alien(2) or Robot(3)"
            )


def create_character() -> character.Human | character.Robot | character.Alien | None:
    """Creates new character for game"""
    name = set_name()
    gender = set_gender()
    race = set_race()
    new_char = None
    if race == "Human":
        new_char = character.Human(name, gender)
    elif race == "Alien":
        new_char = character.Alien(name, gender)
    elif race == "Robot":
        new_char = character.Robot(name, gender)
    term.clear()
    if new_char is not None:
        term.bprint(
            f"Welcome {new_char.name}!\nYou have chosen to be a {new_char.gender} {new_char.race}.\n"
        )
    term.player_input("Press enter to continue...")
    term.bprint("Good luck out there!")
    time.sleep(1)
    return new_char


def main() -> None:
    """Main game loop."""
    start_game = None
    my_char = None
    player_action = None
    current_room = None

    # Menu
    player_input = menu.game_menu()

    if player_input == "1":
        start_game = True
        my_char = create_character()
        current_room = 1
        if my_char is not None:
            player_action = Commands(my_char, current_room)
        dialog.start_prison_cell_dialog()

    elif player_input == "2":
        start_game = False

    while start_game:
        if player_action is None or current_room is None or my_char is None:
            break

        command, argument = term.player_input()

        if not player_action.is_valid_command(command):
            term.player_hint()
            continue

        # quit game
        if command == "q" or command == "quit":
            start_game = player_action.quit()

        # help menu
        elif command == "h" or command == "help":
            term.player_help()

        # view room
        elif command == "v" or command == "view":
            player_action.view()

        # player status
        elif command == "s" or command == "status":
            my_char.describe_character()

        # check inventory
        elif command == "i" or command == "inventory":
            my_char.view_inventory()

        # take item
        elif command == "t" or command == "take":
            player_action.take()

        # equip item
        elif command == "e" or command == "equip":
            if argument is not None:
                player_action.equip(argument)
            else:
                player_action.equip()

        # inspect room
        elif command == "y" or command == "inspect":
            player_action.inspect()

        # view map
        elif command == "m" or command == "map":
            maps.unknown_spaceship()

        # move
        elif command in world.room_map[current_room]:
            current_room = player_action.move(command)

        # clear terminal
        elif command == "c" or command == "clear":
            term.clear()

        # attack enemy
        elif command == "a" or command == "attack":
            player_action.attack()

        else:
            start_game = True


if __name__ == "__main__":
    # Clear current terminal
    term.clear()
    # Game intro
    game_intro()
    # Starting game
    main()
