#!/bin/bash
export API_KEY=""
export API_BASE=""
export DEPLOYMENT_ID="" #model name

curl $API_BASE"/openai/deployments/"$DEPLOYMENT_ID"/chat/completions?api-version="$API_VERSION \
  -H "Content-Type: application/json" \
  -H "OpenAI-Organization: $ORGANIZATION" \
  -H "api-key: $API_KEY" \
  -d '{
  "model": "gpt-4.1",
  "messages": [{"role":"system","content":"You are a helpful bot"},{"role":"user","content":"What is 2+2"}],
  "temperature": 0,
  "frequency_penalty":0,
  "top_p":0.95
}'
