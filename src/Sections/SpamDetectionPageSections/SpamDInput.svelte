<!-- src/Sections/SpamDetectionPageSections/SpamDInput.svelte -->
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
			const response = await axios.post('/api/spam-detection', { inputText });

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

	function clearInput() {
		inputText = '';
	}
</script>

<div class="mt-10 flex w-full flex-col items-center justify-center px-4">
	<!-- Input Container -->
	<div class="w-full max-w-3xl rounded-lg bg-white bg-opacity-80 p-6 shadow-md">
		<label for="spam-input" class="mb-4 block text-center text-2xl font-bold text-black">
			Enter Text
		</label>
		<div class="relative">
			<textarea
				id="spam-input"
				bind:value={inputText}
				class="h-[200px] w-full rounded-lg border border-gray-300 p-4 focus:outline-none focus:ring-2 focus:ring-purple-500 max-sm:text-base"
				rows="4"
				placeholder="Enter Text"
			></textarea>
			<button
				type="button"
				class="absolute right-2 top-2 text-gray-500 hover:text-gray-700 focus:outline-none"
				on:click={clearInput}
			>
				<!-- Trash icon for clearing input -->
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
					class="h-6 w-6"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M6 18L18 6M6 6l12 12"
					/>
				</svg>
			</button>
		</div>
	</div>

	<!-- Prediction Button -->
	<button
		on:click={handlePrediction}
		class="mt-6 w-1/2 max-w-xs rounded-full bg-purple-500 py-3 text-white shadow-md transition duration-300 ease-in-out hover:bg-purple-600 focus:outline-none focus:ring-2 focus:ring-purple-300"
	>
		Prediction
	</button>

	<!-- Modal -->
	<CustomModal
		isOpen={showModal}
		{isLoading}
		title="Prediction Result"
		content={`Input Text: ${inputText}`}
		additionalContent={`Prediction: ${predictionResult}`}
		on:close={() => (showModal = false)}
	/>
</div>

<style>
	/* Additional custom styles if needed */
</style>
