document.querySelector(".enter").addEventListener(click, function () {
  document.querySelector(".iosTitle").textContent =
    document.querySelector(".title").textContent;
  document.querySelector(".anTitle").textContent =
    document.querySelector(".iosTitle").textContent;

  document.querySelector(".iosCont").textContent =
    document.querySelector(".text").textContent;
  document.querySelector(".anCont").textContent =
    document.querySelector(".iosCont").textContent;
});
