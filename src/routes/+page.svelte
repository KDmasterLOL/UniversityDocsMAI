<script>
	import katex from 'katex';
	import Math from '$lib/components/Math.svelte';
	
</script>


<Math expression="x_2+10"></Math>
<figure>
	<template lang="pug">
		+m x_1` + x^{223} + \sum
		//- div #[+m({'z':'чето','x':'чето','m':'чето'}) x_2+h+z=z^m];
	</template>

	<figcaption>Formula with some description of used symbols</figcaption>
</figure>

