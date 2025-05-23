from strands import Agent
from strands_tools import swarm,http_request

# Create an agent with swarm capability
#agent = Agent(tools=[swarm, http_request])
agent = Agent(tools=[swarm])

# Process a complex task with multiple agents in parallel
result = agent.tool.swarm(
    task="Analyze the recent stock price for Tesla and its future stock tranding.",
    swarm_size=4,
    coordination_pattern="collaborative"
)

# The result contains contributions from all swarm agents
print(result["content"])