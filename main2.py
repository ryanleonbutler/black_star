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
        dialog.chapter1_prison_cell_dialog_intro(prison_cell.name)
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

            elif player_input.lower() == 'l' or player_input.lower() == 'look':
                actions.player_look(prison_cell.name, prison_cell.up, prison_cell.down, prison_cell.left, prison_cell.right, prison_cell.item)

            elif player_input.lower() == 'r' or player_input.lower() == 'right':
                chapter1 = False
                chapter2 = True
            else:
                print('Option does not exist. Try \'help\' for more info')

        # CHAPTER: 2 (Passage)
        # -------------------------------------------------------------------------------------------
        passage = world.Room('Passage', 'More Passage', 'Nothing', 'Prison Cell', 'Armory', 'Nothing')
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

            elif player_input.lower() == 'l' or player_input.lower() == 'look':
                actions.player_look(passage.name, passage.up, passage.down, passage.left, passage.right, passage.item)

            else:
                print('Option does not exist. Try \'help\' for more info')