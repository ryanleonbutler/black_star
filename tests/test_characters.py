from black_star.characters.character import Alien, Human, Robot
import pytest


@pytest.mark.parametrize(
    "CharClass, race, health, armor, damage",
    [
        (Alien, "Alien", 9, 3, 13),
        (Human, "Human", 15, 7, 3),
        (Robot, "Robot", 12, 5, 8),
    ],
)
def test_create_alien(CharClass, race, health, armor, damage):
    c = CharClass("John", "Male", [])
    assert c.name == "John"
    assert c.gender == "Male"
    assert c.inventory == []
    assert c.level == 1
    assert c.exp == 0
    assert c.head == ""
    assert c.body == ""
    assert c.weapon == ""
    assert c.race == race
    assert c.health == health
    assert c.armor == armor
    assert c.damage == damage


def test_add_to_inventory(fake_sword):
    c = Human("John", "Male", [])
    c.take_item(fake_sword)
    assert len(c.inventory) == 1
    assert c.inventory[0].name == fake_sword.name


def test_equip_item(fake_sword):
    c = Human("John", "Male", [])
    c.take_item(fake_sword)
    c.equip_item(fake_sword.name)
    assert c.weapon == fake_sword.name
    assert len(c.inventory) == 0
