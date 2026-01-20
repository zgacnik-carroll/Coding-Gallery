# Tower Defense GUI Game

## Overview
This is a **Python-based Tower Defense game** with a fully-featured **Tkinter GUI**. Players place towers to defend against waves of monsters. The game includes:

- **Arrow Towers** (`🏹`) and **Cannon Towers** (`💣`)  
- Two monster types: **Goblin (`G`)** and **Ogre (`O`)**  
- **10 challenging waves** 
- **Title screen, fade-in effects, and end screens** (win / lose)  
- Restart or exit the game after completion

## Installation

1. Make sure you have **Python 3.10+** installed.
2. Clone or download this repository.
3. Navigate to the `gui` directory within the `python` directory:

```bash
cd python/gui
```

## Running the Game

1. Launch the game with:
```bash
python gui_main.py
```
2. A **title screen** will appear with a fade in effect.
3. Click **Start Game** to enter the main tower defense GUI.

All interactions are done through **buttons and clickable board cells**, no console commands needed.

## Gameplay

- You have **Gold** to purchase towers and **Lives** representing health.
- Place **Arrow Towers (50 Gold)** or **Cannon Towers (80 Gold)** on the board.
- Towers automatically attack monsters during turns.
- Monsters move forward each turn; if they reach the end, you lose lives.
- Survive all 10 waves to win the game.
- After a win or loss, restart or exit via GUI buttons.

## Controls

- **Arrow Tower / Cannon Tower Buttons**: Select tower to place.
- **Board Cells**: Click a cell to place the selected tower.
- **End Turn Button**: Moves the game forward, triggers tower attacks and monster movement.
- **Restart / Exit Buttons**: Available after winning or losing.

## Visuals

- **Board**: Grid of clickable buttons that scale with the window.
- **Towers**: Represented by 🏹 (Arrow) and 💣 (Cannon) emojis.
- **Monsters**: Represented by G (Goblin) and O (Ogre).
- **Title & End Screens**: Bold and professional fonts with color highlights.
- **Fade-in effects**: Smooth introduction and transitions.
