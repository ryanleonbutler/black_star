# class Room:
# TODO: Create Room class
class Room:
    NAME = ""
    UP = ""
    DOWN = ""
    LEFT = ""
    RIGHT = ""
    OBJECT = [""]


def create_room_func(name, up, down, left, right, room_object):
    Room.NAME = name
    Room.UP = up
    Room.DOWN = down
    Room.LEFT = left
    Room.RIGHT = right
    Room.OBJECT[-1] = room_object
