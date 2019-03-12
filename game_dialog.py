# ------------------------------------------------------------------------------------------------------------------
# Text-Based RPG Game
# Author: Ryan Butler
# Developer notes: I am a massive fan of Star Wars and programming. Eager to learn Python,
# I thought it would be an awesome idea to develop a game, taking Star Wars as the inspiration.
# ------------------------------------------------------------------------------------------------------------------
"""
[Module for game dialog]
"""

import os
import time
import game_terminal as term

def chapter1_prison_cell_dialog_intro(room_name):
    term.wprint(f'you: uhhhh...ahhhh...')
    time.sleep(2)
    term.wprint(f'you: my head...what happened???')
    time.sleep(2)
    term.wprint(f'you: *standing up*')
    time.sleep(2)
    term.wprint(f'you: *looking around*')
    term.bprint(f'You are in a {room_name}')
    time.sleep(2)