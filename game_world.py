# ------------------------------------------------------------------------------------------------------------------
# Text-Based RPG Game
# Author: Ryan Butler
# Developer notes: I am a massive fan of Star Wars and programming. Eager to learn Python,
# I thought it would be an awesome idea to develop a game, taking Star Wars as the inspiration.
# ------------------------------------------------------------------------------------------------------------------
"""
[Module for game world]
"""

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

    def describe_room(self):
        term.bprint(f"You are in a {name}")
        term.yprint(f"Up: {up}")
        term.yprint(f"Down: {down}")
        term.yprint(f"Left: {left}")
        term.yprint(f"Right: {right}")
        term.gprint(f"Ground: {item}")