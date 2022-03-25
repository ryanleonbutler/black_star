class Enemy:
    """
    Enemy class that defines and creates
    enemies to combat with.
    """

    def __init__(
        self,
        name: str,
        gender: str,
        race: str,
        inventory: list,
        health: int,
        armor: int,
        damage: int,
    ):
        self.name = name.title()
        self.gender = gender.title()
        self.race = race.title()
        self.inventory = inventory
        self.health = health
        self.armor = armor
        self.damage = damage
