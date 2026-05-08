import os
import base64
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
    base_url=os.environ["OPENAI_API_BASE"],
)

#Send a completion request.
response = client.images.generate(
    model=os.environ['MODEL'],
    prompt="University of Michigan block M logo in the style of a Pixar movie, with a blue sky and green grass background",
    quality="low",
    size="1024x1024",
    response_format="b64_json",
)

#Decode base64 image data and save it to a file.
image_data = base64.b64decode(response.data[0].b64_json)
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "generated_image.png")
with open(output_path, "wb") as f:
    f.write(image_data)

#Print path to saved image. 
print(f"Image saved to: {output_path}")