import os

import dotenv
import autogen

from logger import logger
from prompt import SystemMessage

dotenv.load_dotenv()

if os.environ.get("ENV") == "production":
    logger.info("use bedrock-claude")
    config_list = [
        {
            "model": "bedrock-claude",
            "base_url": "http://localhost:8000/v1",
            "api_key": "nil",
        }
    ]
else:
    logger.info("use ollama")
    config_list = [
        {
            "model": "codellama:7b-instruct",
            "base_url": "http://localhost:11434/v1",
            "api_key": "nil",
        },
    ]


def is_termination_msg(msg):
    return "TERMINATE" in msg.get("content", "").rstrip().upper()


user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=is_termination_msg,
    code_execution_config={"work_dir": "coding", "use_docker": True},
    system_message=SystemMessage,
)

assistant = autogen.AssistantAgent("coder", llm_config={"config_list": config_list})

user_proxy.initiate_chat(
    assistant, message="Plot a chart of NVDA and TESLA stock price change YTD."
)
