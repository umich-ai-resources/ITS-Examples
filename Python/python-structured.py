"""Example of structured outputs using the Responses API with JSON Schema enforcement.

Structured outputs make the model follow a strict JSON Schema so the response
can be parsed directly into a typed Python object — no manual JSON wrangling needed.
The Pydantic model defines the schema; model_validate_json() validates the result.
"""
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

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


# Define the expected output shape as a Pydantic model.
# Each field is a list of strings representing Named Entities of that type.
class Extract(BaseModel):
    University: list[str]
    Facility: list[str]
    City: list[str]
    State: list[str]
    Event: list[str]
    Work_of_art: list[str]
    Date: list[str]
    Quantity: list[str]
    Mascot: list[str]


# Sample text containing various named entities to be extracted.
text = (
    "I am a student at the University of Michigan in Ann Arbor, MI. "
    "I like to go to football games at Michigan's football stadium, The Big House. "
    "The Big House's seating capacity is 107,601 people. "
    "The first game of the 2024 football season is on August 31st. "
    "U of M's fight song is called The Victors. "
    "The Ann Arbor campus is divided into four main areas: North campus, Central campus, "
    "Medical campus, and South campus, for a combined area of more than 37.48 million square feet. "
    "UMich's mascot is the wolverine."
)

# Build the schema from the Pydantic model and add additionalProperties: false,
# which is required by some providers (e.g. Azure OpenAI) for strict mode.
schema = Extract.model_json_schema()
schema["additionalProperties"] = False

# Send the request with a JSON Schema derived from the Pydantic model.
# strict=True ensures the model follows the schema exactly with no extra fields.
response = client.responses.create(
    model=os.environ['MODEL'],
    instructions=(
        "You are an expert in Natural Language Processing. Your task is to identify common "
        "Named Entities (NER) in a given text and return them in the specified JSON format."
    ),
    input=text,
    text={
        "format": {
            "type": "json_schema",
            "name": "Extract",
            "schema": schema,
            "strict": True,
        }
    },
)

# Validate the JSON response against the Pydantic model and print formatted output.
result = Extract.model_validate_json(response.output_text)
print(result.model_dump_json(indent=2))
