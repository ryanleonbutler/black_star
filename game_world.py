<<<<<<< HEAD
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
=======
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
class Room:
    def __init__(self, name, up, down, left, right, item):
        self.name = name
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.item = item

    def print_room(self):
        term.bprint(f"Moved to {self.name}")

    def describe_room(self):
        term.yprint(f"You are in a {self.name}")
        term.gprint(
            f"up: {self.up}\n"
            f"down: {self.down}\n"
            f"left: {self.left}\n"
            f"right: {self.right}"
        )
        if self.item == "":
            term.pprint(f"Nothing on the ground")
        else:
            term.pprint(f"There is a {self.item} on the ground")


prison_cell = Room("Prison Cell", "Window", "Nothing", "Nothing", "Passage", "Key")
passage = Room("Passage", "Sleeping Quarters", "Armory", "Prison Cell", "Lab", "Dirty Robe")
armory = Room("Armory", "Passage", "Nothing", "Nothing", "Nothing", "Space Alloy Sword")
sleep_quar = Room("Sleeping Quarters", "Food Hall", "Passage", "Nothing", "Nothing", "")
food_hall = Room("Food Hall", "Nothing", "Sleeping Quarters", "Nothing", "Nothing", "")
lab = Room("Lab", "Nothing", "Nothing", "Passage", "Passenger Area", "")
pass_area = Room("Passenger Area", "Blaster Turret", "Cargo Hold", "Lab", "Crew Area", "")
cargo_hold = Room("Cargo Hold", "Passenger Area", "Nothing", "Nothing", "Nothing", "")
blaster_turret = Room("Blaster Turret", "Nothing", "Passenger Area", "Nothing", "Nothing", "")
crew_area = Room("Crew Area", "Nothing", "Nothing", "Passenger Area", "Cockpit", "")
cockpit = Room("Cockpit", "Nothing", "Nothing", "Crew Area", "Nothing", "")

room_map = {
    1: {
        "room": prison_cell,
        "name": prison_cell.name,
        "up": prison_cell.up,
        "u": prison_cell.up,
        "down": prison_cell.down,
        "d": prison_cell.down,
        "left": prison_cell.left,
        "l": prison_cell.left,
        "right": 2,
        "r": 2,
    },
    2: {
        "room": passage,
        "name": passage.name,
        "up": 4,
        "u": 4,
        "down": 3,
        "d": 3,
        "left": 1,
        "l": 1,
        "right": 6,
        "r": 6,
    },
    3: {
        "room": armory,
        "name": armory.name,
        "up": 2,
        "u": 2,
        "down": armory.down,
        "d": armory.down,
        "left": armory.left,
        "l": armory.left,
        "right": armory.right,
        "r": armory.right,
    },
    4: {
        "room": sleep_quar,
        "name": sleep_quar.name,
        "up": 5,
        "u": 5,
        "down": 2,
        "d": 2,
        "left": sleep_quar.left,
        "l": sleep_quar.left,
        "right": sleep_quar.right,
        "r": sleep_quar.right,
    },
    5: {
        "room": food_hall,
        "name": food_hall.name,
        "up": food_hall.up,
        "u": food_hall.up,
        "down": 4,
        "d": 4,
        "left": food_hall.left,
        "l": food_hall.left,
        "right": food_hall.right,
        "r": food_hall.right,
    },
    6: {
        "room": lab,
        "name": lab.name,
        "up": lab.up,
        "u": lab.up,
        "down": 2,
        "d": 2,
        "left": lab.left,
        "l": lab.left,
        "right": 7,
        "r": 7,
    },
    7: {
        "room": pass_area,
        "name": pass_area.name,
        "up": 9,
        "u": 9,
        "down": 8,
        "d": 8,
        "left": 6,
        "l": 6,
        "right": 10,
        "r": 10,
    },
    8: {
        "room": cargo_hold,
        "name": cargo_hold.name,
        "up": 7,
        "u": 7,
        "down": cargo_hold.down,
        "d": cargo_hold.down,
        "left": cargo_hold.left,
        "l": cargo_hold.left,
        "right": cargo_hold.right,
        "r": cargo_hold.right,
    },
    9: {
        "room": blaster_turret,
        "name": blaster_turret.name,
        "up": blaster_turret.up,
        "u": blaster_turret.up,
        "down": 7,
        "d": 7,
        "left": blaster_turret.left,
        "l": blaster_turret.left,
        "right": blaster_turret.right,
        "r": blaster_turret.right,
    },
    10: {
        "room": crew_area,
        "name": crew_area.name,
        "up": crew_area.up,
        "u": crew_area.up,
        "down": crew_area.down,
        "d": crew_area.down,
        "left": 7,
        "l": 7,
        "right": 11,
        "r": 11,
    },
    11: {
        "room": cockpit,
        "name": cockpit.name,
        "up": cockpit.up,
        "u": cockpit.up,
        "down": cockpit.down,
        "d": cockpit.down,
        "left": 10,
        "l": 10,
        "right": cockpit.right,
        "r": cockpit.right,
    },
}


def view_map():
    term.wprint(
        """\
                      ______________
                     |              |
                     |              |
                     |   Food Hall  |
                     |              |
                     |______________|
                             |
                      ______________                            ______________
                     |              |                          |              |
                     |   Sleeping   |                          |    Blaster   |
                     |   Quarters   |                          |    Turret    |
                     |              |                          |              |
                     |______________|                          |______________|
                             |                                         |
 ______________       ______________       ______________       ______________       ______________       ______________
|              |     |              |     |              |     |              |     |              |     |              |
|  Prison Cell |     |              |     |              |     |   Passenger  |     |              |     |              |
|    (Start)   | --- |    Passage   | --- |      Lab     | --- |     Area     | --- |   Crew Area  | --- |   Cockpit    |
|              |     |              |     |              |     |              |     |              |     |              |
|______________|     |______________|     |______________|     |______________|     |______________|     |______________|
                             |                                         |
                      ______________                            ______________
                     |              |                          |              |
                     |              |                          |              |
                     |    Armory    |                          |  Cargo Hold  |
                     |              |                          |              |
                     |______________|                          |______________|
"""
    )
>>>>>>> dec7fd7efd0b50d5c0b9ee672c8c00a6c7dd2ab2
