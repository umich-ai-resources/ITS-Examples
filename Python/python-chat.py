"""Basic example of using the Chat Completions API with the LLM Gateway.

The Chat Completions API (client.chat.completions.create) is the traditional
OpenAI-compatible endpoint. Use a 'system' role message for instructions and
a 'user' role message for the prompt. Access the reply via
response.choices[0].message.content.

For new projects, consider the Responses API (see python-responses.py), which
provides a simpler interface with built-in multi-turn and tool-use support.
"""
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

# Set the current working directory to the same directory as this file.
# This ensures the .env file is found regardless of where the script is run from.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables (API key, base URL, model name) from the .env file.
if not load_dotenv(".env"):
    print("Unable to load .env file.", file=sys.stderr)
    sys.exit(1)

# Create the OpenAI client pointed at the LLM Gateway base URL.
client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
    base_url=os.environ['OPENAI_API_BASE'],
)

# Send a request using the Chat Completions API.
# 'system' sets the assistant behavior; 'user' is the human turn.
response = client.chat.completions.create(
    model=os.environ['MODEL'],
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. Always say GO BLUE! at the end of your response.",
        },
        {
            "role": "user",
            "content": "Explain step by step. Where is the University of Michigan?",
        },
    ],
)

# response.choices[0].message.content holds the assistant's reply.
print(response.choices[0].message.content)
