---
title: Ethan Tran and Alex Kumar JavaScript Exit Mini-Game
badges: true
comments: true
author: Ethan Tran
categories: [javascript, clicker game]
layout: base
---

## Ethan Tran & Alex Kumar: Monkey Clicker
>A JavaScript Cookie Clicker-type Game

<html>
<style>
#clicker-button1 {
    width: 100px;
    height: 100px;
    border: none;
    outline: none;
    background: url('https://github.com/realethantran/fastpages_EthanT/assets/109186517/8bbff442-768e-4040-ab9e-232f1880f860') no-repeat;
    background-size: cover;
    cursor: pointer;
    transition: transform 0.3s;
}
#clicker-button1:hover {
    transform: scale(1.1); /* Increase the size on hover */
}
button {
    margin: 5px; /* Add some margin around the buttons */
    padding: 10px 20px; /* Add padding to the buttons */
    border: #fff;
    outline: #fff;
    background-color: #f1f1f1; /* Set a background color */
    color: #333; /* Set the text color */
    cursor: pointer;
    transition: background-color 0.3s;
}
#container {
    display: flex; /* Use flexbox for layout */
    flex-direction: column; /* Arrange elements in a column */
    align-items: center; /* Center align the elements horizontally */
    justify-content: center; /* Center align the elements vertically */
}
button:nth-child(1) {
    background-color: #b3ffb3; /* Set a different background color for the fourth button */
}
button:nth-child(2) {
    background-color: #ff8080; /* Set a different background color for the second button */
}
button:nth-child(3) {
    background-color: #80b3ff; /* Set a different background color for the third button */
}
#score1,
#highscore1,
#timer {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
    color: white;
}
#save-form {
    margin-top: 20px;
}
#save-form input[type="text"] {
    padding: 5px;
    margin-right: 10px;
}
#score-table {
    margin-top: 20px;
    border-collapse: collapse;
}
#score-table th,
#score-table td {
    padding: 5px 10px;
    border: 1px solid black;
}
</style>
<div id="container">
    <div id="score1">Score: 0</div>
    <div id="highscore1">High Score: 0</div>
    <div id="timer">Time: 10</div>
    <div>
        <button onclick="upgradeOne()">1.5x Multiplier</button>
        <button onclick="upgradeTwo()">2.0x Multiplier</button>
        <button onclick="upgradeThree()">2.5x Multiplier</button>
    </div>
    <button id="clicker-button1" onclick="incrementScore()"></button>
    <form id="save-form">
        <input type="text" id="name-input" placeholder="Enter your name" />
        <button type="button" onclick="saveScore()">Save Score</button>
    </form>
    <table id="score-table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Score</th>
            </tr>
        </thead>
        <tbody id="score-table-body"></tbody>
    </table>
</div>

<script>
var score = 0;
var highScore = localStorage.getItem('highScore') || 0; // Retrieve the high score from local storage
var growth = 1.0; // The button's initial size (as a scaling factor)
var upgradeMultiplier = 1.0; // Setting up the multiplier
var timer;
var scores = JSON.parse(localStorage.getItem('scores')) || []; // Retrieve the scores from local storage

// Update the high score display
document.getElementById('highscore1').innerText = "High Score: " + highScore;

function incrementScore() {
    score += incrementNumber();
    document.getElementById('score1').innerText = "Score: " + score;

    // Check if the current score is higher than the high score
    if (score > highScore) {
        highScore = score;
        document.getElementById('highscore1').innerText = "High Score: " + highScore;
        localStorage.setItem('highScore', highScore); // Save the new high score to local storage
    }

    // Increase the button's size by 1% for each click, up to a maximum of 50% increase
    if (growth < 3) {
        growth += 0.01;
        document.getElementById('clicker-button1').style.transform = 'scale(' + growth + ')';
    }

    // Restart the timer if it's not already running
    if (!timer) {
        var timeLeft = 10;
        timer = setInterval(function() {
            document.getElementById('timer').innerText = "Time: " + timeLeft;
            timeLeft--;
            
            if (timeLeft < 0) {
                clearInterval(timer);
                timer = null;
                resetGrowth();
                resetUpgrade();
            }
        }, 1000);
    }
}

function resetScore() {
    score = 0;
    document.getElementById('score1').innerText = "Score: " + score;
}

function resetGrowth() {
    growth = 1.0;
}

function resetUpgrade() {
    upgradeMultiplier = 1.0;
}

function incrementNumber() {
    return 1 * upgradeMultiplier; // The default increment is 1, this allows the upgrades to be applied
}

function upgradeOne() {
    upgradeMultiplier = 1.5;
}

function upgradeTwo() {
    upgradeMultiplier = 2.0;
}

function upgradeThree() {
    upgradeMultiplier = 2.5;
}

function saveScore() {
    var name = document.getElementById('name-input').value;
    

    if (name.trim() === '') {
        alert('Please enter your name.');
        return;
    }

    var newScore = {
        name: name,
        score: score
    };

    scores.push(newScore);
    localStorage.setItem('scores', JSON.stringify(scores));
    displayScores();
    document.getElementById('name-input').value = '';
    resetScore();
}

function displayScores() {
    var scoreTableBody = document.getElementById('score-table-body');
    scoreTableBody.innerHTML = '';

    for (var i = 0; i < scores.length; i++) {
        var scoreRow = document.createElement('tr');
        var nameCell = document.createElement('td');
        var scoreCell = document.createElement('td');

        nameCell.innerText = scores[i].name;
        scoreCell.innerText = scores[i].score;

        scoreRow.appendChild(nameCell);
        scoreRow.appendChild(scoreCell);
        scoreTableBody.appendChild(scoreRow);
    }
}

// Initial display of scores
displayScores();
</script>
</html>

