# Module 4: Retrieval-Augmented Generation (RAG) with FAISS & LangChain

This module implements a Retrieval-Augmented Generation (RAG) question-answering CLI pipeline over PDF documents using **LangChain**, **HuggingFace Embeddings**, **FAISS Vector Store**, and **Groq** (`ChatGroq`).

---

## 📌 Architecture & Features

- **Document Ingestion**: Extracts text from PDF files using `PyPDFLoader`.
- **Text Chunking**: Splits large documents into semantically coherent overlapping segments using `RecursiveCharacterTextSplitter` (chunk size: 500 characters, overlap: 50 characters).
- **Dense Vector Embeddings**: Uses HuggingFace's `sentence-transformers/all-MiniLM-L6-v2` for dense semantic representations.
- **Vector Search**: Indexes chunks in a fast local `FAISS` vector database to retrieve the top 3 relevant passages per query.
- **Grounded Q&A Generation**: Leverages `ChatGroq` (`openai/gpt-oss-20b`) with a strict context constraint to answer questions exclusively using retrieved information.
- **Interactive CLI Loop**: Continuous command-line query interface with session exit control.

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

Install the required packages using [`requirements.txt`](file:///f:/Intership/GenAI-Codomax/Module%204/requirements.txt):

```bash
pip install -r requirements.txt
```

### 3. API Key Configuration

Create or update the `.env` file in the `Module 4` directory with your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Provide Source Document

Ensure your source PDF document is named `document.pdf` and placed directly inside the `Module 4` directory (a sample [`document.pdf`](file:///f:/Intership/GenAI-Codomax/Module%204/document.pdf) is already included).

---

## 🚀 Running the Application

Run the RAG QA script:

```bash
python app.py
```

### Usage:
1. Wait for embeddings generation and vector store indexing to complete.
2. Enter your question at the prompt:
   ```text
   Ask a question (exit to stop):
   ```
3. Type `exit` to quit the interactive session.

---

## 📁 File Structure

```text
Module 4/
├── .env                # Environment variables (GROQ_API_KEY)
├── app.py              # RAG pipeline implementation
├── document.pdf        # Target source PDF document
├── README.md           # Module documentation
└── requirements.txt    # Project dependencies
```
