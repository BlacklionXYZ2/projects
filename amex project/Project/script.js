'use strict';

// const getText = function (element) {
//   if (document.querySelector(element).value == null || undefined) {
//     document.querySelector(element).value == '';
//   }
//   let text = document.querySelector(element).value;
//   return text;
// };

const getText2 = function (element) {
  // if (document.querySelector(element).value == null || '' || ' ' || undefined) {
  //   document.querySelector(element).value = '';
  // }
  return document.querySelector(element).value;
};

const getTitle = function () {
  return document.querySelector('#adtitle').value;
};

let text = {
  1: '.iosCont',
  2: '.anCont',
};

let t = {
  1: ' ',
  2: ' ',
  3: ' was ',
  4: ' on the ',
  5: ' ',
  6: ' ',
  7: ' on your ',
  8: ' ',
  9: ' ',
};

let g = {
  1: ' ',
  2: ' ',
  3: ' was ',
  4: ' on the ',
  5: ' ',
  6: ' ',
  7: ' on your ',
  8: ' ',
  9: ' ',
};
// #prefix1 ''1 #amount2 ' '2 #type3 was3 #action4 on the4 #date5 ' '5 #object6 ' '6 #entity7 from the7 #accType8 ' '8 #account9 ' '9 #other10
let e = {
  1: '#prefix',
  2: '#amount',
  3: '#type',
  4: '#action',
  5: '#date',
  6: '#object',
  7: '#entity',
  8: '#accType',
  9: '#account',
  10: '#other',
};

function test() {
  for (let i = 1; i < e.length; i++) {
    if (document.querySelector(e[i]).value == '' || null) {
      t[i] = ' ';
    } else {
      t[i] = g[i];
    }
  }
}
let textW;

// function writeText() {
//   for (let i = 1; i <= e.length; i++) {
//     if (i != t.length) {
//       textW = textW + (getText2(e[i]) + t[i]);
//     } else {
//       textW = textW + getText2(e[i]);
//     }
//   }
//   return textW;
// }

document.querySelector('.enter').addEventListener('click', function () {
  test();
  if (document.querySelector('#action').value == 'scheduled') {
    t[4] = ' for the ';
  }
  document.querySelector('#adtitleLive').textContent = getTitle();
  document.querySelector('#adtitleLive2').textContent =
    document.querySelector('#adtitleLive').textContent;

  document.querySelector('.iosCont').textContent =
    getText2(e[1]) +
    t[1] +
    getText2(e[2]) +
    t[2] +
    getText2(e[3]) +
    t[3] +
    getText2(e[4]) +
    t[4] +
    getText2(e[5]) +
    t[5] +
    getText2(e[6]) +
    t[6] +
    getText2(e[7]) +
    t[7] +
    getText2(e[8]) +
    t[8] +
    getText2(e[9]) +
    t[9] +
    getText2(e[10]);
  document.querySelector('.anCont').textContent =
    document.querySelector('.iosCont').textContent;
  event.preventDefault;
});

let state = false;
document.querySelector('.dateToggle').addEventListener('click', function () {
  let on =
    '<input id="date" class="Content" type="text" placeholder="Date"></input>';
  let off =
    '<select   id="date" class="Content"> <option value="N/A">N/A</option> </select>';
  if ((state = false)) {
    document.querySelector('.date').innerHTML =
      '<select   id="date" class="Content"> <option value="N/A">N/A</option> </select>';
    state = true;
    console.log(1);
  } else if ((state = true)) {
    document.querySelector('.date').innerHTML =
      '<input id="date" class="Content" type="text" placeholder="Date"></input>';
    state = false;
    console.log(2);
  }
  console.log(0);
});

// let count = 0;
// document.querySelector('.darkMode').addEventListener('click', function () {
//   if (count > 1) {
//     count = 0;
//   }
//   if (count == 1) {
//     document.querySelector('.darkMode').style.backgroundColor =
//       'rgba(50,255,50,1)';
//     document.querySelector('.darkMode').textContent = 'on';
//     document.querySelector('.iosCont').style.color =
//       'rgba(255, 255, 255, 0.955);';
//     document.querySelector('.iosTitle').style.color =
//       document.querySelector('.iosCont').style.color;
//   } else if (count == 0) {
//     document.querySelector('.darkMode').style.backgroundColor =
//       'rgba(239,28,28,1)';
//     document.querySelector('.darkMode').textContent = 'off';
//     document.querySelector('.iosCont').style.color = 'rgb(0,0,0)';
//     document.querySelector('.iosTitle').style.color =
//       document.querySelector('.iosCont').style.color;
//   }
//   count++;
// });
