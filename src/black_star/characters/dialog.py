"""
Module for game dialog.
"""

import time

from black_star.tools import terminal as term


def start_prison_cell_dialog():
    """
    [Start of game in the Prison Cell - Dialog]
    """
    time.sleep(0.5)
    term.clear()
    time.sleep(2)
    term.wprint("you: uhhhh...ahhhh...")
    time.sleep(1)
    term.wprint("you: my head...what happened???")
    time.sleep(1)
    term.wprint("you: *standing up*")
    time.sleep(1)
    term.wprint("you: *looking around*")
    time.sleep(1)
