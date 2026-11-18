
import streamlit as st
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

# Structured response
class InterviewResponse(BaseModel):
    feedback: str = Field(description="Feedback on the candidate's answer")
    score: int = Field(description="Score out of 10")
    ideal_answer: str = Field(description="Suggested ideal answer")
    next_question: str = Field(description="Next interview question")


parser = PydanticOutputParser(pydantic_object=InterviewResponse)

# Page configuration
st.set_page_config(page_title="AI Interview Assistant")
st.title("🎯 AI Interview Assistant")
st.write("Practice interviews and improve your skills with AI.")

# Sidebar settings
st.sidebar.header("Interview Settings")

role = st.sidebar.selectbox(
    "Select Job Role",
    ["Python Developer", "AI Engineer", "Data Scientist",
     "Java Developer", "GenAI Developer"]
)

level = st.sidebar.selectbox(
    "Experience Level",
    ["Fresher", "Intermediate", "Experienced"]
)

interview_type = st.sidebar.selectbox(
    "Interview Type",
    ["Technical", "HR", "Coding", "Mixed"]
)

temperature = st.sidebar.slider(
    "Temperature", 0.0, 1.0, 0.7
)

max_tokens = st.sidebar.slider(
    "Max Tokens", 100, 2000, 700
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear interview
if st.sidebar.button("Restart Interview"):
    st.session_state.messages = []
    st.rerun()

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Start interview
if not st.session_state.messages:
    if st.button("Start Interview"):
        st.session_state.messages.append({
            "role": "user",
            "content": "Start the interview. Ask me the first question."
        })
        st.rerun()

# User answer
query = st.chat_input("Enter your interview answer...")

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

        # Conversation history
        history = "\n".join(
            f"{m['role']}: {m['content']}"
            for m in st.session_state.messages
        )

        # Interview prompt
        prompt = PromptTemplate(
            template="""
            You are a professional AI Interviewer.

            Candidate Job Role: {role}
            Experience Level: {level}
            Interview Type: {interview_type}

            Conversation History:
            {history}

            Instructions:
            1. Conduct a professional interview.
            2. Ask questions according to the selected job role.
            3. Evaluate the candidate's latest answer.
            4. Give constructive feedback.
            5. Give a score out of 10.
            6. Provide an ideal answer for improvement.
            7. Ask one relevant next interview question.
            8. If the interview is just starting, welcome the
               candidate and ask the first question.
            9. Keep responses clear and concise.

            {format_instructions}
            """,
            input_variables=[
                "role", "level", "interview_type", "history"
            ],
            partial_variables={
                "format_instructions": parser.get_format_instructions()
            }
        )

        # Create chain
        chain = prompt | llm | parser

        # Generate response
        with st.spinner("Interviewer is thinking..."):
            result = chain.invoke({
                "role": role,
                "level": level,
                "interview_type": interview_type,
                "history": history
            })

        # Display feedback
        with st.chat_message("assistant"):

            st.subheader("📝 Interview Feedback")
            st.write(result.feedback)

            st.metric("Your Score", f"{result.score}/10")

            with st.expander("View Ideal Answer"):
                st.write(result.ideal_answer)

            st.subheader("❓ Next Interview Question")
            st.write(result.next_question)

        # Save assistant response
        response = f"""
        **Feedback:** {result.feedback}

        **Score:** {result.score}/10

        **Ideal Answer:** {result.ideal_answer}

        **Next Question:** {result.next_question}
        """

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

    except Exception as e:
        st.error(f"Something went wrong: {e}")
