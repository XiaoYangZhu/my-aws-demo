from strands import Agent, tool

def event_loop_tracker(**kwargs):
    # Track event loop lifecycle
    if kwargs.get("init_event_loop", False):
        print("🔄 Event loop initialized")
    elif kwargs.get("start_event_loop", False):
        print("▶️ Event loop cycle starting")
    elif kwargs.get("start", False):
        print("📝 New cycle started")
    elif "message" in kwargs:
        print(f"📬 New message created: {kwargs['message']['role']}")
    elif kwargs.get("complete", False):
        print("✅ Cycle completed")
    elif kwargs.get("force_stop", False):
        print(f"🛑 Event loop force-stopped: {kwargs.get('force_stop_reason', 'unknown reason')}")

    # Track tool usage
    if "current_tool_use" in kwargs and kwargs["current_tool_use"].get("name"):
        tool_name = kwargs["current_tool_use"]["name"]
        print(f"🔧 Using tool: {tool_name}")

    # Show only a snippet of text to keep output clean
    if "data" in kwargs:
        # Only show first 20 chars of each chunk for demo purposes
        data_snippet = kwargs["data"][:20] + ("..." if len(kwargs["data"]) > 20 else "")
        print(f"📟 Text: {data_snippet}")


# Level 2 - Mid-level Manager Agent with its own specialized tools
@tool
def economic_department(query: str) -> str:
    """Coordinate economic analysis across market and financial domains."""
    print("📈 Economic Department coordinating analysis...")
    econ_manager = Agent(
        system_prompt="""You are an economic department manager who coordinates specialized economic analyses.
        For market-related questions, use the market_research tool.
        For financial questions, use the financial_analysis tool.
        Synthesize the results into a cohesive economic perspective.

        Important: Make sure to use both tools for comprehensive analysis unless the query is clearly focused on just one area.
        """,
        tools=[market_research, financial_analysis],
        callback_handler=None
    )
    return str(econ_manager(query))


# Level 3 - Specialized Analysis Agents
@tool
def market_research(query: str) -> str:
    """Analyze market trends and consumer behavior."""
    print("🔍 Market Research Specialist analyzing...")
    market_agent = Agent(
        system_prompt="You are a market research specialist who analyzes consumer trends, market segments, and purchasing behaviors. Provide detailed insights on market conditions, consumer preferences, and emerging trends.",
        callback_handler=None
    )
    return str(market_agent(query))

@tool
def financial_analysis(query: str) -> str:
    """Analyze financial aspects and economic implications."""
    print("💹 Financial Analyst processing...")
    financial_agent = Agent(
        system_prompt="You are a financial analyst who specializes in economic forecasting, cost-benefit analysis, and financial modeling. Provide insights on financial viability, economic impacts, and budgetary considerations.",
        callback_handler=None
    )
    return str(financial_agent(query))

@tool
def technical_analysis(query: str) -> str:
    """Analyze technical feasibility and implementation challenges."""
    print("⚙️ Technical Analyst evaluating...")
    tech_agent = Agent(
        system_prompt="You are a technology analyst who evaluates technical feasibility, implementation challenges, and emerging technologies. Provide detailed assessments of technical aspects, implementation requirements, and potential technological hurdles.",
        callback_handler=None
    )
    return str(tech_agent(query))

@tool
def social_analysis(query: str) -> str:
    """Analyze social impacts and behavioral implications."""
    print("👥 Social Impact Analyst investigating...")
    social_agent = Agent(
        system_prompt="You are a social impact analyst who focuses on how changes affect communities, behaviors, and social structures. Provide insights on social implications, behavioral changes, and community impacts.",
        callback_handler=None
    )
    return str(social_agent(query))


# Level 1 - Executive Coordinator
COORDINATOR_SYSTEM_PROMPT = """You are an executive coordinator who oversees complex analyses across multiple domains.
For economic questions, use the economic_department tool.
For technical questions, use the technical_analysis tool.
For social impact questions, use the social_analysis tool.
Synthesize all analyses into comprehensive executive summaries.

Your process should be:
1. Determine which domains are relevant to the query (economic, technical, social)
2. Collect analysis from each relevant domain using the appropriate tools
3. Synthesize the information into a cohesive executive summary
4. Present findings with clear structure and organization

Always consider multiple perspectives and provide balanced, well-rounded assessments.
"""

# Create the coordinator agent with all tools
coordinator = Agent(
    system_prompt=COORDINATOR_SYSTEM_PROMPT,
    tools=[economic_department, technical_analysis, social_analysis],
    callback_handler=event_loop_tracker
)

# Process a complex task through the hierarchical agent graph
def process_complex_task(task):
    """Process a complex task through the multi-level hierarchical agent graph"""
    return coordinator(f"Provide a comprehensive analysis of: {task}")

print(process_complex_task("Amazon").message)