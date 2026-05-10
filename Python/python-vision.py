"""Example of using the Responses API to analyze images with the LLM Gateway.

Two approaches are demonstrated:
  1. Image URL  — pass a publicly accessible URL directly in the request.
  2. Local file — base64-encode the file and embed it as a data URI.

The URL example runs automatically. To also run the local file example,
set image_path to the path of a file on your machine.
"""
import base64
import os

from dotenv import load_dotenv
from openai import OpenAI

# Set the current working directory to the same directory as this file.
# This ensures the .env file is found regardless of where the script is run from.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables (API key, base URL, model name) from the .env file.
try:
    if load_dotenv('.env') is False:
        raise TypeError
except TypeError:
    print('Unable to load .env file.')
    quit()

# Create the OpenAI client pointed at the LLM Gateway base URL.
client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
    base_url=os.environ['OPENAI_API_BASE'],
)

# ---------------------------------------------------------------------------
# Approach 1: Image URL
# Pass a public URL directly — no local file or encoding needed.
# ---------------------------------------------------------------------------

response = client.responses.create(
    model=os.environ['MODEL'],
    instructions="You are a helpful assistant that responds in Markdown! Help the user by describing the picture.",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "What is this picture of?"},
                {
                    "type": "input_image",
                    "image_url": "https://michiganross.umich.edu/sites/default/files/styles/max_1300x1300/public/images/news-story/butterfly.jpeg",
                },
            ],
        }
    ],
)

print("--- Image URL result ---")
print(response.output_text)

# ---------------------------------------------------------------------------
# Approach 2: Local file
# Read the file, base64-encode it, and embed it as a data URI so no public
# URL is needed — the image bytes travel with the request.
# ---------------------------------------------------------------------------

image_path = ''  # e.g. '/path/to/image.jpg' — leave empty to skip this example

if not image_path:
    print("\n--- Local file example skipped (set image_path to run it) ---")
else:
    with open(image_path, 'rb') as image_file:
        imagedata = base64.b64encode(image_file.read()).decode('ascii')

    response = client.responses.create(
        model=os.environ['MODEL'],
        instructions="As an AI tool specialized in image recognition, you will be given an image and asked to answer a question about it.",
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": "How many green dots are there?"},
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{imagedata}",
                    },
                ],
            }
        ],
    )

    print("\n--- Local file result ---")
    print(response.output_text)
