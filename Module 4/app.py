import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# 1. Load PDF
loader = PyPDFLoader("document.pdf")
docs = loader.load()

# 2. Split documents
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs)

# 3. Create embeddings and vector database
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = FAISS.from_documents(chunks, embeddings)
retriever = vector_db.as_retriever(search_kwargs={"k": 3})

# 4. Initialize LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

prompt = ChatPromptTemplate.from_template("""
Answer the question using only the given context.

Context:
{context}

Question:
{question}
""")

chain = prompt | llm

# 5. Ask questions
while True:
    query = input("\nAsk a question (exit to stop): ")

    if query.lower() == "exit":
        break

    results = retriever.invoke(query)
    context = "\n".join(doc.page_content for doc in results)

    response = chain.invoke({
        "context": context,
        "question": query
    })

    print("\nAnswer:", response.content)
