# ------------------------------------------------------------------------------------------------------------------
# Text-Based RPG Game
# Author: Ryan Butler
# Developer notes: I am a massive fan of Star Wars and
# programming. Eager to learn Python, I thought it would
# be an awesome idea to develop a game, taking Star Wars
# as the inspiration.
# ------------------------------------------------------------------------------------------------------------------
"""
[Main of game]
"""

from os import initgroups
import time
from tools import terminal as term, menu
from world import world
from characters import characters as char, dialog


if __name__ == "__main__":

    term.clear()

    # Game Intro
    # -------------------------------------------------------------------------------------------
    menu.game_intro()

    # Menu
    # -------------------------------------------------------------------------------------------
    # TODO: Refactor Menu Code, can move it to the game_menu function
    player_input = menu.game_menu()

    # Starting game if player_input == 1 in def player_menu(game_menu.py)
    # -------------------------------------------------------------------------------------------
    if player_input == "1":
        start_game = True
        name = term.player_input("Please enter your name")
        gender = term.player_input("Please enter your gender (Male/Female)")
        race = term.player_input("Please enter your race (Human/Alien/Robot)")
        my_player = char.Character(name, gender, race)
        inventory_items = []
        my_inventory = char.Inventory(inventory_items)
        term.clear()
        term.bprint(
            f"Welcome {my_player.name}! \nYou have chosen to be a {my_player.gender} {my_player.race}.\n"
        )
        choice = term.player_input("Continue? (Y/N)")
        if choice[0].lower == "n":
            term.bprint("Going back to Main Menu")
            time.sleep(1)
        elif choice[0].lower == "Y":
            term.bprint("Good luck out there!")
            time.sleep(1)
        else:
            term.bprint('Please enter "Y" or "N"')

        dialog.start_prison_cell_dialog()
        time.sleep(0.5)
        term.player_hint()

    elif player_input == "2":
        start_game = False

    while start_game:
        game = True
        current_room = 1

        while game:
            try:
                player_input = term.player_input("")
                if player_input == "q" or player_input == "quit":
                    player_input = term.player_input("Are you sure you wish to quit? (Y/N)")
                    if player_input == "y" or player_input == "Y":
                        term.bprint("Goodbye, see you again soon...")
                        game = False
                        start_game = False
                    else:
                        game = True
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
                    player_input = term.player_input("Enter item name in inventory that you wish to equip:")
                    my_inventory.equip_item(
                        player_input
                    )  # TODO: Fix error in equip action

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
                    world.view_map()

                elif (
                    player_input in world.room_map[current_room]
                    or player_input[0] in world.room_map[current_room]
                ):
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

            except IndexError:
                pass
