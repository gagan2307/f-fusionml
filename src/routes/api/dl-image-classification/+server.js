// +server.js

import { json } from '@sveltejs/kit';
import { spawn } from 'child_process';
import { writeFile, unlink } from 'fs/promises';
import path from 'path';
import { v4 as uuidv4 } from 'uuid';
import os from 'os';

export async function POST({ request }) {
    try {
        // Log the PATH environment variable
        // console.log('Node.js PATH:', process.env.PATH);

        const formData = await request.formData();
        const file = formData.get('file');

        if (!file || !file.size) {
            return new Response('No file uploaded', { status: 400 });
        }

        // Generate a unique filename
        const filename = `${uuidv4()}-${file.name}`;
        const tempDir = os.tmpdir();
        const filepath = path.join(tempDir, filename);

        // Read the file data and save it to a temporary file
        const fileBuffer = await file.arrayBuffer();
        await writeFile(filepath, Buffer.from(fileBuffer));

        const scriptPath = path.resolve('src/python/dl/image-classification/image_classifier.py');
        const modelDir = path.resolve('src/python/dl/image-classification');

        // Spawn the Python process
        const pythonProcess = spawn('python', [scriptPath, filepath], {
            cwd: modelDir,
            stdio: ['pipe', 'pipe', 'pipe']
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

        // Wait for the process to exit
        const code = await new Promise((resolve, reject) => {
            pythonProcess.on('close', resolve);
            pythonProcess.on('error', reject);
        });

        // Clean up the uploaded file
        await unlink(filepath);

        if (code === 0) {
            return json({ prediction: result.trim() });
        } else {
            console.error(`Python script exited with code ${code}`);
            console.error(`Error: ${error}`);
            return new Response(`Internal Server Error: ${error}`, { status: 500 });
        }

    } catch (error) {
        console.error('Error:', error);
        return new Response('Internal Server Error', { status: 500 });
    }
}
