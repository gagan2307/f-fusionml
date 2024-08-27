<script>
	// No script needed unless you want to add interactivity later.
</script>

<section class="custom-padding flex h-screen w-full items-start justify-center lg:justify-start">
	<div
		class="translate-y-[200px] transform text-center sm:translate-y-[150px] lg:translate-x-[30px] lg:translate-y-[200px] lg:text-left"
	>
		<h1 class="text-4xl font-bold text-black sm:text-6xl md:text-6xl lg:text-[8.05rem]">
			FusionML
		</h1>
		<p class="mt-2 text-base font-semibold text-gray-700 sm:text-2xl md:text-lg lg:text-[1.725rem]">
			The Comprehensive Platform<br />For ML Innovation
		</p>
	</div>
</section>

<style>
	.custom-padding {
		padding-left: 28px;
	}

	@media (max-width: 1024px) {
		/* Center the text for screens 1024px and below */
		.custom-padding {
			padding-left: 0;
		}
		.lg\:justify-start {
			justify-content: center !important;
		}
		.lg\:translate-x-\[30px\] {
			transform: translateY(200px) translateX(0) !important;
		}
		.lg\:text-left {
			text-align: center !important;
		}
		h1 {
			font-size: 4.65rem; /* Larger heading for small screens */
		}
		p {
			margin-top: 0.5rem;
			font-size: 1.25rem; /* Larger subheading for small screens */
		}
	}

	@media (max-width: 768px) {
		/* Increase font size on small screens */
		h1 {
			font-size: 4.65rem; /* Larger heading for small screens */
		}
		p {
			margin-top: 0.5rem;
			font-size: 1.25rem; /* Larger subheading for small screens */
		}
	}
	@media (max-width: 640px) {
		/* Increase font size on small screens */
		h1 {
			font-size: 2.34rem; /* Larger heading for small screens */
		}
		p {
			margin-top: 0.5rem;
			font-size: 1rem; /* Larger subheading for small screens */
		}
	}
</style>
