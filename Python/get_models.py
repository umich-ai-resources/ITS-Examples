"""List all models available on the LLM Gateway, grouped by provider."""
import os

from dotenv import load_dotenv
from openai import OpenAI

# Set the current working directory to the same directory as this file.
# This ensures the .env file is found regardless of where the script is run from.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables (API key, base URL) from the .env file.
try:
    if load_dotenv('.env') is False:
        raise TypeError
except TypeError:
    print('Unable to load .env file.')
    quit()

# Create the OpenAI client pointed at the LLM Gateway base URL.
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE"),
)

# Fetch the full list of models available on the gateway.
models = client.models.list()

# Group models by provider. Gateway model IDs follow the pattern '<provider>-<name>',
# so we split on the first hyphen to extract the provider name.
groups = {}
for model in models.data:
    model_id = model.id
    if '-' in model_id:
        provider, name = model_id.split('-', 1)
        provider = provider.lstrip('@').title()
    else:
        provider = 'General'
        name = model_id
    groups.setdefault(provider, []).append(model_id)

# Print each provider and its models in alphabetical order.
for provider in sorted(groups):
    model_list = sorted(groups[provider])
    print(f"\n{provider} ({len(model_list)} models):")
    for model_id in model_list:
        print(f"  {model_id}")
