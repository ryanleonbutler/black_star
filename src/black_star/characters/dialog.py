"""
Module for game dialog.
"""

import time

from tools import terminal as term


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
