import os
from openai import OpenAI
from dotenv import load_dotenv
import base64

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
    base_url=os.environ['OPENAI_API_BASE']
)

#Create Query.
messages=[
        {"role": "system", "content": "You are a helpful assistant that responds in Markdown!  Help the user by describing the picture."},
        {"role": "user", "content": [
            {"type": "text", "text": "What is this picture of?"},
            {"type": "image_url", "image_url": {
                "url": "https://michiganross.umich.edu/sites/default/files/styles/max_1300x1300/public/images/news-story/butterfly.jpeg"}
            }
        ]}
    ]

# Send a completion request.
response = client.chat.completions.create(
    model=os.environ['MODEL'],
    messages=messages,
    temperature=0.0,
)

#Print response.
print(response.choices[0].message.content)
