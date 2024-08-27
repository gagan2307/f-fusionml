<script>
	export let label = 'Button'; // You can customize the button label via props
</script>

<button class="custom-button rounded-full px-8 py-4 font-bold text-white">
	{label}
</button>

<style>
	.custom-button {
		/* Updated gradient for the button */
		background: linear-gradient(to bottom, #7a4abf 0%, #a57bc9 25%, #e8d0e0 75%, #f3e6f2 100%);
		background-clip: padding-box;
		position: relative;
		z-index: 1;
	}

	.custom-button:before {
		/* Slightly lighter radial gradient */
		content: '';
		position: absolute;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		background: radial-gradient(circle, #71527a 0%, #71527a 97%);
		z-index: -1;
		opacity: 0.5;
		border-radius: inherit;
	}

	.custom-button:hover {
		/* Slightly increase opacity on hover for better visibility */
		opacity: 0.9;
	}

	.custom-button:focus {
		outline: none;
		box-shadow: 0 0 0 3px rgba(255, 255, 255, 0.5);
	}

	@media (max-width: 640px) {
		.custom-button {
			/* Responsive padding for small screens */
			padding-left: 1.5rem;
			padding-right: 1.5rem;
			padding-top: 0.75rem;
			padding-bottom: 0.75rem;
			font-size: 0.875rem;
		}
	}

	@media (min-width: 641px) and (max-width: 1024px) {
		.custom-button {
			/* Responsive padding for medium screens */
			padding-left: 2rem;
			padding-right: 2rem;
			padding-top: 1rem;
			padding-bottom: 1rem;
			font-size: 1rem;
		}
	}

	@media (min-width: 1025px) {
		.custom-button {
			/* Larger size for large screens */
			padding-left: 3rem;
			padding-right: 3rem;
			padding-top: 1.5rem;
			padding-bottom: 1.5rem;
			font-size: 1.25rem;
		}
	}
</style>
