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
        NAME = ''
        LEVEL = 0
        HEALTH = 0
        ARMOR = 0
        DAMAGE = 0
        HEAD = 'None'
        CHEST = 'None'
        WEAPON = 'None'

    # class Object:
    # TODO: Create Object class
    class Object:
        NAME = ''
        ARMOR = 0
        DAMAGE = 0
        USE = ''
        Note = ''

    # class Inventory:
    # Inventory has 8 slots
    # TODO: Create Inventory class
    class Inventory:
        BAG = []

    # class Room:
    # TODO: Create Room class
    class Room:
        NAME = ''
        UP = ''
        DOWN = ''
        LEFT = ''
        RIGHT = ''
        OBJECT = []

    # class Enemy:
    # TODO: Create Enemy class
    class Enemy:
        NAME = ''
        LEVEL = 1
        HEALTH = 100
        ARMOR = 1
        DAMAGE = 1
    # Functions
    # ------------------------------------------------------------------------------------------------------------------

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
        os.system('cls' if os.name == 'nt' else 'clear')

    # TODO: Player Help
    def player_help():
        wprint('Help Menu:')
        wprint('- type \'look\' to look around in this area')
        wprint('- type \'take\' to take object into inventory')
        wprint('- type \'inventory\' to see what is in your bag, current gear on player and status')
        wprint('- type \'up\', \'down\', \'left\' and \'right\' to move around in this area')

    def character_create():
        bprint('Enter your character\'s name:')
        Character.NAME = input(str())
        Character.LEVEL = 1
        Character.HEALTH = 150
        Character.DAMAGE = 5
        Character.ARMOR = 1
        Character.HEAD = 'Empty'
        Character.CHEST = 'Tunic'
        Character.WEAPON = 'Empty'
        Inventory.BAG.append('Empty')
        clear()
        bprint(f'Welcome young {Character.NAME}, may the force be with you...')
        time.sleep(1)
        clear()
        time.sleep(1)

    def look_func():
        bprint(f'You are in a {Room.NAME}')
        yprint(f'Up is {Room.UP}')
        yprint(f'Down is {Room.DOWN}')
        yprint(f'To your left is {Room.LEFT}')
        yprint(f'To your right is {Room.RIGHT}')
        gprint(f'On the ground is {Room.OBJECT[:]}')

    def inventory_func():
        gprint(f'---INVENTORY---\nHead: {Character.HEAD}\tChest: {Character.CHEST}\n'
               f'Weapon: {Character.WEAPON}')
        gprint(f'Bag: {Inventory.BAG[:]}')
        bprint(f'\n---STATUS---\nLevel: {Character.LEVEL}\tHealth: {Character.HEALTH}')
        rprint(f'\n---ATTRIBUTES---\nDamage: {Character.DAMAGE}\tArmor: {Character.ARMOR}')

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
        clear()
        time.sleep(1)
        bprint('Long ago,'.center(width))
        bprint('in a star system very far away...\n'.center(width))
        time.sleep(1)
        yprint('Black Star'.center(width))
        wprint('A Text-Based Adventure'.center(width))
        time.sleep(1)
        wprint('Developed by Ryan Butler'.center(width))
        time.sleep(1)
        clear()
        yprint('Black Star'.center(width))
        wprint('A Text-Based Adventure\n\n'.center(width))
        wprint('MAIN MENU\n1. Play\n2. Quit')

        # Player menu option input
        menuOption = int(input())
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
                Room.NAME = 'Jail Cell'
                Room.UP = 'Door'
                Room.DOWN = 'Window'
                Room.LEFT = 'Nothing'
                Room.RIGHT = 'Nothing'
                Room.OBJECT = ['Key']
                wprint(f'{Character.NAME}: uhhhh...ahhhh...')
                time.sleep(1)
                wprint(f'{Character.NAME}: my head...what happened???')
                bprint(f'You are in a {Room.NAME}')
                time.sleep(2)
                bprint('Hint: type \'h\' or \'help\' for controls')
                while intro:
                    playerInput = str(input())
                    if playerInput == 'q' or playerInput == 'quit':
                        intro = False
                        playGame = False    # End the game
                    elif playerInput == 'h' or playerInput == 'help':
                        player_help()
                    elif playerInput == 'll' or playerInput == 'look':
                        look_func()
                    elif playerInput == 'i' or playerInput == 'inventory':
                        inventory_func()
                    elif playerInput == 'l' or playerInput == 'left':
                        yprint(f'You moved to {Room.LEFT}')
                    elif playerInput == 'r' or playerInput == 'right':
                        yprint(f'You moved to {Room.RIGHT}')
                    elif playerInput == 'u' or playerInput == 'up':
                        yprint(f'You moved to {Room.UP}')
                        if 'Key' in Inventory.BAG:
                            bprint('Unlock door with Key? (y/n)')
                            playerInput = str(input())
                            if playerInput == 'y':

                                # Chapter: Passage
                                yprint('Moved to Passage')
                                passage = True
                                Room.NAME = 'Passage'
                                Room.UP = 'Nothing'
                                Room.DOWN = 'Door - to Jail Cell[been there]'
                                Room.LEFT = 'Door'
                                Room.RIGHT = 'More Passage Way'
                                Room.OBJECT = ['Sword']
                                while passage:
                                    playerInput = str(input())
                                    if playerInput == 'q' or playerInput == 'quit':
                                        intro = False
                                        playGame = False  # End the game
                                    elif playerInput == 'h' or playerInput == 'help':
                                        player_help()
                                    elif playerInput == 'll' or playerInput == 'look':
                                        look_func()
                                    elif playerInput == 'i' or playerInput == 'inventory':
                                        inventory_func()
                                    elif playerInput == 'l' or playerInput == 'left':
                                        if Room.LEFT == 'Nothing':
                                            bprint('You cannot move into Nothing')
                                        else:
                                            yprint(f'You moved to {Room.LEFT}')
                                    elif playerInput == 'r' or playerInput == 'right':
                                        if Room.RIGHT == 'Nothing':
                                            bprint('You cannot move into Nothing')
                                        else:
                                            bprint(f'You moved to {Room.RIGHT}')
                                    elif playerInput == 'u' or playerInput == 'up':
                                        if Room.UP == 'Nothing':
                                            bprint('You cannot move into Nothing')
                                        else:
                                            yprint(f'You moved to {Room.UP}')
                                    elif playerInput == 'd' or playerInput == 'down':
                                        if Room.DOWN == 'Nothing':
                                            bprint('You cannot move into Nothing')
                                        else:
                                            yprint(f'You moved to {Room.DOWN}')
                                    else:
                                        passage = False
                            else:
                                intro = True
                        else:
                            bprint('The Door is locked and needs a key')
                    elif playerInput == 'd' or playerInput == 'down':
                        yprint(f'You looked out of {Room.DOWN}, it is dark...')
                    elif playerInput == 't' or playerInput == 'take':
                        gprint(f'You picked up {Room.OBJECT[-1:]}')
                        Inventory.BAG.append(Room.OBJECT[-1:])
                        Room.OBJECT.pop()
                    else:
                        intro = True
        # Menu Item 2
        # Quit game option
        elif menuOption == 2:
            clear()
            game = False
        else:
            game = True
