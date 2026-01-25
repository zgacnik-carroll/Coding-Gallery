"""
game.py

This module contains the core game logic for the Monster Evolution Clicker web game.
It defines the MonsterGame class, which manages experience points (XP), upgrades,
click values, and monster evolution stages. The logic in this file is independent
of the web framework and is intended to be used by the Flask application.
"""

class MonsterGame:
    """
    Represents the core game logic for the Monster Evolution Clicker game.
    Handles XP accumulation, upgrades, and monster evolution stages.
    """

    def __init__(self, xp=0, click_value=1, upgrade_cost=10, current_stage=1):
        """
        Initialize a new game state or restore an existing one.

        :param xp: Current experience points accumulated by the player.
        :param click_value: Amount of XP gained per click.
        :param upgrade_cost: XP required to purchase the next upgrade.
        :param current_stage: Current evolution stage of the monster.
        """
        self.xp = xp
        self.click_value = click_value
        self.upgrade_cost = upgrade_cost
        self.current_stage = current_stage

    def click(self):
        """
        Handle a monster click.
        Increases XP based on the current click value.
        """
        self.xp += self.click_value

    def can_upgrade(self):
        """
        Determine whether the player has enough XP to perform an upgrade.

        :return: True if the player can upgrade, False otherwise.
        """
        return self.xp >= self.upgrade_cost

    def calculate_stage(self):
        """
        Determine the monster's eligible evolution stage based on XP thresholds.

        Stages:
        - Stage 1: XP < 10
        - Stage 2: XP >= 10
        - Stage 3: XP >= 50
        - Stage 4: XP >= 250

        :return: The highest stage the player qualifies for based on XP.
        """
        if self.xp >= 250:
            return 4
        elif self.xp >= 50:
            return 3
        elif self.xp >= 10:
            return 2
        else:
            return 1

    def upgrade(self):
        """
        Perform a monster upgrade if the player has enough XP.

        - Deducts XP equal to the upgrade cost.
        - Doubles XP gained per click.
        - Increases the cost of the next upgrade.
        - Advances the monster's evolution stage if eligible.
        """
        if self.can_upgrade():
            # Determine the highest evolution stage eligible before XP is deducted
            eligible_stage = self.calculate_stage()

            # Apply upgrade effects
            self.xp -= self.upgrade_cost
            self.click_value *= 2
            self.upgrade_cost *= 5

            # Update monster stage only if a new stage has been reached
            if eligible_stage > self.current_stage:
                self.current_stage = eligible_stage

    def get_stage(self):
        """
        Retrieve the monster's current evolution stage.

        :return: Current evolution stage
        """
        return self.current_stage
