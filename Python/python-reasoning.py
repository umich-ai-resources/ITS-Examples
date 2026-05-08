import os
from openai import OpenAI
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

#Create OpenAI client.
client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
    base_url = os.environ['OPENAI_API_BASE']
)

#Create Query.
messages=[
        {"role": "system","content": "You are a helpful assistant.  Always say GO BLUE! at the end of your response."},
        {"role": "user","content": "Explain step by step. Where is the University of Michigan?"},
    ]

completion_kwargs={"reasoning_effort": "high"}

#Send a completion request.
response = client.chat.completions.create(
        model=os.environ['MODEL'], ## Make sure you set a reasoning model in your .env file.  Example: o1, o3-mini, etc.
        reasoning_effort="high",  ##Set your reasoning effort here.  Options are "low", "medium", "high".  Only works with reasoning models (o1, o3-mini, etc).
        ##Temperature, top_p, presence_penalty, frequency_penalty, logprobs, top_logprobs, logit_bias, max_tokensis are not supported with reasoning models.
        messages=messages)

#Print response.
print(response.choices[0].message.content)
