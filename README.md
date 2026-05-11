# U-M GPT Toolkit — Code Examples

A collection of code examples for accessing the [U-M GPT Toolkit](https://its.umich.edu/computing/ai/gpt-toolkit-in-depth) API service. For a full overview of AI services available at the University of Michigan, visit the [U-M AI Services page](https://its.umich.edu/computing/ai).

## Required parameters

Each example requires three parameters. These may be named slightly differently depending on the language or framework.

| Parameter | Description |
|-----------|-------------|
| `OPENAI_API_KEY` | Your API key |
| `OPENAI_API_BASE` | The gateway base URL |
| `MODEL` | The model you want to use |

Run `Python/get_models.py` to see the full list of available model names.

## Endpoint compatibility

Not all models support every endpoint. Use the matrix below as a reference when choosing a model for your use case.

| Model | Chat Completions | Responses API | Embeddings | Image Generation |
|-------|:---:|:---:|:---:|:---:|
| gpt-4o | ✅ | ✅ | ❌ | ❌ |
| gpt-4.1 | ✅ | ✅ | ❌ | ❌ |
| gpt-4.1-mini | ✅ | ✅ | ❌ | ❌ |
| gpt-4.1-nano | ✅ | ✅ | ❌ | ❌ |
| o1 | ✅ | ✅ | ❌ | ❌ |
| o3-mini | ✅ | ✅ | ❌ | ❌ |
| gpt-5 | ✅ | ✅ | ❌ | ❌ |
| gpt-5-mini | ✅ | ✅ | ❌ | ❌ |
| gpt-5.1 | ✅ | ✅ | ❌ | ❌ |
| gpt-5.2 | ✅ | ✅ | ❌ | ❌ |
| gpt-5.4 | ✅ | ✅ | ❌ | ❌ |
| gpt-5.5 | ✅ | ✅ | ❌ | ❌ |
| claude-haiku-4-5 | ✅ | ✅ | ❌ | ❌ |
| claude-sonnet-4-6 | ✅ | ✅ | ❌ | ❌ |
| claude-opus-4-6 | ✅ | ✅ | ❌ | ❌ |
| claude-opus-4-7 | ✅ | ✅ | ❌ | ❌ |
| Llama-4-Maverick-17B-128E-Instruct-FP8 | ✅ | ❌ | ❌ | ❌ |
| Llama-4-Scout-17B-16E-Instruct | ✅ | ❌ | ❌ | ❌ |
| text-embedding-3-small | ❌ | ❌ | ✅ | ❌ |
| text-embedding-3-large | ❌ | ❌ | ✅ | ❌ |
| gpt-image-1.5 | ❌ | ❌ | ❌ | ✅ |
| gpt-image-2 | ❌ | ❌ | ❌ | ✅ |

> **Note:** This table reflects current gateway support and will be updated as new models and endpoints are added.

## Examples by language

| Language | Folder |
|----------|--------|
| Python | [Python/](Python/) |
| JavaScript | [JavaScript/](JavaScript/) |
| cURL | [Curl/](Curl/) |
| PowerShell | [PowerShell/](PowerShell/) |

