<script>
	import { fade } from 'svelte/transition';
	import { cubicOut } from 'svelte/easing';
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
			img: spamImg,
			summary:
				'Spam detection in machine learning involves training models to identify and filter out unwanted or malicious emails. Techniques such as Naive Bayes, support vector machines (SVM), and deep learning algorithms are commonly used.'
		},
		{
			id: 2,
			title: 'Text Summation',
			description: 'Summarizes a Given Text',
			img: textsumImg,
			summary:
				'Text summation in machine learning, also known as text summarization, involves condensing large amounts of text into a shorter version while preserving key information.'
		},
		{
			id: 3,
			title: 'Speech Transformation',
			description: 'STT and TTS',
			img: speechImg,
			summary:
				'Speech recognition in machine learning involves converting spoken language into text using algorithms like deep learning, acoustic models, and feature extraction. It enhances applications like virtual assistants and real-time transcription.'
		},
		{
			id: 4,
			title: 'Sentiment Analyser',
			description: 'Provides sentiment',
			img: sentimentImg,
			summary:
				'Sentiment analysis in machine learning classifies emotions in text, identifying positive, negative, or neutral sentiments. It uses natural language processing, text mining, and deep learning to interpret opinions and emotions accurately.'
		},
		{
			id: 5,
			title: 'Text Generation',
			description: 'Generates an Abstract Text Paragraph',
			img: textgenImg,
			summary:
				'Text generation is a task in natural language processing (NLP) where a model generates coherent and contextually relevant text based on a given input prompt. It utilizes deep learning models, such as GPT (Generative Pre-trained Transformer), to predict and construct sentences. These models are trained on vast datasets, enabling them to produce human-like and creative text for applications like chatbots, story writing, and summarization.'
		}
	];

	let currentSummary =
		'Spam detection in machine learning involves training models to identify and filter out unwanted or malicious emails. Techniques such as Naive Bayes, support vector machines (SVM), and deep learning algorithms are commonly used.';

	function handleHover(event) {
		const { index } = event.detail;
		currentSummary =
			buttons.find((button) => button.id === index)?.summary || 'No details available.';
	}

	function handleLeave() {
		currentSummary = 'Hover over any button to see more details.';
	}
</script>

<div class="flex w-full flex-col justify-between px-10 lg:flex-row">
	<!-- Left Column: Machine Learning Heading and Summary -->
	<div class="lg:w-1/2">
		<!-- Heading -->
		<h1
			class="-mt-28 ml-4 text-5xl font-bold max-lg:mt-28 max-lg:text-center max-lg:text-5xl max-md:text-4xl max-sm:mb-16 max-sm:text-3xl max-2xs:text-2xl lg:ml-10 lg:mt-20 lg:text-left"
		>
			Machine Learning
		</h1>

		<!-- Summary Section -->
		<div
			class="mt-8 h-[59vh] max-h-[80vh] w-full max-w-full rounded-2xl bg-opacity-80 bg-gradient-to-r from-purple-500 to-pink-500 p-6 shadow-lg max-lg:h-auto max-md:p-4 max-sm:mx-auto max-sm:h-auto max-sm:w-[90%] max-xs:mx-auto max-xs:h-auto max-xs:w-[95%] lg:ml-10 lg:mt-10"
		>
			<h2 class="mb-4 text-2xl font-bold text-white max-xl:text-xl max-sm:text-lg">Summary</h2>
			<p
				class="max-xl:text-md fade-transform text-lg text-white max-sm:text-sm"
				transition:fade={{ duration: 300 }}
				on:mouseenter={() => event.target.classList.add('fade-transform-active')}
				on:mouseleave={() => event.target.classList.remove('fade-transform-active')}
			>
				{currentSummary}
			</p>
		</div>
	</div>

	<!-- Right Column: Buttons -->
	<div class="mt-10 lg:mt-0 lg:flex lg:w-1/2 lg:justify-end">
		<div class="w-full lg:w-auto">
			<h3
				class="mb-4 mt-10 text-right text-lg font-semibold max-lg:mb-8 max-lg:mt-8 max-lg:text-center max-sm:text-lg"
			>
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
						on:hover={handleHover}
						on:leave={handleLeave}
					/>
				{/each}
			</div>
		</div>
	</div>
</div>

<style>
	.fade-transform {
		transform: translateY(10px);
		transition: transform 0.3s cubic-bezier(0.23, 1, 0.32, 1);
	}
	.fade-transform-active {
		transform: translateY(0);
	}
</style>
