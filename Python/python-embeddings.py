"""Example of generating text embeddings via the LLM Gateway.

Embeddings are numerical representations of text — each piece of text is
converted into a list of floating-point numbers (a vector) that captures its
semantic meaning. Text with similar meaning will have vectors that are close
together in this high-dimensional space.

Common use cases:
  - Semantic search: find documents that are conceptually similar to a query,
    even if they don't share the same keywords.
  - Retrieval-Augmented Generation (RAG): retrieve relevant context from a
    knowledge base before passing it to a language model.
  - Clustering: group documents by topic without predefined labels.
  - Classification: train a lightweight classifier on top of embeddings.
  - Anomaly detection: flag text that is semantically unlike the rest of a dataset.
"""
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

# Set the current working directory to the same directory as this file.
# This ensures the .env file is found regardless of where the script is run from.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables (API key, base URL, model name) from the .env file.
if not load_dotenv(".env"):
    print("Unable to load .env file.", file=sys.stderr)
    sys.exit(1)

# Create the OpenAI client pointed at the LLM Gateway base URL.
client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
    base_url=os.environ['OPENAI_API_BASE'],
)

# Generate an embedding for a single string.
# The model converts the text into a vector of floating-point numbers.
response = client.embeddings.create(
    input="The University of Michigan is located in Ann Arbor, Michigan.",
    model=os.environ['EMBEDDING_MODEL'],
)

embedding = response.data[0].embedding

print(f"Model:      {response.model}")
print(f"Dimensions: {len(embedding)}")
print(f"Vector:     {embedding[:5]} ...")  # first 5 values as a preview
