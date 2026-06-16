"""Example of using the Responses API to analyze a document (PDF) with the LLM Gateway.

Two approaches are demonstrated:
  1. File URL     — pass a publicly accessible PDF URL directly in the request.
  2. Local file   — encode a local PDF as base64 and pass it inline in the request.

The URL example runs automatically. To also run the local file example,
set pdf_path to the path of a PDF on your machine.
"""
import base64
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

# ---------------------------------------------------------------------------
# Approach 1: File URL
# Pass a public PDF URL directly — no local file or upload needed.
# ---------------------------------------------------------------------------

response = client.responses.create(
    model=os.environ['MODEL'],
    instructions="You are a helpful assistant that responds in Markdown.",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Summarize the key points of this document."},
                {
                    "type": "input_file",
                    "file_url": "https://facultyhandbook.provost.umich.edu/wp-content/uploads/handbook/handbook.pdf",
                },
            ],
        }
    ],
)

print("--- File URL result ---")
print(response.output_text)

# ---------------------------------------------------------------------------
# Approach 2: Local file (base64)
# Read a local PDF, encode it as base64, and pass it inline in the request.
# This avoids needing a public URL and does not require Files API support.
# ---------------------------------------------------------------------------

pdf_path = ''  # e.g. '/path/to/document.pdf' — leave empty to skip this example

if not pdf_path:
    print("\n--- Local file example skipped (set pdf_path to run it) ---")
else:
    with open(pdf_path, 'rb') as pdf_file:
        pdf_data = base64.b64encode(pdf_file.read()).decode('utf-8')

    filename = os.path.basename(pdf_path)

    response = client.responses.create(
        model=os.environ['MODEL'],
        instructions="You are a helpful assistant that responds in Markdown.",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_file",
                        "filename": filename,
                        "file_data": f"data:application/pdf;base64,{pdf_data}",
                    },
                    {"type": "input_text", "text": "Summarize the key points of this document."},
                ],
            }
        ],
    )

    print("\n--- Local file result ---")
    print(response.output_text)
