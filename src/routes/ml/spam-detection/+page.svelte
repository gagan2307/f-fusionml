<script>
	import BG from '$lib/MLListPage/background.png';
	import SpamDNavbar from '../../../Sections/SpamDetectionPageSections/SpamDNavbar.svelte';
	import SpamDHeading from '../../../Sections/SpamDetectionPageSections/SpamDHeading.svelte';
	import SpamDInput from '../../../Sections/SpamDetectionPageSections/SpamDInput.svelte';
</script>

<main>
	<section id="nav-spam">
		<SpamDNavbar />
	</section>

	<!-- Background Image -->
	<div class="absolute inset-0 -z-50 h-full w-full bg-cover bg-center">
		<img src={BG} alt="BackgroundImage" class="h-full w-full object-cover" />
	</div>

	<section id="heading-spam">
		<SpamDHeading />
	</section>

	<section id="heading-spam">
		<SpamDInput />
	</section>
</main>

<style>
</style>
