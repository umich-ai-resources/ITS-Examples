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
| `EMBEDDING_MODEL` | Model to use for embeddings (`python-embeddings.py`) |
| `REASONING_MODEL` | Model to use for reasoning (`python-.py`) |

Run `get_models.py` to see all available model names.

## Examples

| Script | Description |
|--------|-------------|
| `python-responses.py` | Basic request using the Responses API (recommended) |
| `python-chat.py` | Basic request using the Chat Completions API |
| `python_json.py` | JSON object output mode |
| `python-structured.py` | Structured output enforced with a Pydantic JSON Schema |
| `python-vision.py` | Analyze an image via URL or a base64-encoded local file |
| `python-langchain.py` | Use the gateway through the LangChain framework |
| `python-ner.py` | Named Entity Recognition (NER) using few-shot prompting |
| `python-image.py` | Generate an image saved as a PNG |
| `python-embeddings.py` | Generate text embeddings and learn what they can be used for |
| `python-reasoning.py` | Reasoning model using the `reasoning.effort` parameter |
| `python-document.py` | Analyze a PDF via URL or an uploaded local file |
| `get_models.py` | List all available models grouped by provider |
