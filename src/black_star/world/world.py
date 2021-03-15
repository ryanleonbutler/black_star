"""
Module for game world.
"""

from tools import terminal as term
from world import items


# class Room:
class Room:
    def __init__(self, name, up, down, left, right, item):
        self.name = name
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.item = item

    def print_room(self):
        term.bprint(f"-> Moved to {self.name}")

    def describe_room(self):
        term.yprint(f"* You are in a {self.name}")

        if self.up == "nothing":
            term.wprint(f"up: {self.up}")
        else:
            term.gprint(f"up: {self.up}")

        if self.down == "nothing":
            term.wprint(f"down: {self.down}")
        else:
            term.gprint(f"down: {self.down}")

        if self.left == "nothing":
            term.wprint(f"left: {self.left}")
        else:
            term.gprint(f"left: {self.left}")

        if self.right == "nothing":
            term.wprint(f"right: {self.right}")
        else:
            term.gprint(f"right: {self.right}")

        if self.item == "":
            term.wprint(f"ground: none")
        elif self.item == "none":
            term.wprint(f"ground: none")
        else:
            term.pprint(f"+ ground: {self.item.title()}")


prison_cell = Room(
    "Prison Cell", "Window", "nothing", "nothing", "Passage", items.key.name
)
passage = Room(
    "Passage", "Sleeping Quarters", "Armory", "Prison Cell", "Lab", items.robe.name
)
armory = Room(
    "Armory", "Passage", "nothing", "nothing", "nothing", items.space_sword.name
)
sleep_quar = Room("Sleeping Quarters", "Food Hall", "Passage", "nothing", "nothing", "")
food_hall = Room("Food Hall", "nothing", "Sleeping Quarters", "nothing", "nothing", "")
lab = Room("Lab", "nothing", "nothing", "Passage", "Passenger Area", "")
pass_area = Room(
    "Passenger Area", "Blaster Turret", "Cargo Hold", "Lab", "Crew Area", ""
)
cargo_hold = Room("Cargo Hold", "Passenger Area", "nothing", "nothing", "nothing", "")
blaster_turret = Room(
    "Blaster Turret", "nothing", "Passenger Area", "nothing", "nothing", ""
)
crew_area = Room("Crew Area", "nothing", "nothing", "Passenger Area", "Cockpit", "")
cockpit = Room("Cockpit", "nothing", "nothing", "Crew Area", "nothing", "")

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
        "item": items.key,
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
        "item": items.robe,
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
        "item": items.space_sword,
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
        "down": lab.down,
        "d": lab.down,
        "left": 2,
        "l": 2,
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
