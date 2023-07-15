import { nodeResolve } from '@rollup/plugin-node-resolve';

export default {
	input: 'src/script.js',
	output: {
		file: 'dist/script.js',
		format: 'cjs'
	},
	plugins: [nodeResolve()]
};