/**
 * main.js
 *
 * Handles client-side interaction for the Monster Evolution Clicker game.
 * Responsible for sending user actions to the server and updating the UI
 * based on the game state returned by the Flask backend.
 */

// Cache references to key DOM elements for efficient access
const clickBtn = document.getElementById('clickBtn');
const upgradeBtn = document.getElementById('upgradeBtn');
const xpSpan = document.getElementById('xp');
const clickValueSpan = document.getElementById('click_value');
const upgradeCostSpan = document.getElementById('upgrade_cost');
const monsterImg = document.getElementById('monster');

// Event listener for clicking the monster
// Sends a POST request to the server to increment XP
clickBtn.addEventListener('click', () => {
    fetch('/click', { method: 'POST' })
        .then(response => response.json())
        .then(data => updateUI(data));
});

// Event listener for upgrading the monster
// Sends a POST request to apply an upgrade if eligible
upgradeBtn.addEventListener('click', () => {
    fetch('/upgrade', { method: 'POST' })
        .then(response => response.json())
        .then(data => updateUI(data));
});

/**
 * Update the user interface with the latest game state.
 *
 * @param {Object} data - Game state returned from the server
 * @param {number} data.xp - Current XP value
 * @param {number} data.click_value - XP gained per click
 * @param {number} data.upgrade_cost - XP required for the next upgrade
 * @param {number} data.stage - Current monster evolution stage
 */
function updateUI(data) {
    // Update displayed XP, click value, and upgrade cost
    xpSpan.textContent = data.xp;
    clickValueSpan.textContent = data.click_value;
    upgradeCostSpan.textContent = data.upgrade_cost;

    // Enable or disable the upgrade button based on available XP
    upgradeBtn.disabled = data.xp < data.upgrade_cost;

    // Update monster image to reflect the current evolution stage
    // Timestamp is appended to prevent browser image caching
    monsterImg.src = `/static/stage${data.stage}.png?t=${new Date().getTime()}`;
}
