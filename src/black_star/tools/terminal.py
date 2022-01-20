"""Terminal API to print graphics, fonts and colors."""

import os

from rich.console import Console

console = Console()


def gprint(text):
    console.print(text, style="green")


def gbprint(text):
    console.print(text, style="bold green")


def wprint(text):
    console.print(text, style="white")


def wbprint(text):
    console.print(text, style="bold white")


def rprint(text):
    console.print(text, style="red")


def rbprint(text):
    console.print(text, style="bold red")


def yprint(text):
    console.print(text, style="yellow")


def ybprint(text):
    console.print(text, style="bold yellow")


def bprint(text):
    console.print(text, style="blue")


def bbprint(text):
    console.print(text, style="bold blue")


def pprint(text):
    console.print(text, style="purple")


def pbprint(text):
    console.print(text, style="bold purple")


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def player_hint():
    bprint("---Hint: Enter 'h' or 'help' for controls---")


def player_help():
    bprint("Help Menu:")
    bprint("- 'attack(a)' to attack an enemy in the area")
    bprint("- 'view(v)' to look around in this area")
    bprint("- 'map(m)' to look at the map of the world")
    bprint("- 'inspect(y)' to view item attributes")
    bprint("- 'take(t)' to take item into inventory")
    bprint("- 'status(s)' to view current player status, attributes and equipped gear")
    bprint("- 'inventory(i)' to view current player's inventory")
    bprint("- 'up(u)', 'down(d)', 'left(l)' and 'right(r)' to move around between areas")
    bprint("- 'clear(c)' to clear the terminal")
    bprint("- 'help(h)' to acess the help menu")
    bprint("- 'quit(q)' to quit the game")


def player_input(text):
    bprint(text)
    return str(console.input("[bold white]>>[/] ").lower())


if __name__ == "__main__":
    pass
