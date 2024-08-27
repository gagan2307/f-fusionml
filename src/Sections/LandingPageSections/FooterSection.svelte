<script>
	// Add any necessary script or props here
</script>

<footer
	class="footer-container absolute bottom-0 left-0 flex w-full items-center justify-between px-4 py-4"
>
	<!-- Left side content with logo and social icons -->
	<div class="flex flex-col items-center space-y-2">
		<!-- Logo -->
		<div class="footer-logo rounded-full bg-gradient-to-r from-pink-400 to-purple-500 p-1">
			<div class="rounded-full bg-white p-2">
				<!-- Placeholder for logo, replace with actual logo image -->
				<span class="font-bold text-pink-500">F</span>
			</div>
		</div>

		<!-- Social Media Icons -->
		<div class="flex space-x-4">
			<a href="https://linkedin.com" target="_blank" class="text-black hover:text-gray-700">
				<i class="fab fa-linkedin"></i>
			</a>
			<a href="https://github.com" target="_blank" class="text-black hover:text-gray-700">
				<i class="fab fa-github"></i>
			</a>
		</div>
	</div>

	<!-- Right side text -->
	<div class="flex flex-col items-end text-sm text-black sm:text-base">
		<span>Privacy Policy</span>
		<span>All Rights Reserved</span>
	</div>
</footer>

<style>
	.footer-container {
		/* Ensure the footer is fully transparent */
		background-color: transparent;
		padding-bottom: 20px; /* Add padding at the bottom */
	}

	.footer-logo {
		width: 40px;
		height: 40px;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.footer-container a i {
		font-size: 1.5rem; /* Adjust icon size */
	}
</style>
