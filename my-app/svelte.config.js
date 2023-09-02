import adapter from '@sveltejs/adapter-auto';
// import { vitePreprocess } from '@sveltejs/kit/vite';
import preprocess from 'svelte-preprocess';
import { importAssets } from 'svelte-preprocess-import-assets'


/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://kit.svelte.dev/docs/integrations#preprocessors
	// for more information about preprocessors
	preprocess: [preprocess({
		pug: { basedir: "./src/routes" },
		scss: { includePaths: ["./src/styles"] },
	}), preprocess({
		replace: ([
			[
				/\${1,2}[a-zA-Zа-яА-Я_^{}\\, ρω+*…><ΔΦφ→\n\-–;&=≈0-9().:|\t\[\]]+\${1,2}/g,
				(body) => body.replace(/{/g, "&lcub;").replace(/}/g, "&rcub;")
			]
		]),
	}), importAssets()],

	kit: {
		// adapter-auto only supports some environments, see https://kit.svelte.dev/docs/adapter-auto for a list.
		// If your environment is not supported or you settled on a specific environment, switch out the adapter.
		// See https://kit.svelte.dev/docs/adapters for more information about adapters.
		adapter: adapter()
	}
};

export default config;
