<script>
	import BG from '$lib/MLListPage/background.png';
	import SpamDNavbar from '../../../Sections/SpamDetectionPageSections/SpamDNavbar.svelte';
	import SentimentAnHeading from '../../../Sections/SentimentAnalyzerPageSections/SentimentAnHeading.svelte';
	import SentimentAnInput from '../../../Sections/SentimentAnalyzerPageSections/SentimentAnInput.svelte';
</script>

<main class="relative min-h-screen overflow-hidden">
	<section id="nav-textsum">
		<SpamDNavbar />
	</section>

	<!-- Background Image -->
	<div class="absolute inset-0 -z-50 h-full w-full bg-cover bg-center">
		<img src={BG} alt="BackgroundImage" class="min-h-full min-w-full object-cover" />
	</div>

	<section id="heading-sentiment">
		<SentimentAnHeading />
	</section>

	<section id="input-sentiment">
		<SentimentAnInput />
	</section>
</main>

<style>
</style>
