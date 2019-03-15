# ------------------------------------------------------------------------------------------------------------------
# Text-Based RPG Game
# Author: Ryan Butler
# Developer notes: I am a massive fan of Star Wars and programming. Eager to learn Python,
# I thought it would be an awesome idea to develop a game, taking Star Wars as the inspiration.
# ------------------------------------------------------------------------------------------------------------------
"""
[Main of game]
"""

import os
import time
import game_terminal as term
import game_menu as menu
import game_world as world
import game_dialog as dialog
import game_play as actions

if __name__ == '__main__':

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
    if player_input == '1':
        start_game = True
    elif player_input == '2':
        start_game = False

    while start_game:
        # CHAPTER: 1 (In Prison)
        # -------------------------------------------------------------------------------------------
        prison_cell = world.Room('Prison Cell', 'Small Window', 'Nothing', 'Nothing', 'Door', 'Key')
        dialog.chapter1_prison_cell_dialog()
        prison_cell.print_room()
        time.sleep(1)
        term.player_hint()
        chapter1 = True

        while chapter1:
            player_input = term.player_input()

            if player_input.lower() == 'q' or player_input.lower() == 'quit':
                player_input = menu.game_menu()
                if player_input == '1':
                    chapter1 = False
                    start_game = True
                elif player_input == '2':
                    chapter1 = False
                    start_game = False

            elif player_input.lower() == 'h' or player_input.lower() == 'help':
                actions.player_help()

            elif player_input.lower() == 'v' or player_input.lower() == 'view':
                prison_cell.describe_room()

            elif player_input.lower() == 'u' or player_input.lower() == 'up':
                term.move_to(prison_cell.up)

            elif player_input.lower() == 'd' or player_input.lower() == 'down':
                term.move_to(prison_cell.down)

            elif player_input.lower() == 'l' or player_input.lower() == 'left':
                term.move_to(prison_cell.left)

            elif player_input.lower() == 'r' or player_input.lower() == 'right':
                term.move_to(prison_cell.right)
                chapter1 = False
                chapter2 = True
            else:
                print('Option does not exist. Try \'help\' for more info')

        # CHAPTER: 2 (Passage)
        # -------------------------------------------------------------------------------------------
        passage = world.Room('Passage', 'More Passage', 'Nothing', 'Prison Cell', 'Armory', 'Nothing')
        passage.print_room()
        while chapter2:
            player_input = term.player_input()

            if player_input.lower() == 'q' or player_input.lower() == 'quit':
                player_input = menu.game_menu()
                if player_input == '1':
                    chapter2 = False
                    start_game = True
                elif player_input == '2':
                    chapter2 = False
                    start_game = False

            elif player_input.lower() == 'h' or player_input.lower() == 'help':
                actions.player_help()

            elif player_input.lower() == 'v' or player_input.lower() == 'view':
                passage.describe_room()

            elif player_input.lower() == 'u' or player_input.lower() == 'up':
                term.move_to(passage.up)

            elif player_input.lower() == 'd' or player_input.lower() == 'down':
                term.move_to(passage.down)
                chapter2 = False
                chapter1 = True
                start_game = False

            elif player_input.lower() == 'l' or player_input.lower() == 'left':
                term.move_to(passage.left)

            elif player_input.lower() == 'r' or player_input.lower() == 'right':
                term.move_to(passage.right)
                chapter1 = False
                chapter2 = False
                chapter3 = True
            else:
                print('Option does not exist. Try \'help\' for more info')

        # CHAPTER: 3 (Armory)
        # -------------------------------------------------------------------------------------------
        armory = world.Room('Armory', 'Nothing', 'Nothing', 'Passage', 'Nothing', 'Sword')
        armory.print_room()
        while chapter3:
            player_input = term.player_input()

            if player_input.lower() == 'q' or player_input.lower() == 'quit':
                player_input = menu.game_menu()
                if player_input == '1':
                    chapter3 = False
                    start_game = True
                elif player_input == '2':
                    chapter3 = False
                    start_game = False

            elif player_input.lower() == 'h' or player_input.lower() == 'help':
                actions.player_help()

            elif player_input.lower() == 'v' or player_input.lower() == 'view':
                armory.describe_room()

            elif player_input.lower() == 'u' or player_input.lower() == 'up':
                term.move_to(armory.up)

            elif player_input.lower() == 'd' or player_input.lower() == 'down':
                term.move_to(armory.down)

            elif player_input.lower() == 'l' or player_input.lower() == 'left':
                term.move_to(armory.left)
                chapter3 = False
                chapter1 = True
                start_game = False
                chapter2 = True

            elif player_input.lower() == 'r' or player_input.lower() == 'right':
                term.move_to(armory.right)
            else:
                print('Option does not exist. Try \'help\' for more info')