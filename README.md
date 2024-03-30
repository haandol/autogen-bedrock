# Autogen Bedrock

This is a simple example of how to use the Autogen with bedrock.

# Prerequisites

- AWS CLI already configured with Administrator permission
- Python 3.12+

# Setup

install dependencies

```bash
pip install -r requirements.txt
```

## Run app on Bedrock via LiteLLM

run litellm

```bash
AWS_REGION=us-east-1 litellm --model anthropic.claude-3-sonnet-20240229-v1:0 --drop_params
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
