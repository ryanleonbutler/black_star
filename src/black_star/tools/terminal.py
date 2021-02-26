"""Terminal API to print colors. Uses Rich."""

import os
from rich.console import Console

console = Console()


def gprint(text):
    console.print(text, style="bold green")


def wprint(text):
    console.print(text, style="bold white")


def rprint(text):
    console.print(text, style="bold red")


def yprint(text):
    console.print(text, style="bold yellow")


def bprint(text):
    console.print(text, style="bold blue")


def pprint(text):
    console.print(text, style="bold purple")


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
    value = str(console.input("[bold white]>>[/] ").lower())
    return value
