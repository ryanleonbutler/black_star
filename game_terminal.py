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


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def player_hint():
    bprint('---Hint: type \'h\' or \'help\' for controls---')


def player_input():
    value = str(input("> "))
    return value


