"use strict";

let numId;
document.querySelector(".num").addEventListener("click", function () {
  numId = document.querySelector(".num").textContent;
  console.log(numId);
});
