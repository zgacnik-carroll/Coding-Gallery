from flask import Flask, render_template, session, jsonify
from game import MonsterGame

app = Flask(__name__)
app.secret_key = "supersecretkey"

def get_game():
    if "game" not in session:
        session["game"] = {"xp": 0, "click_value": 1, "upgrade_cost": 10, "current_stage": 1}
    data = session["game"]
    game = MonsterGame(
        data["xp"],
        data["click_value"],
        data["upgrade_cost"],
        data.get("current_stage", 1)
    )
    return game

def save_game(game):
    session["game"] = {
        "xp": game.xp,
        "click_value": game.click_value,
        "upgrade_cost": game.upgrade_cost,
        "current_stage": game.current_stage
    }

@app.route("/")
def index():
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
    game = get_game()
    game.upgrade()
    save_game(game)
    return jsonify({
        "xp": game.xp,
        "click_value": game.click_value,
        "upgrade_cost": game.upgrade_cost,
        "stage": game.get_stage()
    })

if __name__ == "__main__":
    app.run(debug=True)
