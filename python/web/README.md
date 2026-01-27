# Monster Evolution Clicker Game

Monster Evolution Clicker is a simple web-based clicker game built using **Python**, **Flask**, and **JavaScript**.  

Players click a button to earn XP, purchase upgrades to increase click power, and evolve the monster through multiple stages.

---

## Requirements

Before running this project, make sure you have the following installed:

### Required Software
- **Python 3.10+**
- **Flask**

### Check Your Python Version
```bash
python --version
```

### Install Flask

```bash
pip install flask
```

---

## Downloading the Code

After ensuring installation of the proper requirements, you must then clone the Git repository to run the application.

### Clone the Git Repository

```bash
git clone <repo url>
cd python/web
```

Now, after clong the repository, you must use the terminal to run the web application.

### Run the Web Application Game

```bash
python app.py
```

Once you have run this command, you should see something like this within the terminal:

```bash
* Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 112-463-303
```

Click the link to ```http://127.0.0.1:5000``` and the web application game will start within a new browser window.

---

## Gameplay

Monster Evolution Clicker is a simple clicker-style game focused on progression through upgrades and evolution.

### Basic Controls
- **Click the Click Monster button** to gain XP.
- **Click the Upgrade button** to spend XP and improve your click power.

### XP & Upgrades
- Each monster click grants XP.
- Purchasing an upgrade:
  - Doubles the amount of XP earned per click
  - Increases the cost of the next upgrade
- Upgrades require sufficient XP and cannot be purchased otherwise.

### Monster Evolution
- The monster evolves through multiple stages.
- Evolution does **not** happen automatically when XP is gained.
- A new stage is unlocked **only when the Upgrade button is clicked** after reaching the required XP threshold.
- Once a stage is reached, the monster **never devolves**.

### Evolution Stages
- **Stage 1:** 0–9 XP  
- **Stage 2:** 10–49 XP  
- **Stage 3:** 50–249 XP  
- **Stage 4:** 250+ XP  

Each stage is represented by a different monster image that updates dynamically during gameplay.

### Closing Remarks

Monster Evolution Clicker is designed to be easy to understand while still demonstrating key game and web development concepts. The upgrade-driven evolution system encourages strategic progression and provides clear visual feedback as the monster grows stronger. This makes the game both engaging to play and effective as a learning project.
