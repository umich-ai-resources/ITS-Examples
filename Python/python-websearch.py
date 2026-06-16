"""Example of using the LLM Gateway with the web_search_preview tool.

The model can call the web search tool during a response to look up
current information. The result includes both the model's answer and
the sources it cited.
"""
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

os.chdir(os.path.dirname(os.path.abspath(__file__)))

if not load_dotenv(".env"):
    print("Unable to load .env file.", file=sys.stderr)
    sys.exit(1)

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
    base_url=os.environ['OPENAI_API_BASE'],
)

response = client.responses.create(
    model=os.environ['MODEL'],
    tools=[{"type": "web_search_preview"}],
    input="What was a positive news story from today?",
)

print(response.output_text)
