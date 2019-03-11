# ------------------------------------------------------------------------------------------------------------------
# Text-Based RPG Game
# Author: Ryan Butler
# Developer notes: I am a massive fan of Star Wars and programming. Eager to learn Python,
# I thought it would be an awesome idea to develop a game, taking Star Wars as the inspiration.
# ------------------------------------------------------------------------------------------------------------------
# Library imports
# https://pypi.org/project/colorama/

import os

import time
from colorama import Fore, Back, Style
from colorama import init

init(autoreset=True)

if __name__ == "__main__":
    # Classes
    # -------------------------------------------------------------------------------------------
    # class Character:
    # TODO: Create Character class
    class Character:
        NAME = ""
        LEVEL = 0
        HEALTH = 0
        ARMOR = 0
        DAMAGE = 0
        HEAD = "None"
        CHEST = "None"
        WEAPON = "None"

    # class Object:
    # TODO: Create Object class
    class Object:
        NAME = ""
        ARMOR = 0
        DAMAGE = 0
        USE = ""
        Note = ""

    # class Inventory:
    # Inventory has 8 slots
    # TODO: Create Inventory class
    class Inventory:
        BAG = [""]

    # class Room:
    # TODO: Create Room class
    class Room:
        NAME = ""
        UP = ""
        DOWN = ""
        LEFT = ""
        RIGHT = ""
        OBJECT = [""]

    # class Enemy:
    # TODO: Create Enemy class
    class Enemy:
        NAME = ""
        LEVEL = 1
        HEALTH = 100
        ARMOR = 1
        DAMAGE = 1

    # Functions
    # -------------------------------------------------------------------------------------------

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

    # TODO: Player Help
    def player_help():
        wprint("Help Menu:")
        wprint("- type 'look' to look around in this area")
        wprint("- type 'take' to take object into inventory")
        wprint(
            "- type 'inventory' to see what is in your bag, current gear on player and status"
        )
        wprint("- type 'up', 'down', 'left' and 'right' to move around in this area")

    def character_create():
        bprint("Enter your character's name:")
        Character.NAME = input(str("> "))
        Character.LEVEL = 1
        Character.HEALTH = 150
        Character.DAMAGE = 5
        Character.ARMOR = 1
        Character.HEAD = "Empty"
        Character.CHEST = "Tunic"
        Character.WEAPON = "Empty"
        Inventory.BAG[-1] = "Empty"
        clear()
        bprint(f"Welcome young {Character.NAME}, may the force be with you...")
        time.sleep(1)
        clear()
        time.sleep(1)

    def look_func():
        bprint(f"You are in a {Room.NAME}")
        yprint(f"Up: {Room.UP}")
        yprint(f"Down: {Room.DOWN}")
        yprint(f"Left: {Room.LEFT}")
        yprint(f"Right: {Room.RIGHT}")
        gprint(f"Ground: {Room.OBJECT[-1]}")

    def inventory_func():
        gprint(
            f"\n---INVENTORY---\nHead: {Character.HEAD}\tChest: {Character.CHEST}\n"
            f"Weapon: {Character.WEAPON}"
        )
        gprint(f"Bag: {Inventory.BAG[-1]}")
        bprint(f"\n---STATUS---\nLevel: {Character.LEVEL}\tHealth: {Character.HEALTH}")
        rprint(
            f"\n---ATTRIBUTES---\nDamage: {Character.DAMAGE}\tArmor: {Character.ARMOR}\n"
        )

    def create_room_func(name, up, down, left, right, room_object):
        Room.NAME = name
        Room.UP = up
        Room.DOWN = down
        Room.LEFT = left
        Room.RIGHT = right
        Room.OBJECT[-1] = room_object

    # Constants
    # -------------------------------------------------------------------------------------------
    # Variables
    # -------------------------------------------------------------------------------------------
    #    if os.name == 'nt':
    #        width = os.get_terminal_size().columns
    #    else:
    #        width = os.popen('stty size', 'r').read().split()

    game = True  # While variable for game loop
    options = False  # Option menu loop for different setting in the game

    # Starting the game
    # -------------------------------------------------------------------------------------------
    clear()
    time.sleep(1)

    # Start of game loop
    while game:
        # Welcome note where games starts
        clear()
        time.sleep(1)
        bprint("Long ago,")
        bprint("in a star system very far away...\n")
        time.sleep(1)
        yprint("Black Star")
        wprint("A Text-Based Adventure")
        time.sleep(1)
        wprint("Developed by Ryan Butler")
        time.sleep(3)
        clear()
        yprint("Black Star")
        wprint("A Text-Based Adventure\n\n")
        wprint("MAIN MENU\n1. Play\n2. Quit")

        # Player menu option input
        menuOption = int(input("> "))
        # Menu Item 1
        # Playing the game
        if menuOption == 1:
            clear()
            game = True
            playGame = True
            while playGame:
                # Chapter: Intro
                # Character Creation
                character_create()

                # Chapter: Jail Cell
                intro = True
                create_room_func(
                    "Jail Cell", "Window", "Door", "Nothing", "Nothing", "Key"
                )
                wprint(f"{Character.NAME}: uhhhh...ahhhh...")
                time.sleep(1)
                wprint(f"{Character.NAME}: my head...what happened???")
                bprint(f"You are in a {Room.NAME}")
                time.sleep(1)
                bprint("Hint: type 'h' or 'help' for controls")

                # Start of loop
                while intro:
                    player_input = str(input("> "))
                    if player_input == "q" or player_input == "quit":
                        intro = False
                        playGame = False  # End the game
                    elif player_input == "h" or player_input == "help":
                        player_help()
                    elif player_input == "ll" or player_input == "look":
                        look_func()
                    elif player_input == "i" or player_input == "inventory":
                        inventory_func()
                    elif player_input == "t" or player_input == "take":
                        gprint(f"You picked up {Room.OBJECT[-1]}")
                        Inventory.BAG[-1] = Room.OBJECT[-1]
                        Room.OBJECT[-1] = ""
                    elif player_input == "l" or player_input == "left":
                        if Room.LEFT == "Nothing":
                            bprint("You cannot move into Nothing")
                        else:
                            yprint(f"You moved to {Room.LEFT}")
                    elif player_input == "r" or player_input == "right":
                        if Room.RIGHT == "Nothing":
                            bprint("You cannot move into Nothing")
                        else:
                            yprint(f"You moved to {Room.RIGHT}")
                    elif player_input == "u" or player_input == "up":
                        yprint(f"You looked out of the {Room.UP}, it is dark...")
                    elif player_input == "d" or player_input == "down":
                        yprint(f"You moved to {Room.DOWN}")
                        if "Key" in Inventory.BAG:
                            bprint("Unlock door with Key? (y/n)")
                            player_input = str(input())
                            if player_input == "y":
                                Inventory.BAG[-1] = ""

                                # Chapter: Passage
                                yprint("Moved to Passage")
                                passage = True
                                create_room_func(
                                    "Passage",
                                    "Nothing",
                                    "Jail Cell",
                                    "More Passage",
                                    "Nothing",
                                    "Rusty Sword",
                                )
                                while passage:
                                    player_input = str(input("> "))
                                    if player_input == "q" or player_input == "quit":
                                        passage = False
                                        intro = False
                                        playGame = False  # End the game
                                    elif player_input == "h" or player_input == "help":
                                        player_help()
                                    elif player_input == "ll" or player_input == "look":
                                        look_func()
                                    elif (
                                        player_input == "i"
                                        or player_input == "inventory"
                                    ):
                                        inventory_func()
                                    elif player_input == "l" or player_input == "left":
                                        if Room.LEFT == "Nothing":
                                            bprint("You cannot move into Nothing")
                                        else:
                                            yprint(f"You moved to {Room.LEFT}")

                                            # Chapter: Passage2
                                            passage2 = True
                                            create_room_func(
                                                "End of Passage",
                                                "Nothing",
                                                "Nothing",
                                                "Back to the First Passage",
                                                "Nothing",
                                                "",
                                            )
                                            while passage2:
                                                player_input = str(input("> "))
                                                if (
                                                    player_input == "q"
                                                    or player_input == "quit"
                                                ):
                                                    passage2 = False
                                                    passage = False
                                                    intro = False
                                                    playGame = False  # End the game
                                                elif (
                                                    player_input == "h"
                                                    or player_input == "help"
                                                ):
                                                    player_help()
                                                elif (
                                                    player_input == "ll"
                                                    or player_input == "look"
                                                ):
                                                    look_func()
                                                elif (
                                                    player_input == "i"
                                                    or player_input == "inventory"
                                                ):
                                                    inventory_func()
                                                elif (
                                                    player_input == "l"
                                                    or player_input == "left"
                                                ):
                                                    if Room.LEFT == "Nothing":
                                                        bprint(
                                                            "You cannot move into Nothing"
                                                        )
                                                    else:
                                                        yprint(
                                                            f"You moved to {Room.LEFT}"
                                                        )
                                                elif (
                                                    player_input == "r"
                                                    or player_input == "right"
                                                ):
                                                    if Room.RIGHT == "Nothing":
                                                        bprint(
                                                            "You cannot move into Nothing"
                                                        )
                                                    else:
                                                        bprint(
                                                            f"You moved to {Room.RIGHT}"
                                                        )
                                                        passage2 = False
                                                        passage = True
                                                elif (
                                                    player_input == "u"
                                                    or player_input == "up"
                                                ):
                                                    if Room.UP == "Nothing":
                                                        bprint(
                                                            "You cannot move into Nothing"
                                                        )
                                                    else:
                                                        yprint(
                                                            f"You moved to {Room.UP}"
                                                        )
                                                elif (
                                                    player_input == "d"
                                                    or player_input == "down"
                                                ):
                                                    if Room.DOWN == "Nothing":
                                                        bprint(
                                                            "You cannot move into Nothing"
                                                        )
                                                    else:
                                                        yprint(
                                                            f"You moved to {Room.DOWN}"
                                                        )
                                                else:
                                                    passage2 = True

                                    elif player_input == "r" or player_input == "right":
                                        if Room.RIGHT == "Nothing":
                                            bprint("You cannot move into Nothing")
                                        else:
                                            bprint(f"You moved to {Room.RIGHT}")
                                    elif player_input == "u" or player_input == "up":
                                        if Room.UP == "Nothing":
                                            bprint("You cannot move into Nothing")
                                        else:
                                            yprint(f"You moved to {Room.UP}")
                                    elif player_input == "d" or player_input == "down":
                                        if Room.DOWN == "Nothing":
                                            bprint("You cannot move into Nothing")
                                        else:
                                            yprint(f"You moved to {Room.DOWN}")
                                            passage = False
                                            passage2 = False
                                            intro = True
                                    else:
                                        passage = True
                        else:
                            bprint("The Door is locked and needs a key")
                    else:
                        intro = True

        # Menu Item 2
        # Quit game option
        elif menuOption == 2:
            clear()
            game = False
        else:
            game = True
