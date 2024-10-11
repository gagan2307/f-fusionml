<script>
	import BG from '$lib/MLListPage/background.png';
	import SpamDNavbar from '../../../Sections/SpamDetectionPageSections/SpamDNavbar.svelte';
	import SpamDHeading from '../../../Sections/SpamDetectionPageSections/SpamDHeading.svelte';
	import SpamDInput from '../../../Sections/SpamDetectionPageSections/SpamDInput.svelte';
</script>

<main class="relative min-h-screen overflow-hidden">
	<section id="nav-spam">
		<SpamDNavbar />
	</section>

	<!-- Background Image -->
	<div class="absolute inset-0 -z-50 h-full w-full bg-cover bg-center">
		<img src={BG} alt="BackgroundImage" class="min-h-full min-w-full object-cover" />
	</div>

	<section id="heading-spam">
		<SpamDHeading />
	</section>

	<section id="heading-spam">
		<SpamDInput />
	</section>
</main>

<style>
	/* Ensures the main container takes the full height of the viewport */
	main {
		min-height: 100vh;
	}
</style>
