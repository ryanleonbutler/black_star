# ------------------------------------------------------------------------------------------------------------------
# Text-Based RPG Game
# Author: Ryan Butler
# Developer notes: I am a massive fan of Star Wars and
# programming. Eager to learn Python, I thought it would
# be an awesome idea to develop a game, taking Star Wars
# as the inspiration.
# ------------------------------------------------------------------------------------------------------------------
"""
[Module for game custom text terminal output]
"""
# Library imports
# https://pypi.org/project/colorama/

import os
import colorama
from colorama import Back
from colorama import Fore
from colorama import Style
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
    bprint("---Hint:  'h' or 'help' for controls---")


def player_help():
    bprint("Help Menu:")
    bprint("- 'view(v)' to look around in this area")
    bprint("- 'map(m)' to look at the map of the world")
    bprint("- 'inspect(y)' to view item attributes")
    bprint("- 'take(t)' to take item into inventory")
    bprint("- 'status(s)' to view current player status, attributes and equipped gear")
    bprint("- 'inventory(i)' to view current player's inventory")
    bprint(
        "- 'up(u)', 'down(d)', 'left(l)' and 'right(r)' to move around between areas"
    )
    bprint("- 'clear(c)' to clear the terminal")
    bprint("- 'quit(q)' to quit the game")


def player_input():
    value = str(input("> ").lower())
    return value
