"""
This file handles the main game loop, waves, turns, tower placement, monster movement, and win / lose conditions.
Additionally, there is a QuitGame exception class used for
"""

import random
from game.board import Board
from entities.monsters import Goblin, Ogre
from entities.towers import ArrowTower, CannonTower

class QuitGame(Exception):
    # Raised when the player chooses to exit the game.
    pass

class Game:
    """
    Base class for game.

    Attributes:
        board: Game board of type Board.
        gold: Starting gold amount.
        lives: Total user lives.
        turn: Starting turn of the game.
        wave: Starting wave of the game.
        max_waves: Total waves in the game.
    """

    def __init__(self):
        self.board = Board()
        self.gold = 150
        self.lives = 10
        self.turn = 1
        self.wave = 1
        self.max_waves = 5

    def spawn_wave(self):
        # Create a new wave of monsters in all lanes.
        print(f"\n  WAVE {self.wave} INCOMING ")
        for lane in range(self.board.lanes):
            monster = random.choice([Goblin, Ogre])()
            self.board.add_monster(monster, lane)

    def place_tower(self):
        # Prompt player to place a tower or be finished with their turn.
        while True:
            print(f"\nGold: {self.gold}")
            print("[1] Arrow Tower (50 gold)")
            print("[2] Cannon Tower (80 gold)")
            print("[0] Done placing towers")
            print("[exit] Forfeit the game")

            choice = input("Choose tower: ")

            if choice == "exit":
                raise QuitGame()

            if choice == "0":
                return

            tower_map = {"1": ArrowTower, "2": CannonTower}
            if choice not in tower_map:
                print("Invalid choice. Try again.")
                continue

            tower = tower_map[choice]()
            if self.gold < tower.cost:
                print("Not enough gold.")
                continue

            try:
                lane = int(input("Lane (1-3): ")) - 1
                col = int(input("Column (1-6): ")) - 1
            except ValueError:
                print("Invalid number input.")
                continue

            if not (0 <= lane < self.board.lanes and 0 <= col < self.board.width):
                print("Out of bounds.")
                continue

            if (lane, col) in self.board.towers:
                print("Tower already there.")
                continue

            # Valid placement
            self.board.add_tower(lane, col, tower)
            self.gold -= tower.cost
            print(f"{tower.name} placed.")

    def towers_attack(self):
        # Have each tower attack the first monster in range.
        print("\nTOWERS ATTACK")
        for (lane, col), tower in self.board.towers.items():
            for monster, m_lane in self.board.monsters:
                if (
                    m_lane == lane
                    and monster.is_alive()
                    and tower.in_range(col, monster.position)
                ):
                    monster.take_damage(tower.damage)
                    print(
                        f"{tower.name} hits {monster.name} "
                        f"for {tower.damage} damage"
                    )
                    break

    def move_monsters(self):
        # Move all monsters forward according to their speed.
        for monster, _ in self.board.monsters:
            if monster.is_alive():
                monster.move()

    def cleanup_monsters(self):
        # Remove dead or escaped monsters and adjust gold/lives.
        remaining = []
        for monster, lane in self.board.monsters:
            if monster.position >= self.board.width:
                self.lives -= 1
                print(f" {monster.name} escaped! Lives -1")
            elif monster.is_alive():
                remaining.append((monster, lane))
            else:
                self.gold += 10
                print(f" {monster.name} defeated! +10 gold")
        self.board.monsters = remaining

    def run(self):
        # Main game loop that continues until the player wins or loses.
        print("\n TEXT-BASED TOWER DEFENSE ")

        try:
            while self.lives > 0 and self.wave <= self.max_waves:
                self.spawn_wave()

                while self.board.monsters and self.lives > 0:
                    print(f"\nTURN {self.turn} | Lives: {self.lives}")
                    self.board.display()
                    self.place_tower()
                    self.towers_attack()
                    self.move_monsters()
                    self.cleanup_monsters()
                    self.turn += 1

                self.wave += 1

        except QuitGame:
            print("Forfeiting the game. Thanks for playing!")
            return

        if self.lives > 0:
            print("\n YOU WIN! All waves defeated.")
        else:
            print("\n GAME OVER. The monsters broke through.")
