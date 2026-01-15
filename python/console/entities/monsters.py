"""
This file contains all Monster classes for the text-based tower defense game.
"""

class Monster:

    """
    Base class for all monsters in the game.

    Attributes:
        name: The monster's name.
        symbol: Character symbol for display.
        hp: Hit points.
        speed: Cells moved per turn.
        position: Current column position on the lane.
    """

    def __init__(self, name, symbol, hp, speed):
        self.name = name
        self.symbol = symbol
        self.hp = hp
        self.speed = speed
        self.position = 0

    def move(self):
        # Move the monster forward based on speed.
        self.position += self.speed

    def take_damage(self, damage):
        # Reduce monster health by tower damage.
        self.hp -= damage

    def is_alive(self):
        # Check to see if monster is still alive.
        return self.hp > 0

class Goblin(Monster):
    # A fast, weak monster that inherits the Monster constructor.
    def __init__(self):
        super().__init__("Goblin", "G", hp = 20, speed = 2)

class Ogre(Monster):
    # A strong, slow monster that inherits the Monster constructor.
    def __init__(self):
        super().__init__("Ogre", "O", hp = 40, speed = 1)
