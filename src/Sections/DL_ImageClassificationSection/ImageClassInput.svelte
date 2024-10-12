<!-- ImageClassificationInput.svelte -->

<script>
    import axios from 'axios';
    import CustomModal from '../../Components/CustomModal/CustomModal.svelte';
    import { tick } from 'svelte';

    let selectedFile = null;
    let predictionResult = 'Result';
    let imageUrl = null; // Add a variable to store the image URL

    let showModal = false;
    let isLoading = false;

    async function analyzeImage() {
        if (!selectedFile) {
            alert('Please select an image file before analyzing.');
            return;
        }

        // Reset states
        isLoading = true;
        showModal = true;

        // Wait for DOM to update so the modal appears
        await tick();

        try {
            const formData = new FormData();
            formData.append('file', selectedFile);

            const response = await axios.post('/api/dl-image-classification', formData);

            if (response.status !== 200) {
                throw new Error('Network response was not ok');
            }

            predictionResult = response.data.prediction || 'No result received.';
        } catch (error) {
            console.error('Error:', error);
            predictionResult = 'Error analyzing image.';
        } finally {
            isLoading = false;

            // Automatically close the modal after a brief delay to show the result
            setTimeout(() => {
                showModal = false;
            }, 500); // Adjust the delay as needed
        }
    }

    function clearFile() {
        selectedFile = null;
        imageUrl = null; // Clear the image URL when the file is cleared
        predictionResult = 'Result';
    }

    function handleFileChange(event) {
        const file = event.target.files[0];
        if (file) {
            selectedFile = file;

            // Use FileReader to read the image and set the imageUrl
            const reader = new FileReader();
            reader.onload = function(e) {
                imageUrl = e.target.result;
            };
            reader.readAsDataURL(file);
        } else {
            selectedFile = null;
            imageUrl = null;
        }
    }
</script>

<div class="flex flex-col items-center justify-center gap-6 p-4">
    <div class="mb-4 text-center text-2xl font-bold">Upload Image for Classification</div>
    <div class="flex w-full max-w-6xl flex-col gap-8 md:flex-row">
        <!-- Upload Image Section -->
        <div class="flex w-full flex-col rounded-lg bg-white/80 p-6 shadow-lg md:w-2/3">
            <h2 class="mb-4 text-center text-2xl font-bold">Select Image</h2>
            <input type="file" accept="image/*" on:change={handleFileChange} />
            {#if imageUrl}
                <div class="mt-4 flex justify-center">
                    <img src="{imageUrl}" alt="Selected Image" class="max-w-full h-auto" />
                </div>
            {/if}
            <button
                on:click={clearFile}
                class="mt-2 self-end rounded-full bg-gray-200 p-2 transition duration-150 ease-in-out hover:bg-gray-300"
                title="Clear File"
            >
                🗑️
            </button>
        </div>

        <!-- Result Section -->
        <div class="flex w-full flex-col rounded-lg bg-white/80 p-6 shadow-lg md:w-1/3">
            <h2 class="mb-4 text-center text-2xl font-bold">Prediction Result</h2>
            <textarea
                bind:value={predictionResult}
                class="h-40 w-full resize-none overflow-auto rounded-md border border-gray-300 p-4 focus:outline-none focus:ring-2 focus:ring-indigo-500"
                readonly
                style="background-color: #f8f8f8; white-space: pre-wrap;"
            ></textarea>
        </div>
    </div>

    <!-- Analyze Button -->
    <button
        on:click={analyzeImage}
        class="mt-6 w-40 rounded-full bg-gray-800 px-4 py-2 text-white shadow-md transition duration-300 ease-in-out hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-500"
    >
        Analyze
    </button>
</div>

<!-- Modal -->
<CustomModal
    isOpen={showModal}
    {isLoading}
    title="Analyzing Image"
    additionalContent={isLoading ? 'Processing...' : ''}
    on:close={() => (showModal = false)}
/>

<style>
    /* Add any custom styles here */
    img {
        max-width: 100%;
        height: auto;
    }
</style>
