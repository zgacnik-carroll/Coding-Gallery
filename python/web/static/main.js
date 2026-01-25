
const clickBtn = document.getElementById('clickBtn');
const upgradeBtn = document.getElementById('upgradeBtn');
const xpSpan = document.getElementById('xp');
const clickValueSpan = document.getElementById('click_value');
const upgradeCostSpan = document.getElementById('upgrade_cost');
const monsterImg = document.getElementById('monster');


clickBtn.addEventListener('click', () => {
    fetch('/click', { method: 'POST' })
    .then(response => response.json())
    .then(data => updateUI(data));
});


upgradeBtn.addEventListener('click', () => {
    fetch('/upgrade', { method: 'POST' })
    .then(response => response.json())
    .then(data => updateUI(data));
});


function updateUI(data) {
    // Update XP, click value, and upgrade cost
    xpSpan.textContent = data.xp;
    clickValueSpan.textContent = data.click_value;
    upgradeCostSpan.textContent = data.upgrade_cost;


    upgradeBtn.disabled = data.xp < data.upgrade_cost;

    monsterImg.src = `/static/stage${data.stage}.png?t=${new Date().getTime()}`;
}

