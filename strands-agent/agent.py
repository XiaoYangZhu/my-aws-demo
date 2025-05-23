# agent.py

from strands import Agent
import get_user_location
import weather

# Tools can be added to agents through Python module imports
agent = Agent(tools=[get_user_location, weather])

# Use the agent with the custom tools
agent("What is the weather like in my location?")