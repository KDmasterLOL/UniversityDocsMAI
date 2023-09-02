function draw() {
	try {
		// compile the expression once
		const expression = document.getElementById('eq').value
		const expr = math.compile(expression)

		// evaluate the expression repeatedly for different values of x
		const xValues = math.range(-10, 10, 0.5).toArray()
		const yValues = xValues.map(function (x) {
			return expr.evaluate({ x: x })
		})

		// render the plot using plotly
		const trace1 = {
			x: xValues,
			y: yValues,
			type: 'scatter'
		}
		const data = [trace1]
		Plotly.newPlot('plot', data)
	}
	catch (err) {
		console.error(err)
		alert(err)
	}
}

function process_graph() {
	let graphs = document.querySelectorAll(".plot");
	for (let graph of graphs) {
		let expression = graph.dataset.graph
		const expr = math.compile(expression)

		// evaluate the expression repeatedly for different values of x
		const xValues = math.range(-10, 10, 1).toArray()
		const yValues = xValues.map(function (x) {
			return expr.evaluate({ x: x })
		})
		Plotly.newPlot(graph, [{
			x: xValues,
			y: yValues
		}], {
			margin: { t: 0 }, margin: {
				l: 25,
				r: 25,
				b: 25,
				t: 0,
				pad: 4
			}, xaxis: { automargin: true }, yaxis: { automargin: true }, title: false
		}, { staticPlot: true })
	}
}

document.addEventListener("DOMContentLoaded", () => {
	process_graph()
})