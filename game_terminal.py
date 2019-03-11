import os
import time
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
