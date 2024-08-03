import autogen
import json
import openai
import os

api_key = "sk-proj-Oe48zvwErLUek2R7NvuTT3BlbkFJROpQMDhjdAAj4hGeZ35u"
openai.api_key = api_key
os.environ['OPENAI_API_KEY'] = 'sk-proj-Oe48zvwErLUek2R7NvuTT3BlbkFJROpQMDhjdAAj4hGeZ35u'

configList = [{
    "model": "gpt-3.5-turbo",
    "api_key": 'sk-proj-Oe48zvwErLUek2R7NvuTT3BlbkFJROpQMDhjdAAj4hGeZ35u',

}]

llm_config = {
    "config_list": [{
    "model": "gpt-3.5-turbo",
    "api_key": 'sk-proj-Oe48zvwErLUek2R7NvuTT3BlbkFJROpQMDhjdAAj4hGeZ35u',

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