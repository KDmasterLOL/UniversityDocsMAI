<script lang="ts">
	import Prism from 'prismjs';
	import Header from './Header.svelte';
	import 'katex/dist/katex.min.css';
	import '$lib/styles/index.scss';
</script>

<Header />
<main>
	<slot />
</main>
<svelte:head>
	<script
		type="module"
		src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/copy-tex.mjs"
		integrity="sha384-bVEnwt0PtX+1EuJoOEcm4rgTUWvb2ILTdjHfI1gUe/r5fdqrTcQaUuRdHG2DciuQ"
		crossorigin="anonymous"
	></script>
</svelte:head>

<style lang="scss">
	main {
		margin: {
			left: var(--content-margin);
			right: var(--content-margin);
		}
		@media screen and (width <= 900px) {
			margin: 0;
		}
	}
</style>
