import black_star.characters.character as character


def test_create_human():
    c = character.Human(
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
        "",
        "",
        "",
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
        c.body,
        c.weapon,
        c.race,
        c.health,
        c.armor,
        c.damage,
    )


def test_create_alien():
    c = character.Alien(
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
        "",
        "",
        "",
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
        c.body,
        c.weapon,
        c.race,
        c.health,
        c.armor,
        c.damage,
    )


def test_create_robot():
    c = character.Robot(
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
        "",
        "",
        "",
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
        c.body,
        c.weapon,
        c.race,
        c.health,
        c.armor,
        c.damage,
    )
