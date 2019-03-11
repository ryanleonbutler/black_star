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
import game_terminal as gt
import game_world as gw
import game_play as gp

if __name__ == "__main__":
    # Classes
    # -------------------------------------------------------------------------------------------

    # Functions
    # -------------------------------------------------------------------------------------------

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
    gt.clear()
    time.sleep(1)

    # Start of game loop
    while game:
        # Welcome note where games starts
        gt.clear()
        time.sleep(1)
        gt.bprint("Long ago,")
        gt.bprint("in a star system very far away...\n")
        time.sleep(1)
        gt.yprint("Black Star")
        gt.wprint("A Text-Based Adventure")
        time.sleep(1)
        gt.wprint("Developed by Ryan Butler")
        time.sleep(3)
        gt.clear()
        gt.yprint("Black Star")
        gt.wprint("A Text-Based Adventure\n\n")
        gt.wprint("MAIN MENU\n1. Play\n2. Quit")

        # Player menu option input
        menuOption = int(input("> "))
        # Menu Item 1
        # Playing the game
        if menuOption == 1:
            gt.clear()
            game = True
            playGame = True
            while playGame:
                # Chapter: Intro
                # Character Creation
                gp.character_create()
                character = gp.character_create(character_profile)
                # Chapter: Jail Cell
                intro = True
                gw.create_room_func(
                    "Jail Cell", "Window", "Door", "Nothing", "Nothing", "Key"
                )
                gt.wprint(f"{name}: uhhhh...ahhhh...")
                time.sleep(1)
                gt.wprint(f"{name}: my head...what happened???")
                gt.bprint(f"You are in a {Room.NAME}")
                time.sleep(1)
                gt.bprint("Hint: type 'h' or 'help' for controls")

                # Start of loop
                while intro:
                    player_input = str(input("> "))
                    if player_input == "q" or player_input == "quit":
                        intro = False
                        playGame = False  # End the game
                    elif player_input == "h" or player_input == "help":
                        gp.player_help()
                    elif player_input == "ll" or player_input == "look":
                        gp.look_func()
                    elif player_input == "i" or player_input == "inventory":
                        gp.inventory_func()
                    elif player_input == "t" or player_input == "take":
                        gt.gprint(f"You picked up {Room.OBJECT[-1]}")
                        Inventory.BAG[-1] = Room.OBJECT[-1]
                        Room.OBJECT[-1] = ""
                    elif player_input == "l" or player_input == "left":
                        if Room.LEFT == "Nothing":
                            gt.bprint("You cannot move into Nothing")
                        else:
                            gt.yprint(f"You moved to {Room.LEFT}")
                    elif player_input == "r" or player_input == "right":
                        if Room.RIGHT == "Nothing":
                            gt.bprint("You cannot move into Nothing")
                        else:
                            gt.yprint(f"You moved to {Room.RIGHT}")
                    elif player_input == "u" or player_input == "up":
                        gt.yprint(f"You looked out of the {Room.UP}, it is dark...")
                    elif player_input == "d" or player_input == "down":
                        gt.yprint(f"You moved to {Room.DOWN}")
                        if "Key" in Inventory.BAG:
                            gt.bprint("Unlock door with Key? (y/n)")
                            player_input = str(input())
                            if player_input == "y":
                                Inventory.BAG[-1] = ""

                                # Chapter: Passage
                                gt.yprint("Moved to Passage")
                                passage = True
                                gw.create_room_func(
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
                                        gp.player_help()
                                    elif player_input == "ll" or player_input == "look":
                                        gp.look_func()
                                    elif (
                                        player_input == "i"
                                        or player_input == "inventory"
                                    ):
                                        gp.inventory_func()
                                    elif player_input == "l" or player_input == "left":
                                        if Room.LEFT == "Nothing":
                                            gt.bprint("You cannot move into Nothing")
                                        else:
                                            gt.yprint(f"You moved to {Room.LEFT}")

                                            # Chapter: Passage2
                                            passage2 = True
                                            gp.create_room_func(
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
                                                    gp.player_help()
                                                elif (
                                                    player_input == "ll"
                                                    or player_input == "look"
                                                ):
                                                    gp.look_func()
                                                elif (
                                                    player_input == "i"
                                                    or player_input == "inventory"
                                                ):
                                                    gp.inventory_func()
                                                elif (
                                                    player_input == "l"
                                                    or player_input == "left"
                                                ):
                                                    if Room.LEFT == "Nothing":
                                                        gt.bprint(
                                                            "You cannot move into Nothing"
                                                        )
                                                    else:
                                                        gt.yprint(
                                                            f"You moved to {Room.LEFT}"
                                                        )
                                                elif (
                                                    player_input == "r"
                                                    or player_input == "right"
                                                ):
                                                    if Room.RIGHT == "Nothing":
                                                        gt.bprint(
                                                            "You cannot move into Nothing"
                                                        )
                                                    else:
                                                        gt.bprint(
                                                            f"You moved to {Room.RIGHT}"
                                                        )
                                                        passage2 = False
                                                        passage = True
                                                elif (
                                                    player_input == "u"
                                                    or player_input == "up"
                                                ):
                                                    if Room.UP == "Nothing":
                                                        gt.bprint(
                                                            "You cannot move into Nothing"
                                                        )
                                                    else:
                                                        gt.yprint(
                                                            f"You moved to {Room.UP}"
                                                        )
                                                elif (
                                                    player_input == "d"
                                                    or player_input == "down"
                                                ):
                                                    if Room.DOWN == "Nothing":
                                                        gt.bprint(
                                                            "You cannot move into Nothing"
                                                        )
                                                    else:
                                                        gt.yprint(
                                                            f"You moved to {Room.DOWN}"
                                                        )
                                                else:
                                                    passage2 = True

                                    elif player_input == "r" or player_input == "right":
                                        if Room.RIGHT == "Nothing":
                                            gt.bprint("You cannot move into Nothing")
                                        else:
                                            gt.bprint(f"You moved to {Room.RIGHT}")
                                    elif player_input == "u" or player_input == "up":
                                        if Room.UP == "Nothing":
                                            gt.bprint("You cannot move into Nothing")
                                        else:
                                            gt.yprint(f"You moved to {Room.UP}")
                                    elif player_input == "d" or player_input == "down":
                                        if Room.DOWN == "Nothing":
                                            gt.bprint("You cannot move into Nothing")
                                        else:
                                            gt.yprint(f"You moved to {Room.DOWN}")
                                            passage = False
                                            passage2 = False
                                            intro = True
                                    else:
                                        passage = True
                        else:
                            gt.bprint("The Door is locked and needs a key")
                    else:
                        intro = True

        # Menu Item 2
        # Quit game option
        elif menuOption == 2:
            gt.clear()
            game = False
        else:
            game = True
