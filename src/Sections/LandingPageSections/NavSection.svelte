<script>
	import { cubicInOut } from 'svelte/easing';
	import fusionmlLogo from '$lib/LandingPage/fusionmlLogo.webp';
	import { goto } from '$app/navigation';

	let isMenuOpen = false;

	// Custom transition function combining fade and slide
	function combinedTransition(node, { duration = 300, easing = cubicInOut }) {
		return {
			duration,
			easing,
			css: (t) => `
				opacity: ${t};
				transform: translateY(${(1 - t) * -20}px);
			`
		};
	}
</script>

<nav class="fixed left-0 top-0 z-20 w-full bg-white/10 backdrop-blur-md">
	<div class="custom-padding mx-auto w-full px-0">
		<div class="flex h-20 items-center justify-between">
			<!-- Logo Placeholder -->
			<div class="flex-shrink-0">
				<!-- svelte-ignore a11y-click-events-have-key-events -->
				<!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
				<img
					src={fusionmlLogo}
					alt="Logo"
					on:click={() => {
						goto('/');
					}}
					class="h-28 w-32"
				/>
			</div>

			<!-- Navbar Links -->
			<div class="ml-auto hidden space-x-8 md:flex">
				<!-- Added ml-auto for full right alignment -->
				<a href="#" class="text-white hover:text-gray-300">Home</a>
				<a href="#" class="text-white hover:text-gray-300">About</a>
				<a href="#" class="text-white hover:text-gray-300">Community</a>
				<a href="#" class="text-white hover:text-gray-300">GitHub</a>
			</div>

			<!-- Mobile Menu Button -->
			<div class="z-30 flex items-center md:hidden">
				<button
					on:click={() => {
						isMenuOpen = !isMenuOpen;
					}}
					class="text-white focus:outline-none"
				>
					<svg
						class="h-6 w-6"
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						stroke="currentColor"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M4 6h16M4 12h16M4 18h16"
						/>
					</svg>
				</button>
			</div>
		</div>
	</div>

	<!-- Mobile Menu -->
	{#if isMenuOpen}
		<div
			class="z-20 bg-white/20 backdrop-blur-md md:hidden"
			transition:combinedTransition={{ duration: 300 }}
			style="position: absolute; top: 100%; left: 0; right: 0;"
		>
			<a href="#" class="block px-4 py-2 text-white hover:text-gray-300">Home</a>
			<a href="#" class="block px-4 py-2 text-white hover:text-gray-300">About</a>
			<a href="#" class="block px-4 py-2 text-white hover:text-gray-300">Community</a>
			<a href="#" class="block px-4 py-2 text-white hover:text-gray-300">GitHub</a>
		</div>
	{/if}
</nav>

<style>
	.custom-padding {
		padding-right: 28px;
	}
</style>
