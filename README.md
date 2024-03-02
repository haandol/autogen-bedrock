# Autogen Bedrock

This is a simple example of how to use the Autogen with bedrock.

# Prerequisites

- AWS CLI already configured with Administrator permission
- Python 3.10+

# Setup

install dependencies

```bash
pip install -r requirements.txt
```

## Run app on Bedrock via LiteLLM

run litellm

```bash
AWS_REGION=us-east-1 litellm --model bedrock/anthropic.claude-v2:1
```

## Run app locally with Ollama

install [ollama](https://ollama.com)

```bash
brew install ollama
ollama run codellama:7b-instruct
```

# Test

## Copy env

```bash
cp env/prod.env .env
```

## Run the application

```bash
python main.py
```
