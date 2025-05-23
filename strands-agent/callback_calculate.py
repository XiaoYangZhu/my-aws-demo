from strands import Agent
from strands_tools import calculator

def custom_callback_handler(**kwargs):
    # Process stream data
    if "data" in kwargs:
        print(f"MODEL OUTPUT: {kwargs['data']}")
    elif "current_tool_use" in kwargs and kwargs["current_tool_use"].get("name"):
        print(f"\nUSING TOOL: {kwargs['current_tool_use']['name']}")

# Create an agent with custom callback handler
agent = Agent(
    tools=[calculator],
    callback_handler=custom_callback_handler
)

agent("Calculate 2+2")