from typing import Dict, Callable
from google import genai

class ToolRegistry:
    def __init__(self):
        self._tools: Dict[str, Dict] = {}

    def register(self, tool):
    
        self._tools[tool.name()] = {
            "name": tool.name(),
            "description": tool.description(),
            "parameters": tool.get_declaration()["parameters"],
            "callable": tool.execute
        }

    def get_tool(self, name):
        entry = self._tools.get(name)
        return entry["callable"] if entry else None

    def get_declarations(self):
        tools_list = []
        for entry in self._tools.values():
            tools_list.append(
                genai.Tool(
                    name=entry["name"],
                    description=entry["description"],
                    parameters=entry["parameters"],
                    callable=entry["callable"]
                )
            )
        return tools_list