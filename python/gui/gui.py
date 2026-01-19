"""
Tkinter GUI for the Tower Defense game.
Provides a visual interface for placing towers and progressing waves.

Some of the code below was taken from a couple different Tkinter references. Most of which was used to
change sizing of buttons, add colors, fonts, and symbols, and those references used are listed below:

https://docs.python.org/3/library/tkinter.html
https://tkdocs.com/tutorial/widgets.html
"""

import tkinter as tk
from game.game import Game
from entities.towers import ArrowTower, CannonTower

# Constants for adding different visual effects.

CELL_WIDTH = 6
CELL_HEIGHT = 3

INFO_FONT = ("Arial", 16)
BUTTON_FONT = ("Arial", 12)
TITLE_FONT = ("Arial", 22, "bold")

PADDING = 12

CELL_BG = "#2e2e2e"
CELL_BORDER = "#000000"
TOWER_BG = "#4a7a3c"
MONSTER_BG = "#7a3c3c"
HOVER_BG = "#5a5a9a"

FONT_CELL = ("Consolas", 16, "bold")
FONT_UI = ("Arial", 12)

class TowerDefenseGUI:
    """Graphical interface for the Tower Defense game."""

    def __init__(self, root):
        self.root = root
        self.root.title("Tower Defense")
        self.root.configure(bg="#1e1e1e")
        self.game = Game()
        self.selected_tower = None

        self.info_label = tk.Label(root, font=INFO_FONT)
        self.info_label.pack(pady=PADDING)

        self.board_frame = tk.Frame(
            root,
            bg=CELL_BORDER,
            padx=2,
            pady=2
        )
        self.board_frame.pack(pady=10)

        self.controls_frame = tk.Frame(root, bg="#1e1e1e")
        self.controls_frame.pack(pady=10)

        self.create_controls()
        self.create_board()
        self.update_display()

    def create_controls(self):
        """Create tower selection and control buttons."""

        tk.Button(
            self.controls_frame,
            text="🏹 Arrow Tower (50)",
            font=BUTTON_FONT,
            width=18,
            command=lambda: self.select_tower(ArrowTower())
        ).pack(side=tk.LEFT, padx=PADDING)

        tk.Button(
            self.controls_frame,
            text="💣 Cannon Tower (80)",
            font=BUTTON_FONT,
            width=18,
            command=lambda: self.select_tower(CannonTower())
        ).pack(side=tk.LEFT, padx=PADDING)

        tk.Button(
            self.controls_frame,
            text="End Turn",
            font=BUTTON_FONT,
            width=18,
            command=self.end_turn
        ).pack(side=tk.LEFT, padx=PADDING)

        tk.Button(
            self.controls_frame,
            text="Exit",
            font=BUTTON_FONT,
            width=18,
            command=self.root.quit
        ).pack(side=tk.LEFT, padx=PADDING)

    # -------------------------------------------------

    def create_board(self):
        """Create the clickable grid board."""
        self.cells = []

        for lane in range(self.game.board.lanes):
            row = []
            for col in range(self.game.board.width):
                btn = tk.Button(
                    self.board_frame,
                    width=CELL_WIDTH,
                    height=CELL_HEIGHT,
                    font=BUTTON_FONT,
                    command=lambda l=lane, c=col: self.on_cell_click(l, c)
                )

                btn.bind("<Enter>", lambda e, l=lane, c=col: self.on_hover(l, c))
                btn.bind("<Leave>", lambda e: self.update_display())

                btn.grid(row=lane, column=col)
                row.append(btn)

            self.cells.append(row)

    def select_tower(self, tower):
        """Select a tower type for placement."""
        self.selected_tower = tower
        self.info_label.config(
            text=f"Selected: {tower.name} | Gold: {self.game.gold} | Lives: {self.game.lives}"
        )

    def on_cell_click(self, lane, col):
        """Attempt to place a tower on the selected cell."""
        if not self.selected_tower:
            return

        if self.game.place_tower_at(self.selected_tower, lane, col):
            self.selected_tower = None
            self.update_display()

    def on_hover(self, lane, col):
        """Preview tower placement on hover."""
        if self.selected_tower and (lane, col) not in self.game.board.towers:
            self.cells[lane][col].config(bg=HOVER_BG)

    def end_turn(self):
        if self.game.is_game_over():
            return

        self.game.towers_attack()
        self.game.move_monsters()
        self.game.cleanup_monsters()

        if self.game.is_game_over():
            self.show_game_over()
            return

        if self.game.wave_cleared():
            self.game.wave += 1
            self.game.spawn_wave()

        self.update_display()

    def show_game_over(self):
        """Display the GAME OVER screen and disable interaction."""
        self.info_label.config(
            text="GAME OVER",
            fg="red",
            font=TITLE_FONT
        )

        for row in self.cells:
            for btn in row:
                btn.config(state=tk.DISABLED)

        for widget in self.controls_frame.winfo_children():
            widget.config(state=tk.DISABLED)

    def update_display(self):
        """Redraw the entire board and status display."""
        self.info_label.config(
            text=f"Wave {self.game.wave} | Gold: {self.game.gold} | Lives: {self.game.lives}"
        )

        for lane in range(self.game.board.lanes):
            for col in range(self.game.board.width):
                btn = self.cells[lane][col]
                btn.config(text="", bg=CELL_BG)

                if (lane, col) in self.game.board.towers:
                    tower = self.game.board.towers[(lane, col)]
                    symbol = "🏹" if tower.name.startswith("Arrow") else "💣"
                    btn.config(text=symbol, bg=TOWER_BG)
                    continue

                for monster, m_lane in self.game.board.monsters:
                    if monster.is_alive() and m_lane == lane and monster.position == col:
                        btn.config(text=monster.symbol, bg=MONSTER_BG)
                        break
