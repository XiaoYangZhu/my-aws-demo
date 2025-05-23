from strands import Agent

query="I want to promote branding of Tesla and want to know how to do it from market promotion perspective"

# Create specialized agents with different expertise
research_agent = Agent(system_prompt=("""You are a Research Agent specializing in gathering and analyzing information.
Your role in the swarm is to provide factual information and research insights on the topic.
You should focus on providing accurate data and identifying key aspects of the problem.
When receiving input from other agents, evaluate if their information aligns with your research.
"""), 
callback_handler=None)

creative_agent = Agent(system_prompt=("""You are a Creative Agent specializing in generating innovative solutions.
Your role in the swarm is to think outside the box and propose creative approaches.
You should build upon information from other agents while adding your unique creative perspective.
Focus on novel approaches that others might not have considered.
"""), 
callback_handler=None)

critical_agent = Agent(system_prompt=("""You are a Critical Agent specializing in analyzing proposals and finding flaws.
Your role in the swarm is to evaluate solutions proposed by other agents and identify potential issues.
You should carefully examine proposed solutions, find weaknesses or oversights, and suggest improvements.
Be constructive in your criticism while ensuring the final solution is robust.
"""), 
callback_handler=None)

summarizer_agent = Agent(system_prompt="""You are a Summarizer Agent specializing in synthesizing information.
Your role in the swarm is to gather insights from all agents and create a cohesive final solution.
You should combine the best ideas and address the criticisms to create a comprehensive response.
Focus on creating a clear, actionable summary that addresses the original query effectively.
""")

#The mesh communication is implemented using a dictionary to track messages between agents:
# Dictionary to track messages between agents (mesh communication)
messages = {
    "research": [],
    "creative": [],
    "critical": [],
    "summarizer": []
}

# Phase 1: Initial analysis by each specialized agent
research_result = research_agent(query)
creative_result = creative_agent(query)
critical_result = critical_agent(query)

# Share results with all other agents (mesh communication)
messages["creative"].append(f"From Research Agent: {research_result}")
messages["critical"].append(f"From Research Agent: {research_result}")
messages["summarizer"].append(f"From Research Agent: {research_result}")

messages["research"].append(f"From Creative Agent: {creative_result}")
messages["critical"].append(f"From Creative Agent: {creative_result}")
messages["summarizer"].append(f"From Creative Agent: {creative_result}")

messages["research"].append(f"From Critical Agent: {critical_result}")
messages["creative"].append(f"From Critical Agent: {critical_result}")
messages["summarizer"].append(f"From Critical Agent: {critical_result}")

# Phase 2: Each agent refines based on input from others
research_prompt = f"{query}\n\nConsider these messages from other agents:\n" + "\n\n".join(messages["research"])
creative_prompt = f"{query}\n\nConsider these messages from other agents:\n" + "\n\n".join(messages["creative"])
critical_prompt = f"{query}\n\nConsider these messages from other agents:\n" + "\n\n".join(messages["critical"])

refined_research = research_agent(research_prompt)
refined_creative = creative_agent(creative_prompt)
refined_critical = critical_agent(critical_prompt)

# Share refined results with summarizer
messages["summarizer"].append(f"From Research Agent (Phase 2): {refined_research}")
messages["summarizer"].append(f"From Creative Agent (Phase 2): {refined_creative}")
messages["summarizer"].append(f"From Critical Agent (Phase 2): {refined_critical}")

# Final phase: Summarizer creates the final solution
summarizer_prompt = f"""
Original query: {query}

Please synthesize the following inputs from all agents into a comprehensive final solution:

{" ".join(messages["summarizer"])}

Create a well-structured final answer that incorporates the research findings, 
creative ideas, and addresses the critical feedback."""

final_solution = summarizer_agent(summarizer_prompt)