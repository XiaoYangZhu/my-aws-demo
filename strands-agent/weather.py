# weather.py

from typing import Any
from strands.types.tools import ToolResult, ToolUse

TOOL_SPEC = {
    "name": "weather",
    "description": "Get weather information for a location",
    "inputSchema": {
        "json": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City or location name"
                }
            },
            "required": ["location"]
        }
    }
}

# Function name must match tool name
def weather(tool: ToolUse, **kwargs: Any) -> ToolResult:
    tool_use_id = tool["toolUseId"]
    location = tool["input"]["location"]

    # Implement weather lookup logic here
    weather_info = f"Weather for {location}: Sunny, 72°F"

    return {
        "toolUseId": tool_use_id,
        "status": "success",
        "content": [{"text": weather_info}]
    }