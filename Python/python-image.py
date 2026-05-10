"""Example of using the LLM Gateway to generate an image.

The model returns the image as base64-encoded JSON, which is then decoded
and saved as a PNG file in the same directory as this script.
"""
import base64
import os

from dotenv import load_dotenv
from openai import OpenAI

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

# Create the OpenAI client pointed at the LLM Gateway base URL.
client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
    base_url=os.environ['OPENAI_API_BASE'],
)

# Request image generation. 'response_format=b64_json' returns the image as
# base64 text rather than a URL, so it can be saved locally without a second download.
# IMAGE_MODEL is set separately from MODEL so you can keep different models
# for text and image generation in the same .env file.
response = client.images.generate(
    model=os.environ['IMAGE_MODEL'],
    prompt="University of Michigan block M logo in the style of a Pixar movie, with a blue sky and green grass background",
    quality="low",
    size="1024x1024",
    response_format="b64_json",
)

# Decode the base64 image data and write it to a PNG file.
image_data = base64.b64decode(response.data[0].b64_json)
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "generated_image.png")
with open(output_path, "wb") as f:
    f.write(image_data)

# Print the path so the user knows where to find the saved image.
print(f"Image saved to: {output_path}")
