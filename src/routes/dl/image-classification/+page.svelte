<script>
	import BG from '$lib/MLListPage/background.png';
	import GeneralDlNavbar from '../../../Sections/GeneralDlSection/GeneralDlNavbar.svelte';
</script>

<main class="relative min-h-screen overflow-hidden">
	<section id="nav-textsum">
		<GeneralDlNavbar />
	</section>

	<!-- Background Image -->
	<div class="absolute inset-0 -z-50 h-full w-full bg-cover bg-center">
		<img src={BG} alt="BackgroundImage" class="min-h-full min-w-full object-cover" />
	</div>
</main>

<style>
</style>
