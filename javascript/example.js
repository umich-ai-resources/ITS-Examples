#!/usr/bin/env -S npm run tsn -T

import OpenAI from 'openai';

// API Base URL provided to you by ITS
const api_base = '';

// AI model you would like to use
const model = '';

//API Key Provided to you by ITS.
const api_key = ''

if (!api_key) {
  throw new Error('The OPENAI_API_KEY environment variable is missing or empty.');
}
if (!api_base) {
  throw new Error('The OPENAI_API_BASE environment variable is missing or empty.');
}
if (!model) {
  throw new Error('The OPENAI_API_MODEL environment variable is missing or empty.');
}

// OpenAI requires a key and base url
const openai = new OpenAI({
  apiKey: api_key,
  baseURL: api_base,
});

async function main() {
  const result = await openai.chat.completions.create({
    model,
    messages: [{ role: 'user', content: 'Say hello!' }],
  });
  console.log(JSON.stringify(result, null, "    "));
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});

//EOF
