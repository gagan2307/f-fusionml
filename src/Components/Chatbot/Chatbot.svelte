<!-- src/lib/Chatbot.svelte -->
<script>
	let isOpen = false;

	function toggleChatbot() {
		isOpen = !isOpen;
	}
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div
	class="fixed bottom-5 right-5 z-50 flex h-12 w-12 cursor-pointer items-center justify-center rounded-full bg-blue-600 text-white shadow-lg"
	on:click={toggleChatbot}
>
	<i class="fas fa-comments text-xl"></i>
</div>

{#if isOpen}
	<div
		class="fixed bottom-20 right-5 z-50 h-[430px] w-[350px] overflow-hidden rounded bg-white shadow-xl"
	>
		<!-- svelte-ignore a11y-missing-attribute -->
		<iframe
			allow="microphone;"
			width="350"
			height="430"
			src="https://console.dialogflow.com/api-client/demo/embedded/93316f00-5458-4a77-9de1-5c8b0470902b"
		>
		</iframe>
	</div>
{/if}
