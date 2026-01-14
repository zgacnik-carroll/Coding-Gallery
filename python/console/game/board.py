"""
This file handles the board state and display for the text-based tower defense game.
"""

class Board:

    """
    Base class for game board.

    Attributes:
        lanes: The lanes on the game board.
        width: Lane width on the game board.
        towers: Maps (lane, col) to Tower.
        monsters: List of tuples (Monster, lane).
    """

    def __init__(self, lanes=3, width=6):
        self.lanes = lanes
        self.width = width
        self.towers = {}
        self.monsters = []

    def add_tower(self, lane, col, tower):
        # Place a tower on the board.
        self.towers[(lane, col)] = tower

    def add_monster(self, monster, lane):
        # Add a monster to a specific lane.
        self.monsters.append((monster, lane))

    def display(self):
        # Print the board state in ASCII format.
        print("\n" + "=" * 40)
        for lane in range(self.lanes):
            row = []
            for col in range(self.width):
                # Tower takes priority in display
                if (lane, col) in self.towers:
                    row.append(self.towers[(lane, col)].symbol)
                else:
                    symbol = ">"
                    for monster, m_lane in self.monsters:
                        if (
                            m_lane == lane
                            and monster.position == col
                            and monster.is_alive()
                        ):
                            symbol = monster.symbol
                            break
                    row.append(symbol)
            print(f"Lane {lane + 1} | " + " ".join(row) + " |")
        print("=" * 40)
