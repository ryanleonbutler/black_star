"""
Module for world maps.
"""

from black_star.tools import terminal as term


def unknown_spaceship():
    term.wprint(
        """\

Unknown Spaceship:
                     ______________
                    |              |
                    |   Food Hall  |
                    |______________|
                            |
                     ______________                          ______________
                    |   Sleeping   |                        |    Blaster   |
                    |   Quarters   |                        |    Turret    |
                    |______________|                        |______________|
                            |                                       |
 ______________      ______________      ______________      ______________      ______________      ______________
|  Prison Cell |    |              |    |              |    |   Passenger  |    |              |    |              |
|    (Start)   | -- |    Passage   | -- |      Lab     | -- |     Area     | -- |   Crew Area  | -- |   Cockpit    |
|______________|    |______________|    |______________|    |______________|    |______________|    |______________|
                            |                                       |
                     ______________                          ______________
                    |              |                        |              |
                    |    Armory    |                        |  Cargo Hold  |
                    |______________|                        |______________|
"""
    )
