<script>
	import BG from '$lib/MLListPage/background.png';
	import SpamDNavbar from '../../../Sections/SpamDetectionPageSections/SpamDNavbar.svelte';
	import TextSumHeading from '../../../Sections/TextSummationPageSections/TextSumHeading.svelte';
	import TextSumInput from '../../../Sections/TextSummationPageSections/TextSumInput.svelte';
</script>

<main class="relative min-h-screen overflow-hidden">
	<section id="nav-textsum">
		<SpamDNavbar />
	</section>

	<!-- Background Image -->
	<div class="absolute inset-0 -z-50 h-full w-full bg-cover bg-center">
		<img src={BG} alt="BackgroundImage" class="min-h-full min-w-full object-cover" />
	</div>

	<section id="heading-textsum">
		<TextSumHeading />
	</section>

	<section id="heading-input">
		<TextSumInput />
	</section>
</main>

<style>
</style>
