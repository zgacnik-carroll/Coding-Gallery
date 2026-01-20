"""
Tkinter GUI for the Tower Defense game.
"""

import tkinter as tk
from game.game import Game
from entities.towers import ArrowTower, CannonTower

# Game symbols (emojis copied from Google).

ARROW_TOWER_SYMBOL = "🏹"
CANNON_TOWER_SYMBOL = "💣"

GOBLIN_SYMBOL = "G"
OGRE_SYMBOL = "O"

# Visual configuration constants.

# Background colors.

BG_MAIN = "#1e1e1e"
BG_BOARD = "#000000"
BG_CELL = "#2e2e2e"
BG_TOWER = "#4a7a3c"
BG_MONSTER = "#7a3c3c"
BG_HOVER = "#3c5a7a"

# Foreground colors.

FG_TEXT = "#ffffff"
FG_MUTED = "#bbbbbb"

# Fonts.

FONT_TITLE = ("Tahoma", 26, "bold")
FONT_STATUS = ("Arial", 14)
FONT_BUTTON = ("Arial", 12)
FONT_CELL = ("Consolas", 16, "bold")

# Grid cell dimensions.

CELL_WIDTH = 6
CELL_HEIGHT = 3

# Padding for spacing.

PADDING = 12

# Title Screen / Main Menu.

class TitleScreen:

    """Main menu / intro screen."""

    def __init__(self, root, start_callback):
        self.root = root
        self.start_callback = start_callback

        # Main frame for the title screen
        self.frame = tk.Frame(root, bg=BG_MAIN)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Title label
        tk.Label(
            self.frame,
            text="Tower Defense",
            font=FONT_TITLE,
            fg=FG_TEXT,
            bg=BG_MAIN
        ).pack(pady=(60, 20))

        # Game description and instructions.

        description = (
            "Defend your lanes by placing towers.\n"
            "Towers can only attack monsters within two blocks in their lane.\n"
            "Stop enemies before they reach the end.\n\n"
            "🏹 Arrow Towers: Cost 50 gold, 10hp damage per attack\n"
            "💣 Cannon Towers: Cost 80 gold, 20hp per attack\n"
            "Goblin (G): 20hp, moves fast\n"
            "Ogre (O): 40hp, moves slow\n\n"
            "Survive all waves to win!"
        )

        tk.Label(
            self.frame,
            text=description,
            font=FONT_STATUS,
            fg=FG_MUTED,
            bg=BG_MAIN,
            justify=tk.CENTER
        ).pack(pady=20)

        # Start and Exit buttons.

        tk.Button(
            self.frame,
            text="Start Game",
            font=FONT_BUTTON,
            width=22,
            height=2,
            command=self.start_game
        ).pack(pady=(30, 10))

        tk.Button(
            self.frame,
            text="Exit",
            font=FONT_BUTTON,
            width=22,
            height=2,
            command=root.quit
        ).pack(pady=10)

    def start_game(self):
        """Fade out the title screen and start the main game."""
        self.fade_out(self.frame, callback=self.start_callback)

    # Fade effect referenced from:
    # https://python-forum.io/thread-43391.html

    def fade_out(self, widget, callback=None, step=0.05, delay=20):
        """
        Gradually fade out a widget by lowering window alpha.
        Once fade out is complete, destroy widget and call callback.
        """
        root = self.root
        alpha = root.attributes("-alpha")

        def _fade():
            nonlocal alpha
            alpha -= step
            if alpha > 0:
                root.attributes("-alpha", alpha)
                root.after(delay, _fade)
            else:
                if callback:
                    widget.destroy()
                    root.attributes("-alpha", 1.0)
                    callback()

        _fade()

# Main Game GUI.

class TowerDefenseGUI:

    """Graphical interface for the Tower Defense game."""

    def __init__(self, root):
        self.root = root
        self.root.title("Tower Defense")
        self.root.configure(bg=BG_MAIN)
        self.game_finished = False  # Flag to indicate end of game

        # Initialize game logic.

        self.game = Game()
        self.selected_tower = None

        # Title.

        self.title_label = tk.Label(
            root,
            text="Tower Defense",
            font=FONT_TITLE,
            fg=FG_TEXT,
            bg=BG_MAIN
        )
        self.title_label.pack(pady=(10, 5))

        # Status bar.

        self.status_frame = tk.Frame(root, bg=BG_MAIN)
        self.status_frame.pack(pady=5)

        self.wave_label = tk.Label(self.status_frame, font=FONT_STATUS, fg=FG_TEXT, bg=BG_MAIN)
        self.gold_label = tk.Label(self.status_frame, font=FONT_STATUS, fg=FG_TEXT, bg=BG_MAIN)
        self.lives_label = tk.Label(self.status_frame, font=FONT_STATUS, fg=FG_TEXT, bg=BG_MAIN)

        # Pack the status labels.

        self.wave_label.pack(side=tk.LEFT, padx=15)
        self.gold_label.pack(side=tk.LEFT, padx=15)
        self.lives_label.pack(side=tk.LEFT, padx=15)

        # Board.

        self.board_frame = tk.Frame(
            root,
            bg=BG_BOARD,
            padx=3,
            pady=3,
            relief=tk.SUNKEN,
            borderwidth=2
        )
        self.board_frame.pack(pady=10)

        # Controls.

        self.controls_frame = tk.Frame(root, bg=BG_MAIN)
        self.controls_frame.pack(pady=10)

        # Create control buttons and board cells.

        self.create_controls()
        self.create_board()
        self.update_display()

        # Legend for symbols.

        self.legend_label = tk.Label(
            self.root,
            text="Legend: 🏹 Arrow Tower | 💣 Cannon Tower | G Goblin | O Ogre",
            font=("Arial", 11),
            fg=FG_MUTED,
            bg=BG_MAIN
        )
        self.legend_label.pack(pady=(5, 10))

    def create_controls(self):
        """Create tower selection and control buttons."""
        self.arrow_btn = tk.Button(
            self.controls_frame,
            text="Arrow Tower (50)",
            font=FONT_BUTTON,
            width=18,
            cursor="hand2",
            command=lambda: self.select_tower(ArrowTower())
        )
        self.arrow_btn.pack(side=tk.LEFT, padx=PADDING)

        self.cannon_btn = tk.Button(
            self.controls_frame,
            text="Cannon Tower (80)",
            font=FONT_BUTTON,
            width=18,
            cursor="hand2",
            command=lambda: self.select_tower(CannonTower())
        )
        self.cannon_btn.pack(side=tk.LEFT, padx=PADDING)

        self.end_turn_btn = tk.Button(
            self.controls_frame,
            text="End Turn",
            font=FONT_BUTTON,
            width=18,
            cursor="hand2",
            command=self.end_turn
        )
        self.end_turn_btn.pack(side=tk.LEFT, padx=PADDING)

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
                    font=FONT_CELL,
                    bg=BG_CELL,
                    fg=FG_TEXT,
                    relief=tk.FLAT,
                    cursor="hand2",
                    command=lambda l=lane, c=col: self.on_cell_click(l, c)
                )

                # Preview hover effect

                btn.bind("<Enter>", lambda e, l=lane, c=col: self.on_hover(l, c))
                btn.bind("<Leave>", lambda e: self.update_display())
                btn.grid(row=lane, column=col)
                row.append(btn)
            self.cells.append(row)

    def select_tower(self, tower):
        """Select a tower type for placement."""
        self.selected_tower = tower
        self.title_label.config(
            text=f"Placing: {tower.name}",
            fg=FG_MUTED
        )

    def on_cell_click(self, lane, col):
        """Attempt to place a tower on the selected cell."""
        if not self.selected_tower:
            return

        if self.game.place_tower_at(self.selected_tower, lane, col):
            self.selected_tower = None
            self.title_label.config(text="Tower Defense", fg=FG_TEXT)
            self.update_display()

    def on_hover(self, lane, col):
        """Preview placement with hover effect."""
        if self.game_finished:
            return

        if self.selected_tower and (lane, col) not in self.game.board.towers:
            self.cells[lane][col].config(bg=BG_HOVER)

    def end_turn(self):
        """Perform all actions for end-of-turn."""
        if self.game.is_game_over():
            return

        self.game.towers_attack()
        self.game.move_monsters()
        self.game.cleanup_monsters()

        # Check for game over.

        if self.game.is_game_over():
            self.show_end_screen("GAME OVER", "red")
            return

        # Spawn new wave or show victory.

        if self.game.wave_cleared():
            if self.game.wave == self.game.max_waves:
                self.show_end_screen("YOU SURVIVED ALL WAVES!", "lightgreen")
                return
            self.game.wave += 1
            self.game.spawn_wave()

        self.update_display()

    def show_end_screen(self, text, color):
        """Display end-of-game screen and disable board interaction."""
        self.game_finished = True

        # Disable all board cells.

        for row in self.cells:
            for btn in row:
                btn.unbind("<Enter>")
                btn.unbind("<Leave>")
                btn.config(state=tk.DISABLED)

        # Update title text.

        self.title_label.config(text=text, fg=color)

        # Clear control buttons and add Restart / Exit buttons.

        for widget in self.controls_frame.winfo_children():
            widget.destroy()

        tk.Button(
            self.controls_frame,
            text="Restart Game",
            font=FONT_BUTTON,
            width=18,
            command=self.restart_game
        ).pack(side=tk.LEFT, padx=PADDING)

        tk.Button(
            self.controls_frame,
            text="Exit",
            font=FONT_BUTTON,
            width=18,
            command=self.root.quit
        ).pack(side=tk.LEFT, padx=PADDING)

    def restart_game(self):
        """Restart the application cleanly by reinitializing the GUI."""
        for widget in self.root.winfo_children():
            widget.destroy()
        self.__init__(self.root)

    def update_display(self):
        """Redraw the board and update all status labels and buttons."""
        if self.game_finished:
            return

        # Update status labels.

        self.wave_label.config(text=f"Wave: {self.game.wave}")
        self.gold_label.config(text=f"Gold: {self.game.gold}")
        self.lives_label.config(text=f"Lives: {self.game.lives}")

        # Enable/disable tower buttons based on available gold.

        self.arrow_btn.config(state=tk.NORMAL if self.game.gold >= 50 else tk.DISABLED)
        self.cannon_btn.config(state=tk.NORMAL if self.game.gold >= 80 else tk.DISABLED)

        # Update board cells.

        for lane in range(self.game.board.lanes):
            for col in range(self.game.board.width):
                btn = self.cells[lane][col]
                btn.config(text="", bg=BG_CELL)

                # Display towers.

                if (lane, col) in self.game.board.towers:
                    tower = self.game.board.towers[(lane, col)]
                    symbol = ARROW_TOWER_SYMBOL if tower.name.startswith("Arrow") else CANNON_TOWER_SYMBOL
                    btn.config(text=symbol, bg=BG_TOWER)
                    continue

                # Display monsters.

                for monster, m_lane in self.game.board.monsters:
                    if monster.is_alive() and m_lane == lane and monster.position == col:
                        symbol = GOBLIN_SYMBOL if monster.name == "Goblin" else OGRE_SYMBOL
                        btn.config(text=symbol, bg=BG_MONSTER)
                        break
