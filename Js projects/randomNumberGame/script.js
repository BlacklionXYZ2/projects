'use strict';
/*
let number = document.querySelector('.message').textContent;
console.log(number);
//document.querySelector('.message').textContent = '∆∂ß∑®π';
console.log(document.querySelector('.message').textContent);
console.log(document.querySelector('.guess').value);
*/
let range = 10;
let ranNumber = Math.trunc(Math.random() * range) + 1;
let score = Number(document.querySelector('.score').textContent);
let highScore = Number(document.querySelector('.highscore').textContent);
let guess;
let guesses = 0;
let red = 71;
let green = 207;
let blue = 67;
//let prevGuess;

//document.querySelector('.number').textContent = ranNumber;
document.querySelector('.between').textContent =
  '(Between 1 and ' + range + ')';

document.querySelector('.check').addEventListener('click', function () {
  guess = Number(document.querySelector('.guess').value);

  if (guess > range || guess <= 0) {
    document.querySelector('.message').textContent = 'Invalid number';
  } else if (guess === ranNumber) {
    document.querySelector('.message').textContent = 'CORRECT!!';
    score = score + 3;
    document.querySelector('.body').style.backgroundColor =
      'rgb(' + red + ', ' + green + ', ' + blue + ')'; //'rgb(71, 207, 67)'; //'#47cf40'; <-- ways rgb values can be represented
    document.querySelector('.score').textContent = score;
  } else if (guess < ranNumber) {
    document.querySelector('.message').textContent = 'The number is higher';
    score--;
    document.querySelector('.score').textContent = score;
  } else if (guess > ranNumber) {
    document.querySelector('.message').textContent = 'The number is lower';
    score--;
    document.querySelector('.score').textContent = score;
  }
  if (score > highScore) {
    highScore = score;
    document.querySelector('.highscore').textContent = score;
  }
  guesses++;
  document.querySelector('.guessN').textContent = String(guesses) + ' Guesses';
  document.querySelector('.history').textContent = guess;
  document.querySelector('.guess').value = '';
  return guess;
});

document.querySelector('.again').addEventListener('click', function () {
  if (
    guess != ranNumber ||
    document.querySelector('.message').textContent != 'CORRECT!!'
  ) {
    document.querySelector('.message').textContent =
      'The number was ' + ranNumber + '.';
  } else {
    document.querySelector('.message').textContent =
      'Guess a number between 1 and 20';
  }
  guess = Number(document.querySelector('.guess').value);
  document.querySelector('.guess').value = '';
  ranNumber = Math.trunc(Math.random() * range) + 1;
  if (guess == null || undefined) {
    guess = 0;
  }
  guesses = 0;
  document.querySelector('.guessN').textContent = String(guesses) + ' Guesses';
  document.querySelector('.history').textContent = '';
  document.querySelector('.body').style.backgroundColor = '#222222';
  //document.querySelector('.number').textContent = ranNumber;
});

// const element = document.querySelector('.number');
// document.querySelector('.number').style.backgroundColor = 'red';
// const computedHeight = window
//   .getComputedStyle(element)
//   .getPropertyValue('height');
