from strands import Agent, tool

@tool
def word_count(text: str) -> int:
    """
    Count words in text.
    This docstring is used by the LLM to understand the tool's purpose.
    """
    return len(text.split())

agent = Agent(tools=[word_count])
response = agent("How many words are in this sentence?")