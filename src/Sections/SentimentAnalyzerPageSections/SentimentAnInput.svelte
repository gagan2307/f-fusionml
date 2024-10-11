<script>
	import { onMount } from 'svelte';
	let inputText = '';
	let resultText = 'Result';

	function analyzeText() {
		// Placeholder function for analyzing text
		// You can replace this with the actual logic or API call
		if (inputText.trim() === '') {
			resultText = 'Please enter some text!';
		} else {
			// Example analysis result (replace with actual API call result)
			resultText = 'Analysis result will be displayed here.';
		}
	}

	function clearText() {
		inputText = '';
		resultText = 'Result';
	}
</script>

<div class="flex flex-col items-center justify-center gap-6 p-4">
	<div class="mb-4 text-center text-2xl font-bold">Enter Text for Analysis</div>
	<div class="flex w-full max-w-6xl flex-col gap-8 md:flex-row">
		<!-- Enter Text Section -->
		<div class="flex w-full flex-col rounded-lg bg-white/80 p-6 shadow-lg md:w-2/3">
			<h2 class="mb-4 text-center text-2xl font-bold">Enter Text</h2>
			<textarea
				bind:value={inputText}
				placeholder="Enter Text Here"
				class="h-40 w-full resize-none overflow-auto rounded-md border border-gray-300 p-4 focus:outline-none focus:ring-2 focus:ring-indigo-500"
				style="scrollbar-gutter: stable; white-space: pre-wrap;"
			></textarea>
			<button
				on:click={clearText}
				class="mt-2 self-end rounded-full bg-gray-200 p-2 transition duration-150 ease-in-out hover:bg-gray-300"
				title="Clear Text"
			>
				🗑️
			</button>
		</div>

		<!-- Result Section -->
		<div class="flex w-full flex-col rounded-lg bg-white/80 p-6 shadow-lg md:w-1/3">
			<h2 class="mb-4 text-center text-2xl font-bold">Result Category</h2>
			<textarea
				bind:value={resultText}
				class="h-40 w-full resize-none overflow-auto rounded-md border border-gray-300 p-4 focus:outline-none focus:ring-2 focus:ring-indigo-500"
				readonly
				style="background-color: #f8f8f8; white-space: pre-wrap;"
			></textarea>
		</div>
	</div>

	<!-- Analyze Button -->
	<button
		on:click={analyzeText}
		class="mt-6 w-40 rounded-full bg-gray-800 px-4 py-2 text-white shadow-md transition duration-300 ease-in-out hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-500"
	>
		Analyze
	</button>
</div>

<style>
	textarea {
		font-family: 'Arial', sans-serif;
		background-color: #ffffff;
	}

	/* Responsive design */
	@media (max-width: 768px) {
		.flex-col {
			width: 100%;
		}
	}
</style>
