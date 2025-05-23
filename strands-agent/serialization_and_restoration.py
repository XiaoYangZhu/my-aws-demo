import json
import os
import uuid
from strands import Agent

# Save agent state
def save_agent_state(agent, session_id):
    os.makedirs("sessions", exist_ok=True)

    state = {
        "messages": agent.messages,
        "system_prompt": agent.system_prompt
    }
    # Store state (e.g., database, file system, cache)
    with open(f"sessions/{session_id}.json", "w") as f:
        json.dump(state, f)

# Restore agent state
def restore_agent_state(session_id):
    # Retrieve state
    with open(f"sessions/{session_id}.json", "r") as f:
        state = json.load(f)

    # Create agent with restored state
    print("initial agent messages:")
    print(state["messages"])
    return Agent(
        messages=state["messages"],
        system_prompt=state["system_prompt"]
    )

agent = Agent(system_prompt="Talk like a pirate")
agent_id = uuid.uuid4()

print("Initial agent:")
agent("Where are Octopus found? 🐙")
save_agent_state(agent, agent_id)

# Create a new Agent object with the previous agent's saved state
restored_agent = restore_agent_state(agent_id)
print("\n\nRestored agent:")
restored_agent("What did we just talk about?")

print("\n\n")
print("restored agent messages:")
print(restored_agent.messages)  # Both messages and responses are in the restored agent's conversation history