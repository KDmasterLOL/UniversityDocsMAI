<script>
	import { text } from '@sveltejs/kit';
	import katex from 'katex';
</script>

<template lang="pug">
+math
	article: include /articles/PHYSICS/index
</template>
