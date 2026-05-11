"""Example of using the Responses API to request a structured JSON response.

Setting text.format to 'json_object' instructs the model to return its answer
as valid JSON, which is useful for downstream parsing.
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

# Send the request with JSON output mode enabled.
# text={'format': {'type': 'json_object'}} guarantees the response is valid JSON.
response = client.responses.create(
    model=os.environ['MODEL'],
    instructions=(
        "You are a helpful assistant. Always say GO BLUE! at the end of your response. "
        "Respond in json format."
    ),
    input="Explain step by step. Where is the University of Michigan? Respond in JSON format.",
    text={"format": {"type": "json_object"}},
)

# Print the JSON string returned by the model.
print(response.output_text)
