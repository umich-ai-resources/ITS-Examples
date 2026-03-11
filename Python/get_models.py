import os
from openai import OpenAI
from dotenv import load_dotenv

#Sets the current working directory to be the same as the file.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Load environment file for secrets.
try:
    if load_dotenv('.env') is False:
        raise TypeError
except TypeError:
    print('Unable to load .env file.')
    quit()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("OPENAI_API_BASE")
)

models = client.models.list()

# Group models by provider prefix (e.g., @google/, @anthropic/)
groups = {}
for model in models.data:
    model_id = model.id
    if '/' in model_id:
        provider, name = model_id.split('/', 1)
        provider = provider.lstrip('@').title()
    else:
        provider = 'General'
        name = model_id
    groups.setdefault(provider, []).append(model_id)

# Print sorted groups with sorted models
for provider in sorted(groups):
    model_list = sorted(groups[provider])
    print(f"\n{provider} ({len(model_list)} models):")
    for model_id in model_list:
        print(f"  {model_id}")