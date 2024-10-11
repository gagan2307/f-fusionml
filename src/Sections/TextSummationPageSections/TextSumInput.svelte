<script>
	import axios from 'axios';
	import CustomModal from '../../Components/CustomModal/CustomModal.svelte';
	import { tick } from 'svelte'; // Import tick from 'svelte'

	let inputText = '';
	let showModal = false;
	let isLoading = false;
	let predictionResult = '';

	async function handlePrediction() {
		if (inputText.trim() === '') {
			alert('Please enter text before making a prediction.');
			return;
		}
		// Reset states
		isLoading = true;
		showModal = true; // Show the modal immediately
		predictionResult = '';

		// Wait for DOM to update
		await tick();

		try {
			const response = await axios.post('/api/text-summation', { inputText });

			if (response.status !== 200) {
				throw new Error('Network response was not ok');
			}

			predictionResult = response.data.result;
		} catch (error) {
			console.error('Error:', error);
			predictionResult = 'Error occurred during prediction.';
		} finally {
			isLoading = false;
			// The modal remains open, and the content is updated
		}
	}
</script>

<div class="flex flex-col items-center justify-center gap-8 p-6 lg:flex-row">
	<!-- Enter Text Section -->
	<div class="flex w-full flex-col rounded-lg bg-white/70 p-6 shadow-md lg:w-1/2">
		<h2 class="mb-4 text-center text-2xl font-bold">Enter Text</h2>
		<textarea
			placeholder="Enter text here"
			bind:value={inputText}
			class="h-40 w-full resize-none overflow-auto rounded-md border border-gray-300 p-4 focus:outline-none focus:ring-2 focus:ring-indigo-400"
			style="scrollbar-gutter: stable"
		></textarea>
	</div>

	<!-- Summary Section -->
	<div class="flex w-full flex-col rounded-lg bg-white/70 p-6 shadow-md lg:w-1/2">
		<h2 class="mb-4 text-center text-2xl font-bold">Summary</h2>
		<textarea
			placeholder="Summary here"
			bind:value={predictionResult}
			class="h-40 w-full resize-none overflow-auto rounded-md border border-gray-300 p-4 focus:outline-none focus:ring-2 focus:ring-indigo-400"
			style="scrollbar-gutter: stable"
			readonly
		></textarea>
	</div>
</div>

<div class="flex justify-center">
	<button
		on:click={handlePrediction}
		class="mb-[20px] mt-6 w-1/2 max-w-xs justify-center rounded-full bg-purple-500 py-3 text-white shadow-md transition duration-300 ease-in-out hover:bg-purple-600 focus:outline-none focus:ring-2 focus:ring-purple-300"
	>
		Prediction
	</button>
</div>

<style>
	textarea {
		background-color: #f8f8f8;
		font-family: 'Arial', sans-serif;
	}
</style>
