import adapter from '@sveltejs/adapter-static';
// import { vitePreprocess } from '@sveltejs/kit/vite';
import preprocess from 'svelte-preprocess';
import { importAssets } from 'svelte-preprocess-import-assets'
import katex from "katex";

const dev = process.argv.includes('dev');
/** @type {import('@sveltejs/kit').Config} */
const config = {
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
	}

};

export default config;
