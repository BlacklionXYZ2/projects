function playAudio(path) {
  let audio = new Audio(path);
  audio.play();
  audio.currentTime = 0;
}
