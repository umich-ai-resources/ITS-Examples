"""Example using the OpenAI Responses API — the preferred endpoint for the LLM Gateway.

The Responses API (client.responses.create) is the modern, recommended way to interact
with the LLM Gateway. It provides a simpler interface than Chat Completions.

Key differences from Chat Completions:
  - Use 'instructions' for the system prompt instead of a 'system' role message.
  - Use 'input' for the user prompt instead of a 'messages' list.
  - Access the reply with response.output_text instead of response.choices[0].message.content.
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

# Send a request using the Responses API.
# 'instructions' sets the system-level behavior and persona for the model.
# 'input' is the user's question or prompt.
response = client.responses.create(
    model=os.environ['MODEL'],
    instructions="You are a helpful assistant. Always say GO BLUE! at the end of your response.",
    input="Explain step by step. Where is the University of Michigan?",
)

# response.output_text is a convenience property that returns the first text output.
print(response.output_text)
