<script lang="ts">
	import { browser } from '$app/environment';
	import { onMount } from 'svelte';

	let switcher: HTMLElement;

	onMount(() => {
		let current = switcher?.children[0];
		for (let index = 0; index < switcher?.children.length; index++) {
			const element = switcher.children[index];
			element.addEventListener('click', (ev) => {
				const ele: HTMLElement = ev.currentTarget;
				if (ele.nextElementSibling) {
					ele.classList.toggle('hidden');
					ele.nextElementSibling.classList.toggle('hidden');
				} else {
					ele.classList.toggle('hidden');
					current.classList.toggle('hidden');
				}
			});

			if (index != 0) {
				element.classList.toggle('hidden');
			}
		}
	});
</script>

<section bind:this={switcher} class="switcher">
	<slot />
</section>

<style>
	section {
		user-select: none;
		overflow-x: scroll;
	}
</style>
