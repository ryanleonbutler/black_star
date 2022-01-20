from characters import character as char


def test_create_human():
    c = char.Human(
        "Bob",
        "Male",
        ["Space Sword"],
    )
    assert (
        "Bob",
        "Male",
        ["Space Sword"],
        1,
        0,
        None,
        None,
        None,
        "Human",
        15,
        7,
        3,
    ) == (
        c.name,
        c.gender,
        c.inventory,
        c.level,
        c.exp,
        c.head,
        c.chest,
        c.weapon,
        c.race,
        c.health,
        c.armor,
        c.damage,
    )


def test_create_alien():
    c = char.Alien(
        "Bob",
        "Male",
        ["Space Sword"],
    )
    assert (
        "Bob",
        "Male",
        ["Space Sword"],
        1,
        0,
        None,
        None,
        None,
        "Alien",
        9,
        3,
        13,
    ) == (
        c.name,
        c.gender,
        c.inventory,
        c.level,
        c.exp,
        c.head,
        c.chest,
        c.weapon,
        c.race,
        c.health,
        c.armor,
        c.damage,
    )


def test_create_robot():
    c = char.Robot(
        "Bob",
        "Male",
        ["Space Sword"],
    )
    assert (
        "Bob",
        "Male",
        ["Space Sword"],
        1,
        0,
        None,
        None,
        None,
        "Robot",
        12,
        5,
        8,
    ) == (
        c.name,
        c.gender,
        c.inventory,
        c.level,
        c.exp,
        c.head,
        c.chest,
        c.weapon,
        c.race,
        c.health,
        c.armor,
        c.damage,
    )
