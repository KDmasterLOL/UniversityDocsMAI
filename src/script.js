function process_wavy_text() {
  let elements = document.getElementsByClassName("wavy-text");
  Array.from(elements).forEach((element) => {
    element.innerHTML = element.textContent.replaceAll(
      /\S/g,
      "<span>$&</span>"
    );
    let spans = element.querySelectorAll("span");
    for (let i = 0; i < spans.length; i++) {
      spans[i].style.animationDelay = i * 0.05 + "s";
    }
  });
}
function process_themeSwitch() {
  let switcher = document.querySelector("button#switch-theme");
  let html = document.querySelector("html");
  switcher.addEventListener("click", () => {
    if (html.dataset.theme == "dark") {
      html.dataset.theme = "light";
    } else {
      html.dataset.theme = "dark";
    }
  });
}
function process_collapsable() {
  let elements = document.querySelectorAll(".collapse");
  Array.from(elements).forEach((element) => {
    element.addEventListener("click", () => {
      if (element.getAttribute("open") == null) {
        element.setAttribute("open", "");
      } else {
        element.removeAttribute("open");
      }
    });
  });
}
document.addEventListener("DOMContentLoaded", () => {
  process_wavy_text();
  process_collapsable();
  process_themeSwitch();
});

document.addEventListener("touchstart", function () {}, true);
