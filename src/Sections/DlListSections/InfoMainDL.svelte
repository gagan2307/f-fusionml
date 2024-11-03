<script>
	import { fade } from 'svelte/transition';
	import { cubicOut } from 'svelte/easing';
	import imageToTextImg from '$lib/DLListPage/imageToText.svg';
	import movieGenreImg from '$lib/DLListPage/movie.svg';
	import imageClassificationImg from '$lib/DLListPage/imageClassification.svg';
	import musicGenreImg from '$lib/DLListPage/music.svg';
	import imageSentimentImg from '$lib/DLListPage/sentimentImage.svg';
	import CustomGradiantButtonPink from '../../Components/CustomGradiantButtonPink/CustomGradiantButtonPink.svelte';

	const buttons = [
		{
			id: 1,
			title: 'Image to Text',
			description: 'Convert images into text descriptions',
			img: imageToTextImg,
			summary:
				'Image to text conversion utilizes deep learning models such as Convolutional Neural Networks (CNNs) and Recurrent Neural Networks (RNNs) to interpret images and generate descriptive text captions. This technology is essential for applications like automatic image captioning and aiding visually impaired users.',
			link: '/dl/image-to-text'
		},
		// {
		// 	id: 5,
		// 	title: 'Movie Genre Prediction',
		// 	description: 'Predict genres from movie plots',
		// 	img: movieGenreImg,
		// 	summary:
		// 		'Movie genre prediction uses deep learning to analyze movie plots or scripts and predict the genres they belong to. Models like LSTMs and Transformers capture semantic meanings in text to make accurate genre classifications, enhancing recommendation systems and content analysis.',
		// 	link: '/dl/movie-genere'
		// },
		{
			id: 2,
			title: 'Image Classification',
			description: 'Classify images into categories',
			img: imageClassificationImg,
			summary:
				'Image classification involves training deep learning models, primarily Convolutional Neural Networks (CNNs), to categorize images into predefined classes. This is fundamental in computer vision tasks such as object recognition, autonomous driving, and medical image analysis.',
			link: '/dl/image-classification'
		},
		// {
		// 	id: 4,
		// 	title: 'Music Genre Prediction',
		// 	description: 'Predict genres from audio files',
		// 	img: musicGenreImg,
		// 	summary:
		// 		'Music genre prediction employs deep learning to analyze audio features and classify music into genres. Techniques include spectrogram analysis and models like CNNs and RNNs to process temporal audio data, aiding in music recommendation systems and audio content analysis.',
		// 	link: '/dl/music-genere'
		// },
		{
			id: 3,
			title: 'Sentiment Analysis from Image',
			description: 'Detect sentiment from images',
			img: imageSentimentImg,
			summary:
				'Sentiment analysis from images uses deep learning to interpret the emotional content conveyed through visuals. Models analyze facial expressions, body language, and visual context to determine sentiments or emotions, aiding in applications like mood detection and user experience analysis.',
			link: '/dl/image-sentiment-analysis'
		}
	];

	let currentTitle = 'Image to Text';

	let currentSummary =
		'Image to text conversion utilizes deep learning models such as Convolutional Neural Networks (CNNs) and Recurrent Neural Networks (RNNs) to interpret images and generate descriptive text captions. This technology is essential for applications like automatic image captioning and aiding visually impaired users.';

	function handleHover(event) {
		const { index } = event.detail;
		currentSummary =
			buttons.find((button) => button.id === index)?.summary || 'No details available.';
		currentTitle = buttons.find((button) => button.id === index)?.title || 'No details available.';
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
			Deep Learning
		</h1>

		<!-- Summary Section -->
		<div
			class="mt-8 h-[59vh] max-h-[80vh] w-full max-w-full rounded-2xl bg-opacity-80 bg-gradient-to-r from-purple-500 to-pink-500 p-6 shadow-lg max-lg:h-auto max-md:p-4 max-sm:mx-auto max-sm:h-auto max-sm:w-[90%] max-xs:mx-auto max-xs:h-auto max-xs:w-[95%] lg:ml-10 lg:mt-10"
		>
			<h2 class="mb-4 text-2xl font-bold text-white max-xl:text-xl max-sm:text-lg">
				{currentTitle}
			</h2>
			<p
				class="max-xl:text-md fade-transform justify-center text-lg text-white max-sm:text-sm"
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
			<!-- <h3
				class="mb-4 mt-10 text-right text-lg font-semibold max-lg:mb-8 max-lg:mt-8 max-lg:text-center max-sm:text-lg"
			>
				Select Application<br />
				<p class="ml-4 text-sm">Choose Any</p>
			</h3> -->

			<!-- Grid layout for buttons -->
			<div
				class="mt-[100px] grid grid-cols-1 gap-6 max-lg:mb-[25px] max-lg:mt-[50px] md:grid-cols-2 lg:grid-cols-1"
			>
				{#each buttons as button}
					<CustomGradiantButtonPink
						index={button.id}
						title={button.title}
						description={button.description}
						img={button.img}
						source={button.link}
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
