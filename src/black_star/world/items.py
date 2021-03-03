"""
Module for game objects.
"""


from tools import terminal as term


# class for Items to use and equip in-game:
class Items:
    """
    [Item class that defines usable objects in the game like armor and weapons. Also other items like health elixirs and notes.]
    """

    def __init__(self, name="", item_type="", armor=0, damage=0, description=""):
        self.name = name
        self.item_type = item_type
        self.armor = armor
        self.damage = damage
        self.description = description

    def view_item(self):
        """
        [Prints item details and attributes to the screen]
        """
        if not self.name:
            term.wprint("No items on ground to inspect")
        elif self.name == "none":
            term.wprint("No items on ground to inspect")
        else:
            term.bprint(f"---Item details: ({self.name.title()})---")
            term.pprint(
                f"Type: {self.item_type}\n"
                f"Armor: {self.armor}\n"
                f"Damage: {self.damage}\n"
                f"Description: {self.description}"
            )


# Create game items
key = Items("key", "other", 0, 0, "Opens lock on door")
robe = Items("robe", "armor", 5, 0, "Plain brown cotton robe")
space_sword = Items(
    "space sword", "weapon", 0, 5, "Laser energy sword that cuts through anything"
)

item_map = {
    key: {
        "Name": key.name,
        "Type": key.item_type,
        "Armor": key.armor,
        "Damage": key.damage,
        "Description": key.description,
    },
    robe: {
        "Name": robe.name,
        "Type": robe.item_type,
        "Armor": robe.armor,
        "Damage": robe.damage,
        "Description": robe.description,
    },
    space_sword: {
        "Name": space_sword.name,
        "Type": space_sword.item_type,
        "Armor": space_sword.armor,
        "Damage": space_sword.damage,
        "Description": space_sword.description,
    },
}
