from strands import Agent
from strands_tools import http_request

# Create an agent with http capability
agent = Agent(tools=[http_request])
#agent("Tell me the stock price for Tesla in May 23th, 2025.")
agent("check Tesla's current stock price")