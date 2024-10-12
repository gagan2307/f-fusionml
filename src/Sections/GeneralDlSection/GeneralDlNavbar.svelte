<script>
	import { cubicInOut } from 'svelte/easing';
	import fusionmlLogo from '$lib/LandingPage/fusionmlLogo.webp';
	import { goto } from '$app/navigation';
	import backIcon from '$lib/SpamDetection/back-icon.png';
	import threeDots from '$lib/SpamDetection/three-dots.png';
</script>

<nav class="fixed left-0 top-0 z-20 h-16 w-full bg-white/10 backdrop-blur-md">
	<div class="custom-padding mx-auto w-full px-0">
		<div class="flex h-20 items-center justify-between">
			<!-- Logo Placeholder -->
			<div class="flex-shrink-0">
				<!-- svelte-ignore a11y-click-events-have-key-events -->
				<!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
				<img
					src={backIcon}
					alt="Logo"
					on:click={() => {
						goto('/dl');
					}}
					class="-mt-[20px] ml-[20px] h-[35px] w-[40px]"
				/>
			</div>

			<!-- Navbar Links -->
			<div class="ml-auto hidden space-x-8 md:flex">
				<!-- svelte-ignore a11y-click-events-have-key-events -->
				<!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
				<img
					src={threeDots}
					alt="Logo"
					on:click={() => {
						alert('Clicked');
					}}
					class="-mt-[20px] h-[30px] w-2"
				/>
			</div>
		</div>
	</div>
</nav>

<style>
	.custom-padding {
		padding-right: 28px;
	}
</style>
