<script>
	import { text } from '@sveltejs/kit';
	import Math from '$lib/components/Math.svelte';
</script>

<template lang="pug">
+math
	article: include /articles/PHYSICS/index
</template>
