import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

#Set the current working directory to be the same as the file.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Load environment file for secrets.
try:
    if load_dotenv('.env') is False:
        raise TypeError
except TypeError:
    print('Unable to load .env file.')
    quit()

#Define LLM parameters.
llm = ChatOpenAI(
    model_name=os.environ['MODEL'],
    api_key=os.environ['OPENAI_API_KEY'],
    base_url = os.environ['OPENAI_API_BASE']
)

#Create Query.
messages = [
    ("system","You are a helpful assistant.  Always say GO BLUE! at the end of your response."),
    ("human", "Explain step by step. Where is the University of Michigan?"),
]

#Send a completion request.
response = llm.invoke(messages)

#Get and print response
print(response.content)
