<script>
	import axios from 'axios';
	import CustomModal from '../../Components/CustomModal/CustomModal.svelte';
	import { tick } from 'svelte';

	let inputText = '';
	let resultText = 'Result';

	let showModal = false;
	let isLoading = false;

	async function analyzeText() {
		if (inputText.trim() === '') {
			alert('Please enter some text before analyzing.');
			return;
		}

		// Reset states
		isLoading = true;
		showModal = true;

		// Wait for DOM to update so the modal appears
		await tick();

		try {
			const response = await axios.post('/api/sentiment-analyzer', { inputText });

			if (response.status !== 200) {
				throw new Error('Network response was not ok');
			}

			resultText = response.data.result || 'No result received.';
		} catch (error) {
			console.error('Error:', error);
			resultText = 'Error analyzing text.';
		} finally {
			isLoading = false;

			// Automatically close the modal after a brief delay to show the result
			setTimeout(() => {
				showModal = false;
			}, 500); // Adjust the delay as needed
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

<!-- Modal -->
<CustomModal
	isOpen={showModal}
	{isLoading}
	title="Analyzing Sentiment"
	additionalContent={isLoading ? 'Processing...' : ''}
	on:close={() => (showModal = false)}
/>

<style>
	textarea {
		font-family: 'Arial', sans-serif;
		background-color: #ffffff;
	}

	/* Loader styles (optional, if you have a loader in your CustomModal) */
	/* Add any custom styles here */

	/* Responsive design */
	@media (max-width: 768px) {
		.flex-col {
			width: 100%;
		}
	}
</style>
