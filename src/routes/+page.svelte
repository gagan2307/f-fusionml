<script>
	import BG from '$lib/LandingPage/BackgroundImageLanding.webp';
	import NavSection from '../Sections/LandingPageSections/NavSection.svelte';
	import HeadingSection from '../Sections/LandingPageSections/HeadingSection.svelte';
	import FooterSection from '../Sections/LandingPageSections/FooterSection.svelte';
</script>

<main class="relative flex min-h-screen w-screen flex-col">
	<!-- Navbar-Section -->
	<section id="navbar">
		<NavSection />
	</section>

	<!-- Background Image -->
	<div class="absolute inset-0 z-0 h-full w-full bg-cover bg-center">
		<img src={BG} alt="BackgroundImage" class="h-full w-full object-cover" />
	</div>

	<!-- Content Section -->
	<section id="content" class="flex flex-grow flex-col items-center justify-center">
		<HeadingSection />
	</section>

	<!-- Footer Section -->
	<section id="footer" class="z-10">
		<FooterSection />
	</section>
</main>

<style>
	/* Additional styles if needed */
</style>
