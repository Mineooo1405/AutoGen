import autogen
import json
import openai
import os

llm_config = [
    {
    "model": "codellama",
    "base_url": "http://127.0.0.1:11434/v1",
    "api_key": 'ollama'
    }
]

Assistant = autogen.AssistantAgent(
    name = "assitant",
    llm_config = {"config_list": llm_config } 
)

userProxy = autogen.UserProxyAgent(
    name = "Nguoi Dung",
    human_input_mode = "ALWAYS",
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False
    }
)

question = """
    Generate a C++ code to print a rectangular
"""

userProxy.initiate_chat(Assistant, message=question)

# === === 