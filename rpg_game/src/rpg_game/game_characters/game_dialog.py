# ------------------------------------------------------------------------------------------------------------------
# Text-Based RPG Game
# Author: Ryan Butler
# Developer notes: I am a massive fan of Star Wars and
# programming. Eager to learn Python, I thought it would
# be an awesome idea to develop a game, taking Star Wars
# as the inspiration.
# ------------------------------------------------------------------------------------------------------------------
"""
[Module for game dialog]
"""

import time

from game_mechanics import game_terminal as term


def start_prison_cell_dialog():
    """
    [Start of game in the Prison Cell - Dialog]
    """
    term.clear()
    time.sleep(2)
    term.wprint(f"you: uhhhh...ahhhh...")
    time.sleep(1)
    term.wprint(f"you: my head...what happened???")
    time.sleep(1)
    term.wprint(f"you: *standing up*")
    time.sleep(1)
    term.wprint(f"you: *looking around*")
    time.sleep(1)
