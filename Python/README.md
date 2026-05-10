# Python Examples

This is a collection of example Python scripts for accessing the U-M GPT Toolkit API.

## Setup

Copy `.env.example` to `.env` and fill in your credentials:

```
cp .env.example .env
```

| Variable | Description |
|----------|-------------|
| `OPENAI_API_KEY` | Your API key |
| `OPENAI_API_BASE` | The gateway base URL |
| `MODEL` | Model to use for text examples |
| `IMAGE_MODEL` | Model to use for image generation (`python-image.py`) |

Run `get_models.py` to see all available model names.

## Examples

| Script | Description |
|--------|-------------|
| `python-responses.py` | Basic request using the Responses API (recommended) |
| `python-chat.py` | Basic request using the Chat Completions API |
| `python-reasoning.py` | Reasoning model using the `reasoning.effort` parameter |
| `python-structured.py` | Structured output enforced with a Pydantic JSON Schema |
| `python_json.py` | JSON object output mode |
| `python-vision.py` | Analyze an image via URL or a base64-encoded local file |
| `python-image.py` | Generate an image with DALL-E, saved as a PNG |
| `get_models.py` | List all available models grouped by provider |
| `python-langchain.py` | Use the gateway through the LangChain framework |
| `python-ner.py` | Named Entity Recognition (NER) using few-shot prompting |
