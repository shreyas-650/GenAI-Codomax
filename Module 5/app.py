from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

# 1. Create a tool
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

tools = [multiply]

# 2. Initialize LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

# 3. Create agent
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI agent. Use tools when needed."),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder("agent_scratchpad")
])

agent = create_tool_calling_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

# 4. Conversation memory
chat_history = []

while True:
    query = input("\nYou: ")
    if query.lower() == "exit":
        break
    response = agent_executor.invoke({
        "input": query,
        "chat_history": chat_history
    })

    print("\nAI Agent:", response["output"])
    chat_history.append(HumanMessage(content=query))
    chat_history.append(AIMessage(content=response["output"]))
