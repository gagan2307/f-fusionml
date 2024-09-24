<script>
	export let index = '';
	export let title = '';
	export let description = '';
	export let img = '';
</script>

<div
	class="flex w-full items-center justify-start rounded-full bg-gradient-to-r from-purple-500 to-pink-500 p-4 text-white hover:bg-gradient-to-l focus:outline-none focus:ring-4 focus:ring-purple-200 lg:w-80 dark:focus:ring-purple-800"
>
	<!-- Index Section -->
	<div class="mr-4 flex-shrink-0 text-lg font-semibold text-black">
		{index}.
	</div>

	<!-- Image Section -->
	<div class="flex-shrink-0">
		<img src={img} alt="Icon" class="h-10 w-10 object-contain" />
	</div>

	<!-- Text Section -->
	<div class="ml-4 text-black">
		<h2 class="text-left text-lg font-semibold">{title}</h2>
		<p class="text-left text-sm">{description}</p>
	</div>
</div>

<style>
	/* Additional styles if needed */
</style>
