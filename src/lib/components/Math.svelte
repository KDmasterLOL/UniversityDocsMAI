<script lang="ts">
	import katex from 'katex';
	import 'katex/dist/katex.min.css';

	export let expression: string;
	export let is_block = false;
	const props = {
		macros: {
			'\\dd': '\\text{d}#1',
			'\\ddv': '\\frac{\\dd{#1}}{\\dd{#2}}',
			'\\same': String.raw`\left\{#1\mathbb{=}#2\right\}`,
			'\\arsh': `\\operatorname{arsh}`,
			'\\arch': `\\operatorname{arch}`,
			'\\arth': `\\operatorname{arth}`,
			'\\arcth': `\\operatorname{arcth}`,
			'\\const': `\\operatorname{const}`,
			'\\vb': `\\textbf{#1}`
		},
		displayMode: is_block,
		throwOnError: false
	};
</script>

{#if expression}
	{@html katex.renderToString(expression.replace('\n', ' '), props)}
{/if}
