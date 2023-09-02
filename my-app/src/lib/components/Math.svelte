<script lang="ts">
	import renderMathInElement from 'katex/contrib/auto-render';
	import 'katex/dist/katex.min.css';
	import _ from 'katex/dist/katex';
	import { onMount } from 'svelte';

	let el: HTMLElement;
	onMount(() => {
		renderMathInElement(el);
		renderMathInElement(document.body, {
			delimiters: [
				{ left: '$$', right: '$$', display: true },
				{ left: '$', right: '$', display: false },
				{ left: '\\(', right: '\\)', display: false },
				{ left: '\\[', right: '\\]', display: true }
			],
			throwOnError: false
		});
	});
</script>

<section bind:this={el} class="math">
	<slot />
</section>

<svelte:head>
	<script
		type="module"
		src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/copy-tex.mjs"
		integrity="sha384-bVEnwt0PtX+1EuJoOEcm4rgTUWvb2ILTdjHfI1gUe/r5fdqrTcQaUuRdHG2DciuQ"
		crossorigin="anonymous"
	></script>
</svelte:head>
