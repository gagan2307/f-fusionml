<script>
	import NavbarSection from '../../Sections/LandingPageSections/NavSection.svelte';
	import BG from '$lib/MLListPage/background.png';
	import InfoMainDl from '../../Sections/DlListSections/InfoMainDL.svelte';
</script>

<main class="relative flex min-h-screen flex-col justify-between">
	<section id="nav-bar">
		<NavbarSection />
	</section>

	<!-- Background Image -->
	<div class="absolute inset-0 -z-50 h-full w-full bg-cover bg-center">
		<img src={BG} alt="BackgroundImage" class="h-full w-full object-cover" />
	</div>

	<section id="info-section" class="mt-10 flex-grow px-6 lg:mt-20">
		<InfoMainDl />
	</section>
</main>

<style>
	/* Remove html and body selectors, as Tailwind provides min-h-screen */
</style>
