MathJax = {
	loader: { load: ['[tex]/physics', '[tex]/cancel'] },
	chtml: { displayAlign: 'left' },
	tex: {
		packages: { '[+]': ['physics', 'cancel'] },
		inlineMath: [['$', '$'], ['\\(', '\\)']],
		macros: {
			//- dvp: ["{ \\dfrac{\\partial{#1}}{\\partial{#2}} }",2],
			dbd: ["{ \\frac{\\Delta{#1}}{\\Delta{#2}}}", 2],
			const: ["{\\operatorname{const}}"],
			oiint: ["{\\unicode{x222F}}"],
			oiiint: ["{\\unicode{x2230}}"],
			EMF: ["{\\mathscr{E}}"],
			def: ["{\\operatorname{def}}"],
			series: ['{\\sum_{n=#1}^{+\\infty}}', 1, '1'],
			Nseries: ['{\\sum_{n=#1}^{N}}', 1, '1'],
			def_by: ["{\\overset {\\operatorname{def}}} {#1}", 1],
			euint: ["{\\int #2 \\dd #1} = #3 + C", 3, 'x'],
			bvec: ["{\\overrightarrow {#1}}", 1],
			def: ["{\\text{≝}}"],
			if: ["{\\text{Если }}"],

		}
	},
	startup: {
		pageReady: () => {
			return MathJax.startup.defaultPageReady().then(() => {
				let equations = document.querySelectorAll("mjx-container.MathJax");
				for (let equation of equations) {
					let parentWidth = 0
					let buf = equation.parentElement;
					while (buf != null && buf.innerWidth == null) {
						buf = buf.parentElement
					}
					if (buf == null) { parentWidth = window.innerWidth }
					else { parentWidth = equation.parentElement.innerWidth }
					if (equation.offsetWidth > parentWidth) {
						equation.classList.add("equation");
					}
				}
				console.log('MathJax initial typesetting complete');
			});
		}
	}
};