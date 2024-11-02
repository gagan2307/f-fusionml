// server.js

import { json } from '@sveltejs/kit';
import { spawn } from 'child_process';
import { once } from 'events';
import path from 'path';
import fs from 'fs';
import os from 'os';
import { v4 as uuidv4 } from 'uuid';

export async function POST({ request }) {
    try {
        const formData = await request.formData();
        const imageFile = formData.get('file'); // Changed 'image' to 'file' to match client-side

        if (!imageFile) {
            return new Response('No image file provided.', { status: 400 });
        }

        // Create a temporary file to save the uploaded image
        const tempDir = os.tmpdir();
        const tempImagePath = path.join(tempDir, `upload_${uuidv4()}_${imageFile.name}`);

        // Save the image file to the temporary path
        const imageBuffer = Buffer.from(await imageFile.arrayBuffer());
        fs.writeFileSync(tempImagePath, imageBuffer);

        const scriptPath = path.resolve('src/python/dl/image-sentiment-analyzer/Image_sentiment_analyzer.py');
        const modelDir = path.resolve('src/python/dl/image-sentiment-analyzer/local_image_analyzer_model'); // Ensure this path is correct

        // Spawn the Python process
        const pythonProcess = spawn('python', [scriptPath], {
            cwd: path.dirname(scriptPath), // Set current working directory to the script's directory
            stdio: ['pipe', 'pipe', 'pipe'],
            shell: true // Helps in locating the Python executable on Windows
        });

        let result = '';
        let error = '';

        // Write the image path to Python's stdin
        pythonProcess.stdin.write(tempImagePath);
        pythonProcess.stdin.end();

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

        // Delete the temporary image file after processing
        fs.unlinkSync(tempImagePath);

        if (code === 0) {
            return json({ sentiment: result.trim() });
        } else {
            console.error(`Python script exited with code ${code}`);
            return new Response(`Error: ${error || 'Unknown error'}`, { status: 500 });
        }
    } catch (error) {
        console.error('Error:', error);
        return new Response('Internal Server Error', { status: 500 });
    }
}
