# Retrieval-Augmented Generation (RAG) Assistant  

🚀 A fact-based assistant that combines **document retrieval** with **natural language generation** to produce accurate and context-aware responses.  

This project is part of the **Agentic AI Developer Certification (AAIDC) – Module 1**.  

---

## 📌 Overview  

Large Language Models (LLMs) are powerful but prone to hallucinations. The **RAG Assistant** addresses this by grounding responses in retrieved documents, ensuring reliability and factual accuracy.  

The system ingests documents, chunks them into smaller sections, generates embeddings, stores them in a vector database, and retrieves the most relevant context at query time. The retrieved information is then passed to an LLM (e.g., GPT-3.5) to generate accurate, natural-sounding answers.  

---

## ⚙️ Architecture  

**Workflow:**  
1. **Document Loading** – Load `.txt` documents from a folder.  
2. **Chunking** – Split documents into smaller chunks with overlap.  
3. **Embedding Generation** – Convert chunks into embeddings using **OpenAI Embeddings**.  
4. **Vector Database** – Store embeddings in **Chroma** for similarity search.  
5. **Retrieval** – Retrieve top-k relevant chunks for a query.  
6. **Response Generation** – Pass retrieved context to **GPT-3.5** via **LangChain** to generate answers.  

**Tech Stack:**  
- **LangChain** – Orchestrates RAG pipeline  
- **OpenAI Embeddings** – Vector representation  
- **Chroma** – Vector database  
- **Streamlit** – User-friendly interface  

---

## 📦 Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/gone-vamshi233/rag-assistant.git
   cd rag-assistant
2.Create a virtual environment and activate it:
   ```bash
    python -m venv venv
    source venv/bin/activate   # macOS/Linux
    venv\Scripts\activate      # Windows
3. Install dependencies:
   ```bash
 pip install -r requirements.txt
4.Add your OpenAI API key to a .env file:
   ```bash
   OPENAI_API_KEY=your_api_key_here
**usage:**
Place your documents (.txt) inside the data/ folder.

Run the Streamlit app:
```bash
streamlit run app.py

Open the local URL in your browser and start querying the assistant.
