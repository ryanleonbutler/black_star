# ------------------------------------------------------------------------------------------------------------------
# Text-Based RPG Game
# Author: Ryan Butler
# Developer notes: I am a massive fan of Star Wars and programming. Eager to learn Python,
# I thought it would be an awesome idea to develop a game, taking Star Wars as the inspiration.
# ------------------------------------------------------------------------------------------------------------------
"""
[Module for game custom text terminal output]
"""
# Library imports
# https://pypi.org/project/colorama/

import os
import time
import colorama
from colorama import Fore, Back, Style
from colorama import init

init(autoreset=True)

def gprint(sentence):
    print(Style.BRIGHT + Fore.GREEN + sentence)


def wprint(sentence):
    print(Style.BRIGHT + Fore.WHITE + sentence)


def rprint(sentence):
    print(Style.BRIGHT + Fore.RED + sentence)


def yprint(sentence):
    print(Style.BRIGHT + Fore.YELLOW + sentence)


def bprint(sentence):
    print(Style.BRIGHT + Fore.CYAN + sentence)


def pprint(sentence):
    print(Style.BRIGHT + Fore.MAGENTA + sentence)


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def player_hint():
    bprint('---Hint: type \'h\' or \'help\' for controls---')


def player_help():
    bprint("Help Menu:")
    bprint("- type 'view(v)' to look around in this area")
    bprint("- type 'map(m)' to look at the map of the world")
    bprint("- type 'take(t)' to take object into inventory")
    bprint(
        "- type 'inventory(i)' to see what is in your bag, current gear on player and status"
    )
    bprint("- type 'up(u)', 'down(d)', 'left(l)' and 'right(r)' to move around between areas")
    bprint("- type 'clear(c)' to clear the terminal")


def player_input():
    value = str(input("> ").lower())
    return value