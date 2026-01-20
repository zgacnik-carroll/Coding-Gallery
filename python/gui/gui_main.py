import tkinter as tk
from gui import TowerDefenseGUI, TitleScreen

def start_game():
    TowerDefenseGUI(root)

root = tk.Tk()
root.geometry("900x600")
root.resizable(False, False)

# Fade in effect code referenced from this source:
# https://python-forum.io/thread-43391.html

root.attributes("-alpha", 0.0)

def fade_in(alpha=0.0):
    alpha += 0.05
    if alpha <= 1.0:
        root.attributes("-alpha", alpha)
        root.after(20, fade_in, alpha)

fade_in()

# Title screen

TitleScreen(root, start_game)
root.mainloop()
