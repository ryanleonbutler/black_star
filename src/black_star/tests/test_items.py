from world import items


def test_create_item():
    gun = items.Item("Gun", "Weapon", 0, "10", "Gun that shoots")
    assert ("Gun", "Weapon", 0, "10", "Gun that shoots") == (
        gun.name,
        gun.item_type,
        gun.armor,
        gun.damage,
        gun.description,
    )
