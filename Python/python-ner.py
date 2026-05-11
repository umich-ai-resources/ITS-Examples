"""Named Entity Recognition (NER) example using the Responses API and the LLM Gateway.

Two techniques are layered together:
  1. Few-shot prompting — a worked example in the instructions shows the model
     the exact label set and output format it should produce.
  2. Structured outputs — a Pydantic model defines the schema and is passed to
     the API as a strict JSON Schema, so the response is guaranteed to parse
     into a typed Python object.

Either technique works on its own; using both gives the model a concrete
demonstration *and* a hard schema contract.
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
    base_url=os.environ.get("OPENAI_API_BASE"),
)


# Pydantic model defining the exact set of entity labels to extract.
# Field names double as the label set used in the prompt and few-shot example,
# so there is one source of truth for what the model should return.
class Entities(BaseModel):
    University: list[str]
    Department: list[str]
    Role: list[str]
    Supervisor_Name: list[str]
    Facility: list[str]
    City: list[str]
    State: list[str]
    Location: list[str]
    Event: list[str]
    Work_of_art: list[str]
    Date: list[str]
    Time: list[str]
    Quantity: list[str]
    Mascot: list[str]


def few_shot_example():
    """Return a worked example using the exact labels defined by the Entities model."""
    return """\
EXAMPLE:
    Text: 'Dr. Jane Smith is a professor in the Computer Science Department at Stanford University in Palo Alto, CA. She advises graduate student Alex Chen and teaches in the Gates Computer Science Building. Stanford's mascot is the Cardinal. The department hosted its annual Research Symposium on October 5, 2023 at 2:00 pm, drawing over 500 attendees.'
    {
        "University": ["Stanford University"],
        "Department": ["Computer Science Department"],
        "Role": ["professor", "graduate student"],
        "Supervisor_Name": ["Dr. Jane Smith"],
        "Facility": ["Gates Computer Science Building"],
        "City": ["Palo Alto"],
        "State": ["CA"],
        "Location": [],
        "Event": ["Research Symposium"],
        "Work_of_art": [],
        "Date": ["October 5, 2023"],
        "Time": ["2:00 pm"],
        "Quantity": ["500 attendees"],
        "Mascot": ["Cardinal"]
    }
--"""


def build_instructions():
    """Build the full system instructions including entity types and a few-shot example."""
    types = ", ".join(Entities.model_fields.keys())
    system = (
        "You are an expert in Natural Language Processing. Your task is to identify common "
        "Named Entities (NER) in a given text.\n"
        f"The possible Named Entity (NER) types are exclusively: ({types}). "
        "Return a JSON object with one key per label, whose value is a list of matching "
        "strings from the text. Use an empty list for labels with no matches."
    )
    return f"{system}\n\n{few_shot_example()}"


def run_ner_task(text):
    """Send the NER request to the LLM Gateway with a strict JSON Schema and return the parsed result."""
    schema = Entities.model_json_schema()
    schema["additionalProperties"] = False

    response = client.responses.create(
        model=os.environ['MODEL'],
        instructions=build_instructions(),
        input=f"\nTASK:\n    Text: {text}\n",
        text={
            "format": {
                "type": "json_schema",
                "name": "Entities",
                "schema": schema,
                "strict": True,
            }
        },
    )
    return Entities.model_validate_json(response.output_text)


# Sample text containing a variety of entity types for demonstration.
text = (
    'I am a student at the University of Michigan in Ann Arbor, MI. '
    "I like to go to football games at Michigan's football stadium, The Big House. "
    "The Big House's seating capacity is 107,601 people. "
    "The first game of the 2024 football season is on August 31st. "
    "U of M's fight song is called The Victors. "
    "I work at the U-M ITS department in GenAI Services. "
    "I have meetings with my supervisors, Ben and Don, each workday at 9:30 am. "
    "The Ann Arbor campus is divided into four main areas: North campus, Central campus, "
    "Medical campus, and South campus, for a combined area of more than 37.48 million square feet. "
    "UMich's mascot is the wolverine."
)

result = run_ner_task(text)
print(result.model_dump_json(indent=2))
