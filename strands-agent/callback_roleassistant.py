import json
from strands import Agent
from strands_tools import calculator

def message_buffer_handler(**kwargs):
    # When a new message is created from the assistant, print its content
    if "message" in kwargs and kwargs["message"].get("role") == "assistant":
        print(json.dumps(kwargs["message"], indent=2))

# Usage with an agent
agent = Agent(
    tools=[calculator],
    callback_handler=message_buffer_handler
)

agent("What is 2+2 and tell me about AWS Lambda")