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


user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "coding", "use_docker": False},
    system_message=SystemMessage,
)

assistant = autogen.AssistantAgent("coder", llm_config={"config_list": config_list})

user_proxy.initiate_chat(
    assistant, message="Write python script that lists the number from 1 to 100."
)
