"""
app.py

This module defines the Flask web application for the Monster Evolution Clicker game.
It manages routing, session handling, and communication between the frontend and the
core game logic defined in the MonsterGame class.
"""

from flask import Flask, render_template, session, jsonify, redirect, url_for
from game import MonsterGame

# Create the Flask application instance
app = Flask(__name__)

# Secret key required for securely using sessions
# Flask's secret key and session handling was not written by me.
# Source credit is listed below:
# https://flask.palletsprojects.com/en/stable/config/
app.secret_key = "supersecretkey"


def get_game():
    """
    Retrieve the current game state from the session or initialize a new game.

    :return: An instance of MonsterGame representing the current session state.
    """
    if "game" not in session:
        # Initialize a new game state if none exists.
        session["game"] = {
            "xp": 0,
            "click_value": 1,
            "upgrade_cost": 10,
            "current_stage": 1
        }

    data = session["game"]

    # Reconstruct the MonsterGame object from session data.
    game = MonsterGame(
        data["xp"],
        data["click_value"],
        data["upgrade_cost"],
        data.get("current_stage", 1)
    )
    return game


def save_game(game):
    """
    Save the current game state back into the session.

    :param game: MonsterGame instance to persist.
    """
    session["game"] = {
        "xp": game.xp,
        "click_value": game.click_value,
        "upgrade_cost": game.upgrade_cost,
        "current_stage": game.current_stage
    }


@app.route("/")
def menu():
    """
    Render the main menu page.
    Clears any existing session data to reset the game state.
    """
    session.clear()
    session["started"] = False
    return render_template("menu.html")


@app.route("/start")
def start_game():
    """
    Start a new game session and redirect the user to the game page.
    """
    session["started"] = True
    return redirect("/game")


@app.route("/quit")
def quit_game():
    """
    Quit the current game session and return the user to the main menu.
    """
    session.clear()
    return redirect(url_for("menu"))


@app.route("/game", methods=["GET"])
def game():
    """
    Render the main game page.
    Prevents access if the game was not started from the menu.
    """
    if not session.get("started"):
        return redirect(url_for("menu"))

    game = get_game()
    stage = game.get_stage()

    return render_template(
        "index.html",
        xp=game.xp,
        click_value=game.click_value,
        upgrade_cost=game.upgrade_cost,
        stage=stage
    )


@app.route("/click", methods=["POST"])
def click_monster():
    """
    Handle a monster click action.
    Increases XP and returns updated game state as JSON.
    """
    game = get_game()
    game.click()
    save_game(game)

    return jsonify({
        "xp": game.xp,
        "click_value": game.click_value,
        "upgrade_cost": game.upgrade_cost,
        "stage": game.get_stage()
    })


@app.route("/upgrade", methods=["POST"])
def upgrade_monster():
    """
    Handle a monster upgrade action.
    Applies upgrades and returns updated game state as JSON.
    """
    game = get_game()
    game.upgrade()
    save_game(game)

    return jsonify({
        "xp": game.xp,
        "click_value": game.click_value,
        "upgrade_cost": game.upgrade_cost,
        "stage": game.get_stage()
    })

# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True)
