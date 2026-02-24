"use strict";

// while (randomNumber != 4) {
//   console.log(randomNumber);
//   randomNumber = Math.trunc(Math.random() * 6) + 1;
// }

let randomNumber = Math.trunc(Math.random() * 6) + 1;
let playerGuess = prompt(`A dice will be rolled. What number will it be?`);
let guesses = 1;

while (playerGuess != randomNumber && guesses <= 3) {
  console.log(`Wrong. Try again.`);
  guesses++;
  if (guesses <= 3) {
    playerGuess = prompt(`wrong, what is the number?`);
  }
}

if (playerGuess == randomNumber) {
  console.log(`Well done! The number was ${randomNumber}!`);
}

while (playerGuess != randomNumber && guesses == 3) {
  console.log(`Unfortunate. The number was ${randomNumber}.`);
  console.log(`Refresh the page to try again!`);
  guesses++;
}
