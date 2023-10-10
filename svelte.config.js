import adapter from '@sveltejs/adapter-static';
// import { vitePreprocess } from '@sveltejs/kit/vite';
import preprocess from 'svelte-preprocess';
import { importAssets } from 'svelte-preprocess-import-assets'
import katex from "katex";

const dev = process.argv.includes('dev');
/** @type {import('@sveltejs/kit').Config} */
const config = {
	vitePlugin: {
		onwarn(warning, defaultHandler) {
			// don't warn on <marquee> elements, cos they're cool
			return;
			if (warning.code === 'a11y-distracting-elements') return;

			// handle all other warnings normally
			defaultHandler(warning);
		}
	},
	preprocess: [preprocess({
		pug: {
			basedir: "./src/lib/pug",
			prependData: "include /mixins",
		},
		scss: { includePaths: ["./src/lib/styles"], prependData: "@import 'variables','mixins';" },
	}), importAssets()],
	kit: {
		adapter: adapter({
			pages: 'build',
			assets: 'build',
			fallback: undefined,
			precompress: false,
			strict: true
		}),
		alias: {
			"$img": "src/lib/img"
		},
		paths: {
			base: dev ? '' : process.env.BASE_PATH,
		},
	},
	compilerOptions: {

	}
};

export default config;
