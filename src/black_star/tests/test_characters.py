from characters import character as char


def test_create_char():
    c = char.Character("MyPlayer", "Male", "Human")
    assert ("Myplayer", "Male", "Human") == (c.name, c.gender, c.race)
