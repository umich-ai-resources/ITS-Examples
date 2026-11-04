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

| Model | Chat Completions | Responses API | Embeddings | Image Generation | Reasoning
|-------|:---:|:---:|:---:|:---:|:---:|
| gpt-4o | ✅ | ✅ | ❌ | ❌ | ❌ |
| gpt-4o-mini | ✅ | ✅ | ❌ | ❌ | ❌ |
| gpt-4.1 | ✅ | ✅ | ❌ | ❌ | ❌ |
| gpt-4.1-mini | ✅ | ✅ | ❌ | ❌ | ❌ |
| gpt-4.1-nano | ✅ | ✅ | ❌ | ❌ | ❌ |
| gpt-5 | ✅ | ✅ | ❌ | ❌ | ✅ |
| gpt-5-mini | ✅ | ✅ | ❌ | ❌ | ✅ |
| gpt-5.1 | ✅ | ✅ | ❌ | ❌ | ✅ |
| gpt-5.2 | ✅ | ✅ | ❌ | ❌ | ✅ |
| gpt-5.4 | ✅ | ✅ | ❌ | ❌ | ✅ |
| gpt-5.5 | ✅ | ✅ | ❌ | ❌ | ✅ |
| gpt-5.6-sol | ✅ | ✅ | ❌ | ❌ | ✅ |
| gpt-5.6-terra | ✅ | ✅ | ❌ | ❌ | ✅ |
| gpt-5.6-luna | ✅ | ✅ | ❌ | ❌ | ✅ |
| gpt-6-astra | ✅ | ✅ | ❌ | ❌ | ✅ |
| gpt-6-sol | ✅ | ✅ | ❌ | ❌ | ✅ |
| gpt-6-luna | ✅ | ✅ | ❌ | ❌ | ✅ |
| gpt-6.1-sol | ✅ | ✅ | ❌ | ❌ | ✅ |
| gpt-image-1.5 | ❌ | ❌ | ❌ | ✅ | ❌ |
| gpt-image-2 | ❌ | ❌ | ❌ | ✅ | ❌ |
| gpt-image-2.5-flare | ❌ | ❌ | ❌ | ✅ | ❌ |
| gpt-image-2.5-sunburst | ❌ | ❌ | ❌ | ✅ | ❌ |
| claude-haiku-4-5 | ✅ | ✅ | ❌ | ❌ | ❌ |
| claude-sonnet-4-6 | ✅ | ✅ | ❌ | ❌ | ✅ |
| claude-opus-4-6 | ✅ | ✅ | ❌ | ❌ | ✅ |
| claude-opus-4-7 | ✅ | ✅ | ❌ | ❌ | ✅ |
| claude-opus-4-8 | ✅ | ✅ | ❌ | ❌ | ✅ |
| claude-sonnet-5 | ✅ | ✅ | ❌ | ❌ | ✅ |
| claude-opus-5 | ✅ | ✅ | ❌ | ❌ | ✅ |
| claude-fable-5-1 | ✅ | ✅ | ❌ | ❌ | ✅ |
| claude-sonnet-5-5 | ✅ | ✅ | ❌ | ❌ | ✅ |
| claude-haiku-5-5 | ✅ | ✅ | ❌ | ❌ | ✅ |
| claude-opus-5-5 | ✅ | ✅ | ❌ | ❌ | ✅ |
| gemini-3-flash-preview | ✅ | ✅ | ❌ | ❌ | ✅ |
| gemini-3-flash-image-preview | ❌ | ❌ | ❌ | ✅ | ❌ |
| gemini-3.5-flash | ✅ | ✅ | ❌ | ❌ | ✅ |
| gemini-3.6-flash | ✅ | ✅ | ❌ | ❌ | ✅ |
| gemini-3.7-flash | ✅ | ✅ | ❌ | ❌ | ✅ |
| gemini-3.8-flash | ✅ | ✅ | ❌ | ❌ | ✅ |
| deepseek-v4-flash-0731 | ✅ | ✅ | ❌ | ❌ | ✅ |
| deepseek-v4-pro | ✅ | ✅ | ❌ | ❌ | ✅ |
| deepseek-v4.1-flash | ✅ | ✅ | ❌ | ❌ | ✅ |
| grok-4.6 | ✅ | ✅ | ❌ | ❌ | ✅ |
| kimi-k2.5 | ✅ | ❌ | ❌ | ❌ | ✅ |
| kimi-k3 | ✅ | ✅ | ❌ | ❌ | ✅ |
| text-embedding-3-small | ❌ | ❌ | ✅ | ❌ | ❌ |
| text-embedding-3-large | ❌ | ❌ | ✅ | ❌ | ❌ |

> **Note:** This table reflects current gateway support and will be updated as new models and endpoints are added.

## Examples by language

| Language | Folder |
|----------|--------|
| Python | [Python/](Python/) |
| JavaScript | [JavaScript/](JavaScript/) |
| curl | [curl/](curl/) |
| PowerShell | [PowerShell/](PowerShell/) |

