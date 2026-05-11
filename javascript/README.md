# JavaScript Example

This is an example JavaScript script for accessing the U-M GPT Toolkit API.

## Setup

Fill in your credentials in example.js for api_key, api_base, and model.

| Variable | Description |
|----------|-------------|
| `api_key` | Your API key |
| `api_base` | The gateway base URL |
| `model` | Model to be used |

Run `Python/get_models.py` to see all available model names.

Please create a package.json file in the same directory as your script with the following:

{
  "type": "module",
  "dependencies": {
    "openai": "^4.20.1"
  }
}