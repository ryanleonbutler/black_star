from characters import character as char


def test_create_char():
    c = char.Character("Bob", "Male", "Human", ["Space Sword"])
    assert ("Bob", "Male", "Human", ["Space Sword"]) == (
        c.name,
        c.gender,
        c.race,
        c.inventory,
    )
