"""Structured outputs make a model follow a JSON Schema definition that you provide as part of your inference API call."""
import os
from openai import OpenAI
import openai
from dotenv import load_dotenv
from pydantic import BaseModel

#Set the current working directory to be the same as the file.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Load environment file for secrets.
try:
    if load_dotenv('.env') is False:
        raise TypeError
except TypeError:
    print('Unable to load .env file.')
    quit()

#Create OpenAI client
client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
    base_url=os.environ['OPENAI_API_BASE']
)

#Define the Pydantic model for the structured output.
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


#Define tools for the OpenAI client.
tools = [openai.pydantic_function_tool(Extract)]

text = """"I am a student at the University of Michigan in Ann Arbor, MI.
I like to go to football games at Michigan's football stadium, The Big House. The Big House's seating capacity is 107,601 people. 
The first game of the 2024 football season is on August 31st. U of M's fight song is called The Victors.
The Ann Arbor campus is divided into four main areas: North campus, Central campus, Medical campus, and South campus, for a combined area of more than 37.48 million square feet.
UMich's mascot is the wolverine."""

#Create Query.
messages=[
        {"role": "system","content": "You are an expert in Natural Language Processing. Your task is to identify common Named Entities (NER) in a given text.  Use the tools you have been given to structure the extracted data in the desired format."},
        {"role": "user","content": f"{text}"},
    ]

#Send a completion request.
response = client.beta.chat.completions.parse(
    model=os.environ['MODEL'],
    messages=messages,
    temperature=0,
    tools=tools
    )

#Print response.
print(response.choices[0].message.tool_calls[0].function.arguments)