"""
Main of game.
"""

import time
from tools import terminal as term, menu
from world import world, maps
from characters import characters as char, dialog


def create_char() -> tuple:
    name = term.player_input("Please enter your name")
    gender = term.player_input(
        "Please enter your gender -> Male(1) or Female(2)"
    )
    while True:
        if gender == "1":
            gender == "Male"
            break
        elif gender == "2":
            gender == "Female"
            break
        else:
            gender = term.player_input(
                "Please enter your gender -> Male(1) or Female(2)"
            )
    race = term.player_input(
        "Please enter your race -> Human(1) or Alien(2) or Robot(3)"
    )
    while True:
        if race == "1":
            race == "Human"
            break
        elif race == "2":
            race == "Alien"
            break
        elif race == "3":
            race == "Robot"
            break
        else:
            race = term.player_input(
                "Please enter your race -> Human(1) or Alien(2) or Robot(3)"
            )
    my_player = char.Character(name, gender, race)
    inventory_items = []
    my_inventory = char.Inventory(inventory_items)

    term.clear()
    term.bprint(
        f"Welcome {my_player.name}!\n"
        f"You have chosen to be a {my_player.gender} {my_player.race}.\n"
    )
    term.player_input("Press enter to continue...")
    term.bprint("Good luck out there!")
    time.sleep(1)
    return (my_player, my_inventory)


def main() -> None:
    player_input = menu.game_menu()

    # Starting game if player_input == 1 in def player_menu(game_menu.py)
    if player_input == "1":
        start_game = True
        (my_player, my_inventory) = create_char()
        current_room = 1
        dialog.start_prison_cell_dialog()
        time.sleep(0.5)
        term.player_hint()
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
            my_inventory.view_inventory()

        elif player_input == "t" or player_input == "take":
            if not world.room_map[current_room]["item"]:
                term.wprint("No items on ground to take")
            elif world.room_map[current_room]["item"] == "none":
                term.wprint("No items on ground to take")
            else:
                my_inventory.take_item(world.room_map[current_room]["item"])
                world.room_map[current_room]["item"] = "none"
                world.room_map[current_room]["room"].item = "none"

        elif player_input == "e" or player_input == "equip":
            player_input = term.player_input(
                "Enter item name in inventory" "that you wish to equip:"
            )
            my_inventory.equip_item(player_input)
            # TODO: Fix error in equip action

        elif player_input == "y" or player_input == "inspect":
            if not world.room_map.get([current_room]["item"], None):
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

        else:
            start_game = True


if __name__ == "__main__":
    term.clear()
    menu.game_intro()

    # Starting game
    main()
