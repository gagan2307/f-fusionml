<script>
	// Any required logic can be added here
</script>

<div class="flex flex-col items-center justify-center gap-8 p-6 lg:flex-row">
	<!-- Enter Text Section -->
	<div class="flex w-full flex-col rounded-lg bg-white/70 p-6 shadow-md lg:w-1/2">
		<h2 class="mb-4 text-center text-2xl font-bold">Enter Text</h2>
		<textarea
			placeholder="Enter text here"
			class="h-40 w-full resize-none overflow-auto rounded-md border border-gray-300 p-4 focus:outline-none focus:ring-2 focus:ring-indigo-400"
			style="scrollbar-gutter: stable"
		></textarea>
	</div>

	<!-- Summary Section -->
	<div class="flex w-full flex-col rounded-lg bg-white/70 p-6 shadow-md lg:w-1/2">
		<h2 class="mb-4 text-center text-2xl font-bold">Summary</h2>
		<textarea
			placeholder="Summary here"
			class="h-40 w-full resize-none overflow-auto rounded-md border border-gray-300 p-4 focus:outline-none focus:ring-2 focus:ring-indigo-400"
			style="scrollbar-gutter: stable"
			readonly
		></textarea>
	</div>
</div>

<style>
	textarea {
		background-color: #f8f8f8;
		font-family: 'Arial', sans-serif;
	}
</style>
