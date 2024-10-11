<!-- src/Components/CustomModal/CustomModal.svelte -->
<script>
	import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();

	export let isOpen = false;
	export let isLoading = false;
	export let title = '';
	export let content = '';
	export let additionalContent = '';
	export let showCloseButton = true;

	function closeModal() {
		dispatch('close');
	}
</script>

{#if isOpen}
	<div class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
		<div class="relative w-full max-w-md rounded-lg bg-white p-6 shadow-lg">
			{#if showCloseButton}
				<button
					type="button"
					class="absolute right-3 top-3 text-gray-500 hover:text-gray-700 focus:outline-none"
					on:click={closeModal}
				>
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
			{/if}

			<div class="text-center">
				{#if isLoading}
					<!-- Spinner -->
					<svg
						class="mx-auto h-10 w-10 animate-spin text-gray-500"
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
					>
						<circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"
						></circle>
						<path
							class="opacity-75"
							fill="currentColor"
							d="M4 12a8 8 0 018-8V0l3.2 3.2-3.2 3.2V4a8 8 0 00-8 8z"
						></path>
					</svg>
					<p class="mt-4">Processing...</p>
				{:else}
					{#if title}
						<h2 class="mb-4 text-lg font-bold">{title}</h2>
					{/if}
					{#if content}
						<p class="mb-2">{content}</p>
					{/if}
					{#if additionalContent}
						<p>{additionalContent}</p>
					{/if}
					<button
						class="mt-4 inline-flex items-center rounded-md bg-purple-500 px-4 py-2 text-sm font-medium text-white hover:bg-purple-600 focus:outline-none focus:ring-2 focus:ring-purple-500"
						on:click={closeModal}
					>
						Close
					</button>
				{/if}
			</div>
		</div>
	</div>
{/if}

<style>
	/* Your modal styles here */
</style>
