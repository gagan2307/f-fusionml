// +server.js

import { json } from '@sveltejs/kit';
import { spawn } from 'child_process';
import { once } from 'events';
import path from 'path';

export async function POST({ request }) {
    try {
        const data = await request.json();
        const inputText = data.inputText;

        const scriptPath = path.resolve('src/python/ml/sentiment-analyzer/sentiment_analyzer.py');
        const modelDir = path.resolve('src/python/ml/sentiment-analyzer');

        // Spawn the Python process
        const pythonProcess = spawn('python', [scriptPath], {
            cwd: modelDir,
            stdio: ['pipe', 'pipe', 'pipe']
        });

        // Write the inputText to the Python process's stdin
        pythonProcess.stdin.write(inputText);
        pythonProcess.stdin.end();

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
            return json({ result: result.trim() });
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
