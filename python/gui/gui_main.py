import tkinter as tk
from gui import TowerDefenseGUI, TitleScreen

# Function to start the main Tower Defense GUI game

def start_game():

    """
    Callback function to initialize and start the Tower Defense GUI.
    Called after the title screen fades out.
    """

    TowerDefenseGUI(root)

# Initialize the main Tkinter window.

root = tk.Tk()
root.geometry("900x600")
root.resizable(True, True)

# Fade in effect for the window on startup reference:
# https://python-forum.io/thread-43391.html

root.attributes("-alpha", 0.0)  # Start fully transparent


def fade_in(alpha=0.0):

    """
    Gradually increase window transparency from 0 to 1.
    Creates a smooth fade-in effect on startup.

    Args:
        alpha (float): Current window alpha level (0.0 to 1.0)
    """

    alpha += 0.05
    if alpha <= 1.0:
        root.attributes("-alpha", alpha)
        root.after(20, fade_in, alpha)


# Start the fade-in effect.

fade_in()

# Initialize the main title screen.

TitleScreen(root, start_game)

# Start the Tkinter main event loop.

root.mainloop()
