# Module 2: Prompt Engineering & AI Productivity

This module covers hands-on prompt engineering techniques and productivity workflows using **LangChain** and **Groq** (`ChatGroq`).

---

## 📌 Contents & Key Concepts

The notebook [`Prompt Engineering & AI Productivity.ipynb`](file:///f:/Intership/GenAI-Codomax/Module%202/Prompt%20Engineering%20%26%20AI%20Productivity.ipynb) explores the following topics:

1. **Prompt Engineering Strategies (Zero-Shot & Few-Shot)**
   - Creating prompt templates using `PromptTemplate`.
   - Running Zero-Shot prompts to produce concise answers (word-constrained responses).
   - Implementing Few-Shot prompting with demonstration examples to guide tone, structure, and output consistency.
   - Building prompt chains with `StrOutputParser` and Groq LLMs (`openai/gpt-oss-20b`).

2. **Structured Outputs with Pydantic**
   - Defining rigid output schemas using Pydantic's `BaseModel` and `Field`.
   - Formatting and parsing responses directly into structured objects via `PydanticOutputParser`.
   - Parsing complex multi-field responses (e.g., material requirements, product descriptions).

3. **Task-Specific Code Assistant Prompts**
   - Configuring an expert developer persona.
   - Testing code generation, debugging (e.g., handling runtime errors like `ZeroDivisionError`), and explaining core programming concepts.

4. **Productivity AI Assistants**
   - Developing a reusable `ai_tool(task, query)` pipeline.
   - Applying LLM automation to common professional workflows:
     - **Summarization**: Condensing technical articles and topics.
     - **Email Writing**: Drafting formal emails and workplace requests.
     - **Resume Improvement**: Tailoring skills, metrics, and bullet points.
     - **Code Generation**: Writing standalone, production-ready Python functions.
     - **Research & Analysis**: Synthesizing domain overviews and use-cases.

---

## ⚙️ Prerequisites & Setup

### 1. Environment Setup

Create and activate a Python virtual environment (recommended Python 3.10+):

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 2. Install Dependencies

Install the required packages using the provided [`requirements.txt`](file:///f:/Intership/GenAI-Codomax/Module%202/requirements.txt):

```bash
pip install -r requirements.txt
```

### 3. API Key Configuration

Create a `.env` file in the `Module 2` directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🚀 Running the Notebook

Start Jupyter Notebook or Jupyter Lab:

```bash
jupyter notebook "Prompt Engineering & AI Productivity.ipynb"
```

Run each cell sequentially to inspect the output chains, structured parses, and generated productivity responses.
