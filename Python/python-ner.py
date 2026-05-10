"""Named Entity Recognition (NER) example using the Responses API and the LLM Gateway.

The model is prompted with a set of entity labels and a sample text, then asked
to identify and return instances of each label. A few-shot example is embedded in
the instructions so the model understands the expected output format.
"""
import os

from dotenv import load_dotenv
from openai import OpenAI

# Set the current working directory to the same directory as this file.
# This ensures the .env file is found regardless of where the script is run from.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables (API key, base URL, model name) from the .env file.
if not load_dotenv('.env'):
    print('Unable to load .env file.')
    quit()

# Create the OpenAI client pointed at the LLM Gateway base URL.
client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
    base_url=os.environ.get("OPENAI_API_BASE"),
)


def labels():
    """Return the list of entity types the model should extract.

    Using a list (not a set) preserves insertion order so the system prompt
    is deterministic across runs — important for reproducible NER results.
    """
    return [
        'University',
        'Department',
        'Role',
        'Supervisor Name',
        'Facility',
        'City',
        'State',
        'Location',
        'Event',
        'Work_of_art',
        'Date',
        'Time',
        'Quantity',
        'Mascot',
    ]


def few_shot_example():
    """Return a concrete example showing the model the desired JSON output format."""
    return """\
EXAMPLE:
    Text: 'In Germany, in 1440, goldsmith Johannes Gutenberg invented the movable-type printing press. His work led to an information revolution and the unprecedented mass-spread / \
of literature throughout Europe. Modelled on the design of the existing screw presses, a single Renaissance movable-type printing press could produce up to 3,600 pages per workday.'
    {
        "gpe": ["Germany", "Europe"],
        "date": ["1440"],
        "person": ["Johannes Gutenberg"],
        "product": ["movable-type printing press"],
        "event": ["Renaissance"],
        "quantity": ["3,600 pages"],
        "time": ["workday"]
    }
--"""


def build_instructions(labels_list):
    """Build the full system instructions including entity types and a few-shot example."""
    types = ", ".join(labels_list)
    system = (
        "You are an expert in Natural Language Processing. Your task is to identify common "
        f"Named Entities (NER) in a given text.\n"
        f"The possible common Named Entities (NER) types are exclusively: ({types})."
    )
    return f"{system}\n\n{few_shot_example()}"


def run_ner_task(labels_list, text):
    """Send the NER request to the LLM Gateway and return the extracted entity text.

    The few-shot example is embedded in the instructions rather than passed as a
    separate assistant turn, which is the idiomatic pattern for the Responses API.
    """
    response = client.responses.create(
        model=os.environ['MODEL'],
        instructions=build_instructions(labels_list),
        input=f"\nTASK:\n    Text: {text}\n",
    )
    return response.output_text


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

labels_list = labels()
result = run_ner_task(labels_list, text)
print(result)
