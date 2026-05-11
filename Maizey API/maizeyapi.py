import requests
import os
from dotenv import load_dotenv
import json

# Set the current working directory to the same directory as this file.
# This ensures the .env file is found regardless of where the script is run from.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

url = 'https://umgpt.umich.edu/maizey/api'

# Fill in the below project_pk with your Maizey Project ID!
project_pk = ''

# Load environment variable (API key) from the .env file.
try:
    if load_dotenv('.env') is False:
        raise TypeError
except TypeError:
    print('Unable to load .env file.')
    quit()

# Basic headers for all Maizey requests.
headers = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + os.environ['token'],
    'Content-Type': 'application/json'
}

# Endpoint for creating new conversations.
new_convo = f'{url}/projects/{project_pk}/conversation/'

# Create a new conversation.
response = requests.post(new_convo, headers=headers, json={})

print(response.json())

# Pull the conversation_pk from the conversation created.
conversation_pk = response.json()["pk"]

# Endpoint for creating new messages.
new_msg = f'{url}/projects/{project_pk}/conversation/{conversation_pk}/messages/'

# Replace the following query with whatever you would like to ask Maizey!
response = requests.post(new_msg, headers=headers, json={
    "query": "Hello, who are you and what can you do?"
})

# Print the Maizey response.
print(response.json()['response'])