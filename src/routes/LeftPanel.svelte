<script>
	import { browser } from '$app/environment';
	import TableOfContents from '$lib/components/TableOfContents/TableOfContents.svelte';
	import { gsap } from 'gsap';

	let width = 0;
	let left_panel = false;
	$: if (browser) {
		document.documentElement.style.setProperty('--left-panel', left_panel ? '1' : '0');
	}
</script>

<aside id="left-panel" bind:clientWidth={width}>
	<TableOfContents match_headers={[1, 2, 3, 4]} />
</aside>
<button class="switcher" on:click={() => (left_panel = !left_panel)}>
	<svg viewBox="0 0 100 80">
		{#each { length: 3 } as _, i}
			{@const y = 10 + i * 30}
			<line x1="20" y1={y} x2="80" y2={y} />
		{/each}
	</svg>
</button>

<style lang="scss">
	#left-panel {
		position: fixed;
		top: 0;
		bottom: 0;
		left: 0;
		background-color: var(--background-color);
		width: calc(var(--padding-main) * 2);
		box-sizing: border-box;
		z-index: $pop-up-index;
		border-right: 0.15rem solid var(--text-color);
		background: linear-gradient(to left, white 0, gray 7px, black 1rem, black 100%);
		padding: 1rem;

		transform: translateX(calc(-100% + var(--left-panel) * 100%));
		transition: transform $left-panel-speed ease-in-out;

		@media screen and (width <= 900px) {
			width: 100vw;
		}

		& + .switcher {
			@include toolbar-icon {
				left: calc(var(--padding-main) * var(--left-panel) * 2 + $screen-save);
			}
			box-shadow: 0 0 10px 2px var(--text-color);
			transition: box-shadow ease 500ms, left $left-panel-speed ease-in-out;
			@media screen and (width <= 900px) {
				left: $screen-save;
			}
			svg {
				background-color: var(--text-color);
				line {
					stroke: var(--background-color);
					stroke-width: 10px;
				}
			}
			&:hover {
				box-shadow: 0 0 10px 10px var(--text-color);
			}
		}
	}
</style>
