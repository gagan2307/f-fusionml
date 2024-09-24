<script>
	// Importing Images
	import spamImg from '$lib/MLListPage/spam.svg';
	import textsumImg from '$lib/MLListPage/textsum.svg';
	import speechImg from '$lib/MLListPage/microphone.svg';
	import sentimentImg from '$lib/MLListPage/smile.svg';
	import textgenImg from '$lib/MLListPage/textgen.svg';

	import CustomGradiantButtonPink from '../../Components/CustomGradiantButtonPink/CustomGradiantButtonPink.svelte';

	const buttons = [
		{
			id: 1,
			title: 'Spam Detection',
			description: 'Check for Spam/Ham',
			img: spamImg
		},
		{
			id: 2,
			title: 'Text Summation',
			description: 'Summarizes a Given Text',
			img: textsumImg
		},
		{
			id: 3,
			title: 'Speech Transformation',
			description: 'STT and TTS',
			img: speechImg
		},
		{
			id: 4,
			title: 'Sentiment Analyser',
			description: 'Provides sentiment',
			img: sentimentImg
		},
		{
			id: 5,
			title: 'Text Generation',
			description: 'Generates an Abstract Text Paragraph',
			img: textgenImg
		}
	];
</script>

<div class="flex w-full flex-col justify-between px-10 lg:mt-20 lg:flex-row">
	<!-- Heading on the left -->
	<h1
		class="-mt-10 ml-4 text-5xl font-bold max-lg:mt-28 max-lg:text-5xl max-md:text-4xl max-sm:mb-16 max-sm:text-3xl lg:ml-10 lg:w-1/2 lg:text-left"
	>
		Machine Learning
	</h1>

	<!-- Buttons on the right -->
	<div class="mt-10 lg:mt-0 lg:flex lg:w-1/2 lg:justify-end">
		<div class="w-full lg:w-auto">
			<h3 class="-mt-10 mb-4 text-right text-lg font-semibold max-sm:text-lg">
				Select Application<br />
				<p class="ml-4 text-sm">Choose Any</p>
			</h3>

			<!-- Grid layout for buttons -->
			<div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-1">
				{#each buttons as button}
					<CustomGradiantButtonPink
						index={button.id}
						title={button.title}
						description={button.description}
						img={button.img}
					/>
				{/each}
			</div>
		</div>
	</div>
</div>
