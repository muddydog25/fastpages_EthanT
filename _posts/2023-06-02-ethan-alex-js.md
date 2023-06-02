---
title: Ethan Tran and Alex Kumar JavaScript Exit Mini-Game
badges: true
comments: true
author: Ethan Tran
categories: [javascript, clicker game]
layout: base
---

<html>
<style>
#clicker-button1 {
    width: 100px;
    height: 100px;
    border: black;
    outline: black;
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
    border: black;
    outline: black;
    background-color: #f1f1f1; /* Set a background color */
    color: #333; /* Set the text color */
    cursor: pointer;
    transition: background-color 0.3s;
}
</style>

<div id="score1">Score: 0</div>
<div id="highscore1">High Score: 0</div>
<div id="timer">Time: 10</div>
<button id="clicker-button1" onclick="incrementScore()"></button>
<button onclick="upgradeOne()">1.5x Multiplier</button>
<button onclick="upgradeTwo()">2.0x Multiplier</button>
<button onclick="upgradeThree()">2.5x Multiplier</button>

<script>
var score = 0;
var highScore = 0;
var growth = 1.0;  // The button's initial size (as a scaling factor)
var upgradeMultiplier = 1.0; // setting up the multiplier
var timer;

function incrementScore() {
    score += incrementNumber();
    document.getElementById('score1').innerText = "Score: " + score;

    // check if the current score is higher than the high score
    if (score > highScore) {
        highScore = score;
        document.getElementById('highscore1').innerText = "High Score: " + highScore;
    }

    // increase the button's size by 1% for each click, up to a maximum of 50% increase
    if (growth < 3) {
        growth += 0.01;
        document.getElementById('clicker-button1').style.transform = 'scale(' + growth + ')';
    }

    // restart the timer if it's not already running
    if (!timer) {
        var timeLeft = 10;
        timer = setInterval(function() {
            document.getElementById('timer').innerText = "Time: " + timeLeft;
            timeLeft--;

            if (timeLeft < 0) {
                clearInterval(timer);
                timer = null;
                resetScore();
            }
        }, 1000);
    }
}

function resetScore() {
    score = 0;
    document.getElementById('score1').innerText = "Score: " + score;
}

function incrementNumber() {
    return 1 * upgradeMultiplier; // the default increment is 1, this allows the upgrades to be applied
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
</script>
</html>