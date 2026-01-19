"""
This file contains all Tower classes for the text-based tower defense game.
"""

class Tower:

    """
    Base class for all towers in the game.

    Attributes:
        name: Tower name.
        symbol: Symbol for display.
        cost: Gold cost to build.
        damage: Damage dealt to a monster.
        shot_range: Attack range in cells.
    """

    def __init__(self, name, symbol, cost, damage, shot_range):
        self.name = name
        self.symbol = symbol
        self.cost = cost
        self.damage = damage
        self.range = shot_range

    def in_range(self, tower_col, monster_col):
        # Check if a monster is within range of the tower.
        return abs(tower_col - monster_col) <= self.range

class ArrowTower(Tower):
    # A basic, inexpensive tower with moderate range and damage.
    def __init__(self):
        super().__init__("Arrow Tower", "T", cost = 50, damage = 10, shot_range = 2)

class CannonTower(Tower):
    # A strong, expensive tower with higher damage and same range as ArrowTower.
    def __init__(self):
        super().__init__("Cannon Tower", "C", cost = 80, damage = 20, shot_range = 2)
