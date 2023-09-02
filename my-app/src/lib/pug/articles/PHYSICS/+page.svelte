<script>
	import { text } from '@sveltejs/kit';
	import Math from '$lib/components/Math.svelte';
</script>

<template lang="pug">
include /mixins
+math
	article: include index
</template>
