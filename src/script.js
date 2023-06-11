function process_wavy_text() {
  let elements = document.getElementsByClassName("wavy-text");
  Array.from(elements).forEach((element) => {
    element.innerHTML = element.textContent.replaceAll(
      /\S/g,
      "<span>$&</span>"
    );
    spans = element.querySelectorAll("span");
    for (let i = 0; i < spans.length; i++) {
      spans[i].style.animationDelay = i * 0.05 + "s";
    }
  });
}
function process_collapsable() {
  let elements = document.querySelectorAll("span.collapse");
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
});
