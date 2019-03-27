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
        dialog.start_prison_cell_dialog()
        time.sleep(0.5)
        term.player_hint()
    elif player_input == '2':
        start_game = False

    while start_game:

        prison_cell = world.Room('Prison Cell', 'Small Window', 'Nothing', 'Nothing', 'Passage', 'Key')
        passage = world.Room('Passage', 'More Passage', 'Armory', 'Prison Cell', 'Nothing', 'Chest Plate')
        armory = world.Room('Armory', 'Passage', 'Nothing', 'Nothing', 'Nothing', 'Sword')

        room_map = {
                1: {'room': prison_cell,
                    'name': prison_cell.name,
                    'right': 2},

                2: {'room': passage,
                    'name': passage.name,
                    'left': 1,
                    'down': 3},

                3: {'room': armory,
                    'name': armory.name,
                    'up': 2}
            }

        game = True
        current_room = 1

        while game:

            player_input = term.player_input()

            if player_input == 'q' or player_input == 'quit':
                game = False

            elif player_input == 'h' or player_input == 'help':
                actions.player_help()

            elif player_input == 'v' or player_input == 'view':
                room_map[current_room]['room'].describe_room()

            elif player_input in room_map[current_room] or player_input[0] in room_map[current_room]:
                current_room = room_map[current_room][player_input]
                room_map[current_room]['room'].print_room()

            elif player_input == 'c' or player_input == 'clear':
                term.clear()