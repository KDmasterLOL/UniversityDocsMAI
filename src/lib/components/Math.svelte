<script lang="ts">
	import renderMathInElement from 'katex/contrib/auto-render';

	import katex from 'katex/dist/katex';
	import katex from 'katex';
	import { onMount } from 'svelte';

	let el: HTMLElement;
	// onMount(() => {
	// 	renderMathInElement(el, {
	// 		delimiters: [
	// 			{ left: '$$', right: '$$', display: true },
	// 			{ left: '$', right: '$', display: false },
	// 			{ left: '\\(', right: '\\)', display: false },
	// 			{ left: '\\[', right: '\\]', display: true }
	// 		],
	// 		macros: { '\\dd': '\\text{d}#1' },
	// 		throwOnError: false
	// 	});
	// 	katex.renderToString();
	// });
</script>

<section bind:this={el} class="math">
	<slot />
</section>

<svelte:head />
