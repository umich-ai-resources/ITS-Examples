from openai import OpenAI 
import os
from dotenv import load_dotenv

# Sets the current working directory to be the same as the file.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load environment file for secrets.
if not load_dotenv('.env'):
    print('Unable to load .env file.')
    quit()

# Create OpenAI client
client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
    base_url=os.environ.get("OPENAI_API_BASE"),
)

# Returns a list of entities based on the label given.
def labels():

    # create a dictionary with your entity labels.  By defining which label goes with each entity, we can build a list based on label.
    labels_list = {
        'University',
        'Department',
        'Role',
        "Supervisor Name",
        "Facility",
        "City",
        "State",
        "Location",
        "Event",
        "Work_of_art",
        "Date",
        "Time",
        "Quantity",
        "Mascot",
    }

    return labels_list

# Creates the assistant message for the api call.  The assistant message gives an example of how the LLM should respond.
def assistant_message():
    return f"""
EXAMPLE:
    Text: 'In Germany, in 1440, goldsmith Johannes Gutenberg invented the movable-type printing press. His work led to an information revolution and the unprecedented mass-spread / 
    of literature throughout Europe. Modelled on the design of the existing screw presses, a single Renaissance movable-type printing press could produce up to 3,600 pages per workday.'
    {{
        "gpe": ["Germany", "Europe"],
        "date": ["1440"],
        "person": ["Johannes Gutenberg"],
        "product": ["movable-type printing press"],
        "event": ["Renaissance"],
        "quantity": ["3,600 pages"],
        "time": ["workday"]
    }}
--"""

def system_message(labels_list):
    # print(type(labels_list))
    types=", ".join(labels_list)
    return f"""
You are an expert in Natural Language Processing. Your task is to identify common Named Entities (NER) in a given text.
The possible common Named Entities (NER) types are exclusively: ({types})."""

# Call labels function with 'pi' option (other options are orderform/resume)
labels_list = labels()

# Create usermessage function
def user_message(text):
    return f"""
TASK:
    Text: {text}
"""

# Call API
def run_ner_task(labels_list, text):
    messages = [
          {"role": "system", "content": system_message(labels_list)},
          {"role": "assistant", "content": assistant_message()},
          {"role": "user", "content": user_message(text=text)}
      ]

    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0,
        frequency_penalty=0,
        presence_penalty=0,
    )

    response_message = response.choices[0].message
    return response_message

# Sample text
text = """"I am a student at the University of Michigan in Ann Arbor, MI.
I like to go to football games at Michigan's football stadium, The Big House. The Big House's seating capacity is 107,601 people. 
The first game of the 2024 football season is on August 31st. U of M's fight song is called The Victors.
I work at the U-M ITS department in GenAI Services. 
I have meetings with my supervisors, Ben and Don, each workday at 9:30 am.
The Ann Arbor campus is divided into four main areas: North campus, Central campus, Medical campus, and South campus, for a combined area of more than 37.48 million square feet.
UMich's mascot is the wolverine."""


result = run_ner_task(labels_list, text)
print(result.content)