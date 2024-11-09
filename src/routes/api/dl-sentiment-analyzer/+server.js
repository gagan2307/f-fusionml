import { json } from '@sveltejs/kit';
import { spawn } from 'child_process';
import { once } from 'events';
import path from 'path';
import fs from 'fs';
import os from 'os';

export async function POST({ request }) {
	try {
		const formData = await request.formData();
		const imageFile = formData.get('image');

		if (!imageFile) {
			return new Response('No image file provided.', { status: 400 });
		}

		// Create a temporary file to save the uploaded image
		const tempDir = os.tmpdir();
		const tempImagePath = path.join(tempDir, `upload_${Date.now()}.jpg`);

		try {
			// Save the image file to the temporary path
			const imageBuffer = Buffer.from(await imageFile.arrayBuffer());
			fs.writeFileSync(tempImagePath, imageBuffer);

			const scriptPath = path.resolve(
				'src/python/dl/image-sentiment-analyzer/image_sentiment_analyzer.py'
			);

			// Spawn the Python process with the image path as an argument
			const pythonProcess = spawn('python', [scriptPath, tempImagePath], {
				cwd: path.dirname(scriptPath),
				stdio: ['ignore', 'pipe', 'pipe']
			});

			let result = '';
			let error = '';

			// Collect data from stdout
			pythonProcess.stdout.on('data', (data) => {
				result += data.toString();
			});

			// Collect errors from stderr
			pythonProcess.stderr.on('data', (data) => {
				error += data.toString();
				console.error(`Python stderr: ${data.toString()}`);
			});

			// Await the 'close' event
			const [code] = await once(pythonProcess, 'close');

			if (code === 0) {
				let sentiments;
				try {
					sentiments = JSON.parse(result);
				} catch (err) {
					console.error('Error parsing JSON:', err);
					return new Response('Error parsing JSON output.', { status: 500 });
				}
				return json({ sentiments });
			} else {
				console.error(`Python script exited with code ${code}`);
				return new Response(`Error: ${error || 'Unknown error'}`, { status: 500 });
			}
		} finally {
			// Ensure the temporary image file is deleted
			if (fs.existsSync(tempImagePath)) {
				fs.unlinkSync(tempImagePath);
			}
		}
	} catch (error) {
		console.error('Error:', error);
		return new Response('Internal Server Error', { status: 500 });
	}
}
