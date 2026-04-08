#!/usr/bin/env node
/**
 * Free OpenAI-Starter Node.js Demo
 *
 * This script demonstrates how to call an OpenAI-compatible API
 * using the official OpenAI JavaScript client.
 */

require('dotenv').config();

const API_KEY = process.env.API_KEY || '';
const BASE_URL = process.env.BASE_URL || 'https://www.tken.shop/v1';
const MODEL = process.env.MODEL || 'gpt-4o-mini';

function checkConfig() {
    if (!API_KEY) {
        console.error('Error: API_KEY is not set');
        console.error('Set it with: export API_KEY=your_api_key');
        console.error('Or create a .env file based on .env.example');
        process.exit(1);
    }
}

async function main() {
    checkConfig();

    const { OpenAI } = require('openai');

    const client = new OpenAI({
        apiKey: API_KEY,
        baseURL: BASE_URL
    });

    console.log(`API: ${BASE_URL}`);
    console.log(`Model: ${MODEL}`);
    console.log('-'.repeat(40));

    try {
        const response = await client.chat.completions.create({
            model: MODEL,
            messages: [
                { role: 'user', content: 'Say hello in one sentence.' }
            ],
            max_tokens: 50,
            temperature: 0.7
        });

        console.log('Success!');
        console.log('-'.repeat(40));
        console.log(`Response: ${response.choices[0].message.content}`);
        console.log(`Tokens: ${response.usage.total_tokens}`);

    } catch (error) {
        console.error(`Error: ${error.message}`);
        process.exit(1);
    }
}

main();
