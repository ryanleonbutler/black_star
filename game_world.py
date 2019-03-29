# ------------------------------------------------------------------------------------------------------------------
# Text-Based RPG Game
# Author: Ryan Butler
# Developer notes: I am a massive fan of Star Wars and programming. Eager to learn Python,
# I thought it would be an awesome idea to develop a game, taking Star Wars as the inspiration.
# ------------------------------------------------------------------------------------------------------------------
"""
[Module for game world]
"""

import game_terminal as term

# class Room:
# TODO: Create Room class
class Room():

    def __init__(self, name, up, down, left, right, item):
        self.name = name
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.item = item

    def print_room(self):
        term.bprint(f'Moved to {self.name}')

    def describe_room(self):
        term.yprint(f"You are in a {self.name}")
        term.gprint(f"up: {self.up}\n"
                    f"down: {self.down}\n"
                    f"left: {self.left}\n"
                    f"right: {self.right}"
                    )
        term.pprint(f"There is a {self.item} on the ground")


prison_cell = Room('Prison Cell', 'Window', 'Nothing', 'Nothing', 'Passage', 'Key')
passage = Room('Passage', 'Barracks', 'Armory', 'Prison Cell', 'Nothing', 'Dirty Robe')
armory = Room('Armory', 'Passage', 'Nothing', 'Nothing', 'Nothing', 'Space Alloy Sword')
barracks = Room('Barracks', 'Nothing', 'Passage', 'Nothing', 'Nothing', '')


room_map = {
        1: {'room': prison_cell,
            'name': prison_cell.name,
            'up': prison_cell.up,
            'u': prison_cell.up,
            'down': prison_cell.down,
            'd': prison_cell.down,
            'left': prison_cell.left,
            'l':  prison_cell.left,
            'right': 2,
            'r': 2},

        2: {'room': passage,
            'name': passage.name,
            'up': 4,
            'u': 4,
            'down': 3,
            'd': 3,
            'left': 1,
            'l': 1,
            'right': passage.right,
            'r': passage.right},

        3: {'room': armory,
            'name': armory.name,
            'up': 2,
            'u': 2,
            'down': armory.down,
            'd': armory.down,
            'left': armory.left,
            'l': armory.left,
            'right': armory.right,
            'r': armory.right},

        4: {'room': barracks,
            'name': barracks.name,
            'up': barracks.up,
            'u': barracks.up,
            'down': 2,
            'd': 2,
            'left': barracks.left,
            'l': barracks.left,
            'right': barracks.right,
            'r': barracks.right}
    }

def view_map():
    term.wprint(
            "                      ______________  \n"
            "                     |              | \n"
            "                     |              | \n"
            "                     |    Armory    | \n"
            "                     |              | \n"
            "                     |______________| \n"
            "                             |        \n"
            " ______________       ______________  \n"
            "|              |     |              | \n"
            "|              |     |              | \n"
            "|  Prison Cell | --- |    Passage   | \n"
            "|    (Start)   |     |              | \n"
            "|______________|     |______________| \n"
            "                             |        \n"
            "                      ______________  \n"
            "                     |              | \n"
            "                     |              | \n"
            "                     |    Armory    | \n"
            "                     |              | \n"
            "                     |______________| \n"
                )
