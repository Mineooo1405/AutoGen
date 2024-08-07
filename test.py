from autogen import ConversableAgent

llm_config = [
    {
    "model": "codellama",
    "base_url": "http://127.0.0.1:11434/v1",
    "api_key": 'ollama'
    }
]

Minh = ConversableAgent(
      name="Minh",
      system_message="You are an orator in a two-person debate",
      llm_config = {"config_list": llm_config },
      human_input_mode="NEVER"  
)

Nhi = ConversableAgent(
      name = "Nhi",
      system_message="You are an orator in a two-person debate",
      llm_config = {"config_list": llm_config },
      human_input_mode="NEVER"
)

result = Minh.initiate_chat(Nhi, message="Nhi, raising the age of retirement will gain more benefit. Change my mind.", max_turns = 2) 