import adapter from '@sveltejs/adapter-static';
// import { vitePreprocess } from '@sveltejs/kit/vite';
import preprocess from 'svelte-preprocess';
import { importAssets } from 'svelte-preprocess-import-assets'
import katex from "katex";

const dev = process.argv.includes('dev');
function convert_to_math(text) {
	return katex.renderToString(text, { macros: { '\\dd': '\\text{d}#1', '\\ddv': '\\frac{\\dd{#1}}{\\dd{#2}}' } })
}
/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: [preprocess({
		pug: {
			basedir: "./src/lib/pug",
			prependData: "include /mixins",
			filters: {
				"math": function (text, options) {
					return katex.renderToString(text, { macros: { '\\dd': '\\text{d}#1', '\\ddv': '\\frac{\\dd{#1}}{\\dd{#2}}' } })
				}
			},
		},
		scss: { includePaths: ["./src/lib/styles"], prependData: "@import 'variables','mixins';" },
	}), preprocess({
		replace: ([
			[
				/\${1,2}[a-zA-Zа-яА-Я_^{}\\, ρω+*…><ΔΦφ→\n\-–;&=≈0-9().:|\t\[\]]+\${1,2}/g,
				(body) => body.replace(/{/g, "&lcub;").replace(/}/g, "&rcub;")
			]
		]),
	}), importAssets()],
	kit: {
		adapter: adapter({
			pages: 'build',
			assets: 'build',
			fallback: undefined,
			precompress: false,
			strict: true
		}),
		paths: {
			base: dev ? '' : process.env.BASE_PATH,
		},
	}

};

export default config;
