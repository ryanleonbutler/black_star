"""
Module for the game's start and player menu.
"""

import time

from tools import terminal as term


def game_menu() -> str:
    """
    [Menu function, to start game or quit game.]
    """
    term.clear()
    term.yprint("Black Star")
    term.wprint("A Text-Based Adventure\n\n")
    term.wprint("MAIN MENU\n1. Play\n2. Quit")

    while True:
        player_input = term.player_input("")
        # Start game menu option
        if player_input == "1" or player_input.lower == "start":
            term.bprint("Get ready, starting game...")
            time.sleep(2)
            term.clear()
            break
        # Quit game menu option
        elif player_input == "2" or player_input.lower == "quit":
            term.bprint("Goodbye, see you again soon...")
            time.sleep(2)
            term.clear()
            break
        else:
            term.rprint("Please enter correct menu option...\n")
            continue

    return player_input
