# AI Personal Assistant Agent

A modular AI agent built using Python and Google Gemini API. This agent can maintain conversation history, reason about user requests, and call external tools autonomously.

---

## Features

* **Natural Language Interface** – interact with the agent via CLI.
* **Contextual Memory** – remembers previous conversation turns.
* **Tool Integration** – supports multiple tools:

  * Calculator
  * Current Time
  * Weather
  * Translator (custom)
  * File Reader (custom)
* **Adaptive Execution** – decides whether to answer directly or call a tool.
* **Robust Error Handling** – handles invalid input, unknown tools, and API errors gracefully.

---

## Architecture

The project follows **SOLID principles** and uses **design patterns**:

* **Strategy Pattern** – tools are interchangeable and selected dynamically.
* **Factory / Registry Pattern** – tools are registered and managed via a central registry.
* **ReAct Loop (Reason → Act → Observe)** – main execution loop for agent decisions.
* **Observer Pattern (Optional)** – can track tool usage or update UI without coupling.

**Core Components:**

| Component       | Responsibility                                              |
| --------------- | ----------------------------------------------------------- |
| `Agent`         | Orchestrates the ReAct loop and executes user queries       |
| `MemoryManager` | Stores conversation history for context                     |
| `ToolRegistry`  | Manages available tools and their execution                 |
| `BaseTool`      | Abstract class/interface for all tools                      |
| `Tools`         | Individual tool implementations (calculator, weather, etc.) |

---

## Installation

1. **Set up Python environment**:

```bash
python -m venv venv
source venv/bin/activate   # macOS
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Set your Google Gemini API key**:

```bash
export GEMINI_API_KEY="your_api_key"  
```

---

## Usage

Run the agent in the terminal:

```bash
python main.py
```

Example conversation:

```bash
You: What is 5 * 8?
Agent: 40

You: What time is it?
Agent: 14:23:01

You: Translate "Hello" to Spanish
Agent: Hola
```

Type `exit` to quit the program.

---

## Project Structure

```bash
ai-agent/
├── agent.py          # Main agent logic (ReAct loop)
├── memory_manager.py # Stores conversation history
├── tools/
│   ├── base_tool.py  # Base class/interface for tools
│   ├── calculator.py
│   ├── time_tool.py
│   ├── weather_tool.py
│   ├── translate_tool.py
│   └── file_reader.py
├── tool_registry.py  # Registers and executes tools
├── main.py           # Entry point for CLI
├── config.py         # API key and settings
├── requirements.txt  # Dependencies
└── README.md         # Project documentation
```

---

## Notes

* Currently, free-tier API users may hit **quota limits**.
* For testing without the API, you can enable **mock mode** in `agent.py`.
* Adding a new tool is easy: inherit from `BaseTool` and register it in `ToolRegistry`.

---

