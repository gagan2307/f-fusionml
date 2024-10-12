<script>
	import { createEventDispatcher } from 'svelte';
	import { goto } from '$app/navigation';

	export let index = '';
	export let title = '';
	export let description = '';
	export let img = '';
	export let source = '';

	const dispatch = createEventDispatcher();

	// Dispatch event when mouse enters the button
	function handleMouseEnter() {
		console.log('DEBUG Mouse ENtered');
		dispatch('hover', { index, title, description });
	}

	// Dispatch event when mouse leaves the button
	function handleMouseLeave() {
		console.log('DEBUG Mouse Left');
		dispatch('leave');
	}
</script>

<!-- svelte-ignore a11y-no-static-element-interactions -->
<!-- svelte-ignore a11y-click-events-have-key-events -->
<button
	class="flex w-full items-center justify-start rounded-full bg-gradient-to-r from-purple-500 to-pink-500 p-4 text-white hover:bg-gradient-to-l focus:outline-none focus:ring-4 focus:ring-purple-200 max-2xs:p-2 lg:w-80 dark:focus:ring-purple-800"
	on:mouseenter={handleMouseEnter}
	on:click={() => {
		goto(`${source}`);
	}}
>
	<!-- Index Section -->
	<div class="max-2xs:text-md mr-4 flex-shrink-0 text-lg font-semibold text-black">
		{index}.
	</div>

	<!-- Image Section -->
	<div class="flex-shrink-0">
		<img
			src={img}
			alt="Icon"
			class="h-10 w-10 object-contain max-xs:h-8 max-xs:w-8 max-2xs:h-6 max-2xs:w-6"
		/>
	</div>

	<!-- Text Section -->
	<div class="ml-4 text-black">
		<h2 class="text-left text-lg font-semibold max-2xs:text-sm">{title}</h2>
		<p class="text-left text-sm max-2xs:text-xs">{description}</p>
	</div>
</button>

<style>
	/* Additional styles if needed */
</style>
