# ------------------------------------------------------------------------------------------------------------------
# Text-Based RPG Game
# Author: Ryan Butler
# Developer notes: I am a massive fan of Star Wars and programming. Eager to learn Python,
# I thought it would be an awesome idea to develop a game, taking Star Wars as the inspiration.
# ------------------------------------------------------------------------------------------------------------------
"""
[Main of game]
"""

import time
import game_terminal as term
import game_menu as menu
import game_character as char
import game_world as world
from game_world import room_map
import game_items
import game_dialog as dialog


if __name__ == "__main__":

    # Constants
    # -------------------------------------------------------------------------------------------
    # Variables
    # -------------------------------------------------------------------------------------------

    term.clear()

    # Game Intro
    # -------------------------------------------------------------------------------------------
    menu.game_intro()

    # Menu
    # -------------------------------------------------------------------------------------------
    player_input = menu.game_menu()

    # Starting game if player_input == 1 in def player_menu (game_menu.py module)
    # -------------------------------------------------------------------------------------------
    if player_input == "1":
        start_game = True
        term.bprint("Please enter your name")
        myname = term.player_input()
        myplayer = char.Character(myname)
        inventory_items = []
        myinventory = char.Inventory(inventory_items)
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
                player_input = term.player_input()

                if player_input == "q" or player_input == "quit":
                    term.bprint("Are you sure you wish to quit? (Y/N)")
                    player_input = term.player_input()
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
                    room_map[current_room]["room"].describe_room()

                elif player_input == "s" or player_input == "status":
                    myplayer.describe_character()

                elif player_input == "i" or player_input == "inventory":
                    myinventory.view_inventory()

                elif player_input == "t" or player_input == "take":
                    if not room_map[current_room]["item"]:
                        term.wprint(
                            f"No items on ground to take")
                    elif room_map[current_room]["item"] == "none":
                        term.wprint(
                            f"No items on ground to take")
                    elif room_map[current_room]["room"].item == "none":
                        term.wprint(
                            f"No items on ground to take")
                    else:
                        inventory_items.append(room_map[current_room]["item"].name)
                        room_map[current_room]["item"].take_item()
                        room_map[current_room]["item"] = "none"
                        room_map[current_room]["room"].item = "none"
                
                elif player_input == "e" or player_input == "equip":
                    term.bprint("Enter item name in inventory that you wish to equip:")
                    player_input = term.player_input()
                    for player_input in inventory_items:
                        myplayer.equip_item()
                        term.bprint(f"{player_input} has been equipped")

                elif player_input == "y" or player_input == "inspect":
                    if not room_map[current_room]["item"]:
                        term.wprint(
                            f"No items on ground to inspect")
                    elif room_map[current_room]["item"] == "none":
                        term.wprint(
                            f"No items on ground to inspect")
                    elif room_map[current_room]["room"].item == "none":
                        term.wprint(
                            f"No items on ground to inspect")
                    else:
                        room_map[current_room]["item"].view_item()

                elif player_input == "m" or player_input == "map":
                    world.view_map()

                elif (
                    player_input in room_map[current_room]
                    or player_input[0] in room_map[current_room]
                ):
                    current_room_test = room_map[current_room][player_input]
                    if current_room_test == "nothing":
                        term.rprint(f"You cannot go there")
                    elif current_room_test == "Window":
                        term.bprint(f"It is dark outside, you see nothing")
                    else:
                        current_room = room_map[current_room][player_input]
                        room_map[current_room]["room"].print_room()
                        room_map[current_room]["room"].describe_room()

                elif player_input == "c" or player_input == "clear":
                    term.clear()

            except IndexError:
                pass