
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
});

document.addEventListener("touchstart", function () { }, true);
