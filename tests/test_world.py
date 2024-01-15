from black_star.world import world


def test_create_room():
    room = world.Room("Room", "Up", "Down", "Left", "Right", "Item", "Enemy")
    assert ("Room", "Up", "Down", "Left", "Right", "Item", "Enemy") == (
        room.name,
        room.up,
        room.down,
        room.left,
        room.right,
        room.item,
        room.enemy,
    )
