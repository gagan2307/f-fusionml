<script>
	import CustomGradiantButton from '../../Components/CustomGradiantButton/CustomGradiantButton.svelte';
</script>

<section class="custom-padding flex h-screen w-full items-start justify-center lg:justify-start">
	<div
		class="translate-y-[200px] transform text-center sm:translate-y-[150px] lg:translate-x-[30px] lg:translate-y-[200px] lg:text-left"
	>
		<h1 class="text-5xl font-bold text-black sm:text-6xl md:text-6xl lg:text-[8.05rem]">
			FusionML
		</h1>
		<p class="mt-4 text-lg font-semibold text-gray-700 sm:text-3xl md:text-2xl lg:text-[1.725rem]">
			The Comprehensive Platform<br />For ML Innovation
		</p>

		<!-- Button Placement -->
		<div
			class="mt-12 flex flex-col items-center space-y-4 lg:flex-row lg:justify-start lg:space-x-6 lg:space-y-0"
		>
			<CustomGradiantButton link="/ml" label="Machine Learning" class="w-full sm:w-auto" />
			<CustomGradiantButton link="/dl" label="Deep Learning" class="w-full sm:w-auto" />
		</div>
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
			font-size: 5.65rem; /* Increase heading size */
		}
		p {
			margin-top: 1rem;
			font-size: 1.75rem; /* Increase subheading size */
		}
	}

	@media (max-width: 768px) {
		/* Increase font size and button size on small screens */
		h1 {
			font-size: 5.65rem; /* Increase heading size */
		}
		p {
			margin-top: 1rem;
			font-size: 1.75rem; /* Increase subheading size */
		}
		.flex-col .w-full {
			font-size: 1.5rem;
			padding: 1.5rem 3rem; /* Increase button size */
		}
	}

	@media (max-width: 640px) {
		/* Further adjust font size for very small screens */
		h1 {
			font-size: 3.34rem; /* Increase heading size */
		}
		p {
			margin-top: 1rem;
			font-size: 1.5rem; /* Increase subheading size */
		}

		/* Increase button size further for very small screens */
		.flex-col .w-full {
			font-size: 1.75rem;
			padding: 2rem 4rem; /* Increase button size */
		}
	}
</style>
