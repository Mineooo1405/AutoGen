import autogen
import json
import openai
import os


os.environ['OPENAI_API_KEY'] = '5c7682a2c590db133483670018c3c8e753c6b888'

configList = [{
    "model": "llama3.1",
    "base_url": "http://localhost:11434"

}]

llm_config = {
    "config_list": [{
    "model": "llama3.1",
    "base_url": "http://localhost:11434"
}]
}

Assistant = autogen.AssistantAgent(
    name = "Ho Tro",
    llm_config= llm_config
)

userProxy = autogen.UserProxyAgent(
    name = "Nguoi Dung",
    human_input_mode = "ALWAYS",
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "use_docker": False
    }
)

question = """
    Generate a C++ code to print a rectangular
"""

userProxy.initiate_chat(Assistant, message=question)

# === === 