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
  addMyGraph();
  addAnGraphs();
});

function addMyGraph() {
  const ctx = document.getElementById("myChart1");

  new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
      datasets: [
        {
          label: "# of Votes",
          data: [12, 19, 3, 5, 2, 3],
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
}
document.addEventListener("touchstart", function () {}, true);
function addAnGraphs() {
  let ctx = document.getElementById("myChart");
  const whiteColor = "rgba(0, 0, 0, 1)";
  const X_length = 6;
  const density = 10;

  let data = {
    labels: Array(X_length * density)
      .fill(0)
      .map((_, i) => i / density),
    datasets: [
      {
        label: "f(x) = x",
        function: function (x) {
          return x;
        },
        borderColor: whiteColor,
        data: [],
        fill: false,
      },
      {
        label: "f(x) = x?",
        function: function (x) {
          return x * x;
        },
        borderColor: whiteColor,
        data: [],
        fill: false,
      },
      {
        label: "f(x) = x * log(x)",
        function: function (x) {
          return x * Math.log(x);
        },
        borderColor: whiteColor,
        data: [],
        fill: false,
      },
    ],
  };
  Chart.register({
    id: "func",
    beforeInit: function (chart) {
      var data = chart.config.data;
      for (var i = 0; i < data.datasets.length; i++) {
        for (var j = 0; j < data.labels.length; j++) {
          var fct = data.datasets[i].function,
            x = data.labels[j],
            y = fct(x);
          data.datasets[i].data.push(y);
        }
      }
    },
  });
  var myBarChart = new Chart(ctx, {
    type: "line",
    data: data,
    options: {
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true,
            },
          },
        ],
      },
    },
  });
}
