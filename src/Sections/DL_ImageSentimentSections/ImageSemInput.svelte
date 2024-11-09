<script>
	import { onMount, onDestroy } from 'svelte';
	import axios from 'axios';

	let videoElement;
	let canvasElement;
	let overlayCanvas;
	let isCameraActive = false;
	let sentimentResult = 'Sentiment will appear here.';
	let intervalId;

	async function startCamera() {
		try {
			const stream = await navigator.mediaDevices.getUserMedia({ video: true });
			videoElement.srcObject = stream;
			isCameraActive = true;

			// Start capturing frames every second
			intervalId = setInterval(captureFrame, 1000);
		} catch (error) {
			console.error('Error accessing the camera:', error);
			alert('Could not access the camera.');
		}
	}

	function stopCamera() {
		if (videoElement && videoElement.srcObject) {
			videoElement.srcObject.getTracks().forEach((track) => track.stop());
		}
		isCameraActive = false;
		clearInterval(intervalId);
		sentimentResult = 'Sentiment will appear here.';
		if (overlayCanvas) {
			const ctx = overlayCanvas.getContext('2d');
			ctx.clearRect(0, 0, overlayCanvas.width, overlayCanvas.height);
		}
	}

	async function captureFrame() {
		if (!videoElement || !canvasElement || !overlayCanvas) return;

		// Set canvas size to video size
		canvasElement.width = videoElement.videoWidth;
		canvasElement.height = videoElement.videoHeight;

		overlayCanvas.width = videoElement.videoWidth;
		overlayCanvas.height = videoElement.videoHeight;

		const context = canvasElement.getContext('2d');
		context.drawImage(videoElement, 0, 0, canvasElement.width, canvasElement.height);

		// Convert canvas to blob
		canvasElement.toBlob(
			async function (blob) {
				if (blob) {
					try {
						const formData = new FormData();
						formData.append('image', blob, 'frame.jpg');

						const response = await axios.post('/api/dl-sentiment-analyzer', formData, {
							headers: {
								'Content-Type': 'multipart/form-data'
							}
						});

						if (response.status !== 200) {
							throw new Error('Network response was not ok');
						}

						const data = response.data;
						if (data.sentiments && data.sentiments.length > 0) {
							// Clear the overlay canvas
							const overlayCtx = overlayCanvas.getContext('2d');
							overlayCtx.clearRect(0, 0, overlayCanvas.width, overlayCanvas.height);

							data.sentiments.forEach((item) => {
								const { emotion, box } = item;
								const [x, y, w, h] = box;

								// Adjust coordinates if video is mirrored
								const adjustedX = overlayCanvas.width - x - w;

								// Draw rectangle
								overlayCtx.strokeStyle = 'green';
								overlayCtx.lineWidth = 2;
								overlayCtx.strokeRect(adjustedX, y, w, h);

								// Draw emotion label
								overlayCtx.font = '16px Arial';
								overlayCtx.fillStyle = 'red';
								overlayCtx.fillText(emotion, adjustedX, y - 10);
							});

							sentimentResult = data.sentiments.map((item) => item.emotion).join(', ');
						} else {
							sentimentResult = 'No faces detected.';
							const overlayCtx = overlayCanvas.getContext('2d');
							overlayCtx.clearRect(0, 0, overlayCanvas.width, overlayCanvas.height);
						}
					} catch (error) {
						console.error('Error:', error);
						sentimentResult = 'Error analyzing image.';
					}
				}
			},
			'image/jpeg',
			0.8
		); // Adjust quality if needed
	}

	onDestroy(() => {
		stopCamera();
	});
</script>

<div class="flex flex-col items-center justify-center gap-6 p-4">
	<div class="mb-4 text-center text-2xl font-bold">Webcam Sentiment Analysis</div>

	<!-- Video and Canvas Elements -->
	<div class="relative">
		<video bind:this={videoElement} autoplay playsinline style="transform: scaleX(-1);"></video>
		<canvas bind:this={overlayCanvas} class="overlay-canvas"></canvas>
		<canvas bind:this={canvasElement} style="display: none;"></canvas>
	</div>

	<!-- Sentiment Result -->
	<div class="mt-4">
		<h2 class="mb-2 text-center text-2xl font-bold">Sentiment Result</h2>
		<div class="text-center text-xl">{sentimentResult}</div>
	</div>

	<!-- Start/Stop Buttons -->
	{#if !isCameraActive}
		<button
			on:click={startCamera}
			class="mt-6 w-40 rounded-full bg-gray-800 px-4 py-2 text-white shadow-md transition duration-300 ease-in-out hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-500"
		>
			Start Camera
		</button>
	{:else}
		<button
			on:click={stopCamera}
			class="mt-6 w-40 rounded-full bg-gray-800 px-4 py-2 text-white shadow-md transition duration-300 ease-in-out hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-500"
		>
			Stop Camera
		</button>
	{/if}
</div>

<style>
	.relative {
		position: relative;
		width: 640px;
		height: 480px;
	}
	video {
		width: 100%;
		height: 100%;
		background-color: black;
		position: absolute;
		top: 0;
		left: 0;
	}
	.overlay-canvas {
		position: absolute;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		pointer-events: none;
	}
</style>
