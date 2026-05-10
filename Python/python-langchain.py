"""Example of using the LLM Gateway through the LangChain framework.

LangChain's ChatOpenAI wraps the OpenAI-compatible API, making it easy to
swap in the LLM Gateway by providing the custom base_url.
"""
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

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

# Configure the LangChain LLM wrapper to point at the LLM Gateway.
# base_url overrides the default OpenAI endpoint, routing requests to the gateway.
llm = ChatOpenAI(
    model_name=os.environ['MODEL'],
    api_key=os.environ['OPENAI_API_KEY'],
    base_url=os.environ['OPENAI_API_BASE'],
)

# Build the conversation using LangChain's tuple format: (role, content).
# 'system' sets the assistant behavior; 'human' is the user turn.
messages = [
    ("system", "You are a helpful assistant. Always say GO BLUE! at the end of your response."),
    ("human", "Explain step by step. Where is the University of Michigan?"),
]

# Invoke the model with the message list and capture the response.
response = llm.invoke(messages)

# Print the text content of the response.
print(response.content)
