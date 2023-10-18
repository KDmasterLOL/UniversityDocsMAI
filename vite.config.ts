import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
// import { viteSingleFile } from "vite-plugin-singlefile";

export default defineConfig({
	plugins: [sveltekit(
		// 	{
		// 	onwarn(warning, defaultHandler) {
		// 		// don't warn on <marquee> elements, cos they're cool
		// 		if (warning.code === 'a11y-distracting-elements') return;

		// 		// handle all other warnings normally
		// 		defaultHandler(warning);
		// 	}
		// }
	)],
	optimizeDeps: { include: ['katex'] },
	server: {
		host: '0.0.0.0',
	}

});
