from strands import Agent
from strands_tools import calculator

agent = Agent(tools=[calculator])
agent("What is the square root of 1764")
agent("What is the square root of 1784")
agent("What is the square root of 1600")

# Shows tool calls and results,you can examine the tool interactions in the conversation history
print(agent.messages)
