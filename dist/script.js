
function process_wavy_text() {
  let elements = document.getElementsByClassName("wavy-text");
  for (let element of elements) {
    element.innerHTML = element.textContent.replaceAll(
      /\S/g,
      "<span>$&</span>"
    );
    let spans = element.querySelectorAll("span");
    for (let i = 0; i < spans.length; i++) {
      let span = spans[i];
      span.style.animationDelay = i * 0.2 + "s";
    }
    spans[spans.length - 1].addEventListener("animationend", () => {
      element.classList.remove("wavy-text");
      setTimeout(() => { element.classList.add("wavy-text") }, 1000);
    })
  };
}
function process_collapsible() {
  let elements = document.querySelectorAll("span.collapsible_toggle + span.collapsible");
  for (let element of elements) {
    element.style.display = "none"
    element.previousElementSibling.addEventListener("click", () => {
      if (element.style.display == "none") {
        element.style.display = ""
      } else {
        element.style.display = "none"
      }
    })
  }
}
function process_folder() {
  let elements = document.querySelectorAll("span.folder + span.folder-content");
  for (let element of elements) {
    let prev = element.previousElementSibling;
    element.style.display = "none"
    prev.addEventListener("click", () => {
      prev.style.display = "none"
      element.style.display = ""
    })
    element.addEventListener("click", () => {
      prev.style.display = ""
      element.style.display = "none"
    })
  }
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
  Array.from(elements).forEach(element => {
    element.addEventListener("click", () => {
      if (element.getAttribute("open") == null) {
        element.setAttribute("open", "");
      } else {
        element.removeAttribute("open");
      }
    });
  });
}
function find_next(element, selector, max_level = 1) {
  let level = 0;
  while (element) {
    if (element.matches(selector)) {
      return element
    }
    if (!element.nextElementSibling && level < max_level) { element = element.parentElement }
    else { element = element.nextElementSibling }
  }
  return null
}
function toggle_process() {
  let toggles = document.querySelectorAll("toggle")
  for (let toggle of toggles) {
    let target_selector = toggle.getAttribute("target");
    let target = null;
    target = find_next(toggle.parentElement, target_selector)
    if (target == null) { continue }
    target.classList.add("toggled");
    target.classList.add("hidden");
    toggle.addEventListener("click", () => {
      toggle.classList.toggle("pressed");
      target.classList.toggle("hidden");
    });
  }
}
function process_tip() {
  let elements = document.querySelectorAll("span.tip_for + span.tip");
  for (let el of elements) {
    el.style.display = "none";
    el.previousElementSibling.addEventListener("click", () => {
      if (el.style.display == "none") {
        el.style.display = ""
      }
      else {
        el.style.display = "none"
      }
    })
  }
}
document.addEventListener("DOMContentLoaded", () => {
  process_wavy_text();
  process_collapsable();
  process_themeSwitch();
  process_tip();
  process_collapsible();
  process_folder();
  toggle_process();
});

document.addEventListener("touchstart", function () { }, true);
