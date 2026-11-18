# Module 5: Tool-Calling AI Agents with LangChain & Groq

This module demonstrates building an autonomous, tool-calling conversational agent using **LangChain**, **Groq** (`ChatGroq`), and custom Python functions decorated with `@tool`.

---

## 📌 Architecture & Features

- **Custom Python Tools**: Uses LangChain's `@tool` decorator to define callable functions (e.g., `multiply(a, b)`) with typed signatures and docstrings for the LLM to inspect.
- **Tool-Calling Agent**: Constructed with `create_tool_calling_agent` using `ChatGroq` (`openai/gpt-oss-20b`) for fast decision-making and execution.
- **Agent Scratchpad & Reasoning**: Employs `AgentExecutor` with `verbose=True` to trace thought steps, tool invocations, and parameter selections.
- **Conversational Memory**: Maintains stateful multi-turn history using `HumanMessage` and `AIMessage` objects passed via `MessagesPlaceholder("chat_history")`.
- **Interactive CLI Loop**: Conversational shell interface to test tool delegation and follow-up queries interactively.

---

## ⚙️ Prerequisites & Setup

### 1. Environment Setup

Create and activate a Python virtual environment (Python 3.10+ recommended):

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 2. Install Dependencies

Install the required packages using [`requirements.txt`](file:///f:/Intership/GenAI-Codomax/Module%205/requirements.txt):

```bash
pip install -r requirements.txt
```

### 3. API Key Configuration

Create or update the `.env` file in the `Module 5` directory with your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🚀 Running the Application

Launch the AI Agent CLI:

```bash
python app.py
```

### Example Usage:
```text
You: Multiply 42 and 78

> Entering new AgentExecutor chain...
Invoking: `multiply` with `{'a': 42, 'b': 78}`
3276
AI Agent: 42 multiplied by 78 is 3276.

You: exit
```

---

## 📁 File Structure

```text
Module 5/
├── .env                # Environment variables (GROQ_API_KEY)
├── app.py              # Tool-calling agent implementation
├── README.md           # Module documentation
└── requirements.txt    # Project dependencies
```
