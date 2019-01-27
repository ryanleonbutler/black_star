# ------------------------------------------------------------------------------------------------------------------
# Text-Based RPG Game
# Author: Ryan Butler
# Developer notes: I am a massive fan of Star Wars and programming. Eager to learn Python, I thought it would be an
# awesome idea to develop a game, taking Star Wars as the inspiration.
# ------------------------------------------------------------------------------------------------------------------
# Library imports
# https://pypi.org/project/colorama/

import os
import time
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

if __name__ == '__main__':
    # Classes
    # ------------------------------------------------------------------------------------------------------------------
    # class Character:
    # TODO: Create Character class
    class Character:
        NAME = ""

    # class Inventory:
    # TODO: Create Inventory class

    # class Object:
    # TODO: Create Object class
    class Object:
        NAME = 'Piece of paper'
        ARMOR = 0
        DAMAGE = 0
        WEAR = 0
        USE = 'Read'
        Note = 'Blahblahblah'

    # class Room:
    # TODO: Create Room class
    class Room:
        NAME = 'Small Jail Cell'
        GROUND = Object.NAME

    # class Enemy:
    # TODO: Create Enemy class

    # Functions
    # ------------------------------------------------------------------------------------------------------------------
    def gprint(sentence):
        print(Fore.GREEN + sentence)

    def wprint(sentence):
        print(Fore.WHITE + sentence)

    def rprint(sentence):
        print(Fore.RED + sentence)

    def yprint(sentence):
        print(Style.BRIGHT + Fore.YELLOW + sentence)

    def bprint(sentence):
        print(Style.BRIGHT + Fore.CYAN + sentence)

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    # TODO: Player Help
    def player_help():
        wprint('Help Menu:')
        wprint('- type \'look\' to look around in this area')
        wprint('- type \'take\' to take object into inventory')
        wprint('- type \'up\', \'down\', \'left\' and \'right\' to move around in this area')

    def character_create():
        gprint('Enter your character\'s name:')
        char_name = input(str())
        char_level = 1
        clear()
        bprint(f'Welcome young {char_name}, may the force be with you...')
        time.sleep(1)
        bprint(f'You are currently level: {char_level}')
        time.sleep(2)
        clear()
        time.sleep(1)

    # Constants
    # ------------------------------------------------------------------------------------------------------------------
    # Variables
    # ------------------------------------------------------------------------------------------------------------------
    width = os.get_terminal_size().columns
    game = True         # While variable for game loop
    options = False     # Option menu loop for different setting in the game

    # Starting the game
    # ------------------------------------------------------------------------------------------------------------------
    clear()
    time.sleep(1)

    # Start of game loop
    while game:

        # Welcome note where games starts
        yprint('Welcome to Black Star - TEXT'.center(width))
        time.sleep(1)
        bprint('A Classic Text-Based Adventure Game!\n\n'.center(width))
        wprint('MAIN MENU')
        wprint('1. Play')
        wprint('2. Options')
        wprint('3. Quit')

        # Player menu option input
        menuOption = int(input())

        # Menu Item 1
        # Playing the game
        if menuOption == 1:
            clear()
            game = True
            playGame = True
            gameChapter = 'Intro'
            while playGame:
                # Chapter: Intro
                time.sleep(1)
                bprint('Long ago,'.center(width))
                bprint('in a star system very far away...\n'.center(width))
                time.sleep(1)
                yprint('Black Star'.center(width))
                wprint('A Text-Based Adventure\n'.center(width))
                time.sleep(1)
                wprint('Developed by Ryan Butler'.center(width))
                time.sleep(1)
                clear()

                # Character Creation
                character_create()

                # Chapter: Intro
                wprint('You: uhhhh...ahhhh...')
                time.sleep(1)
                wprint('You: my head...what happened???')
                bprint('Game: You are in a small room')
                time.sleep(1)
                playerInput = str(input())
                if playerInput == 'q' or playerInput == 'quit' or playerInput == 'Quit':
                    playGame = False    # End the game
                elif playerInput == 'h' or playerInput == 'help' or playerInput == 'Help':
                    player_help()
                    playGame = True

        # Menu Item 2
        # Options menu
        elif menuOption == 2:
            game = True
            options = True
            while options:
                wprint('Options: \n1. Difficulty \n2. Text Color \n3. Back to Main Menu')
                optionInput = int(input())
                if optionInput == 1:
                    options = True
                elif optionInput == 2:
                    colorMenu = True
                    # Display text - color menu
                    while colorMenu:
                        wprint('Text Colors: \n1. Purple \n2. Blue \n3. Green \n4. Default\n5. Back to Options')
                        colorInput = int(input())
                        if colorInput == 1:
                            userText = Fore.MAGENTA
                            colorMenu = False
                        elif colorInput == 2:
                            userText = Fore.BLUE
                            colorMenu = False
                        elif colorInput == 3:
                            userText = Fore.GREEN
                            colorMenu = False
                        elif colorInput == 4:
                            userText = Fore.WHITE
                            colorMenu = False
                        else:
                            colorMenu = True
                elif optionInput == 3:
                    clear()
                    options = False
                else:
                    options = True

        # Menu Item 3
        # Quit game option
        elif menuOption == 3:
            clear()
            game = False
        else:
            game = True
