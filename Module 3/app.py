
import streamlit as st
import os
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
load_dotenv()

# Structured response
class AIResponse(BaseModel):
    answer: str = Field(description="Answer to the user's question")
    key_points: list[str] = Field(description="Important key points")

parser = PydanticOutputParser(pydantic_object=AIResponse)

# Page configuration
st.set_page_config(page_title="AI Chat Assistant")
st.title("🤖 AI Chat Assistant")

# Custom instructions
instructions = st.sidebar.text_area(
    "Custom Instructions",
    "You are a helpful AI assistant."
)

# Model parameters
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider("Max Tokens", 100, 2000, 500)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear chat
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Display previous conversations
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
query = st.chat_input("Ask something...")

if query:

    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    try:
        # Initialize LLM
        llm = ChatGroq(
            model="openai/gpt-oss-20b",
            temperature=temperature,
            max_tokens=max_tokens
        )

        # Prepare conversation history
        history = "\n".join(
            f"{m['role']}: {m['content']}"
            for m in st.session_state.messages
        )

        # Prompt template
        prompt = PromptTemplate(
            template="""
            {instructions}

            Conversation:
            {history}

            Respond to the latest user message.

            {format_instructions}
            """,
            input_variables=["instructions", "history"],
            partial_variables={
                "format_instructions": parser.get_format_instructions()
            }
        )

        # Create chain
        chain = prompt | llm | parser

        # Generate response
        with st.spinner("Thinking..."):
            result = chain.invoke({
                "instructions": instructions,
                "history": history
            })

        answer = result.answer

        # Display response
        with st.chat_message("assistant"):
            st.write(answer)
            st.write("### Key Points")
            for point in result.key_points:
                st.write("•", point)

        # Save response
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

        # Basic token usage estimate
        estimated_tokens = (
            len(history) + len(answer)
        ) // 4

        st.caption(
            f"Estimated tokens: {estimated_tokens}"
        )

    except Exception as e:
        st.error(f"Something went wrong: {e}")
