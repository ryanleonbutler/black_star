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
        term.yprint(f'You moved to {self.name}')

    def describe_room(self):
        term.yprint(f"You are in a {self.name}")
        term.gprint(f"up: {self.up}\n"
                    f"down: {self.down}\n"
                    f"left: {self.left}\n"
                    f"right: {self.right}"
                    )
        term.pprint(f"There is a {self.item} on the ground")

