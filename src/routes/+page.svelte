<script>
	import BG from '$lib/LandingPage/BackgroundImageLanding.webp';
	import NavSection from '../Sections/LandingPageSections/NavSection.svelte';
</script>

<main>
	<!-- Navbar-Section -->
	<section id="navbar">
		<NavSection />
	</section>

	<!-- Background Image -->
	<div class="h-screen w-screen bg-cover bg-center">
		<img src={BG} alt="BackgroundImage" class="h-full w-full object-cover" />
	</div>
</main>

<style>
</style>
