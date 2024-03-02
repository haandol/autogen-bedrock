# Autogen Bedrock

This is a simple example of how to use the autogen with bedrock.

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

run the application

```bash
python main.py
```

## Run app locally with Ollama

install [ollama](https://ollama.com)

```bash
brew install ollama
ollama run codellama:7b-instruct
```

run the application

```bash
python main.py
```
