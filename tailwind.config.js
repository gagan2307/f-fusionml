/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],

	theme: {
		screens: {
			'4xs': '200px',
			'3xs': '300px',
			'2xs': '400px',
			'xs': '500px',
			'sm': '640px',    // Default Tailwind CSS breakpoints
			'md': '768px',
			'lg': '1024px',
			'xl': '1280px',
			'2xl': '1536px',
		},
		extend: {},
	},

	plugins: [],
};
