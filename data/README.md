# 📚 RAG Assistant – AAIDC Module 1

This project is part of the **Agentic AI Developer Certification (AAIDC) Module 1**.  
It demonstrates how to build a **Retrieval-Augmented Generation (RAG) Assistant**, which combines document retrieval with natural language generation to answer user queries reliably and contextually.

## Overview

The RAG Assistant loads documents from a folder, splits them into chunks, converts them into embeddings, stores them in a vector database, and answers user queries by combining retrieved knowledge with generative AI.  
This architecture reduces hallucinations, improves reliability, and demonstrates how retrieval plus generation enhances AI assistant capabilities.

## Features

- Load `.txt` documents from a `data/` folder
- Split documents into chunks for efficient processing
- Generate embeddings using **OpenAI Embeddings**
- Store embeddings in **Chroma** vector database
- Retrieve relevant document chunks for each query
- Generate answers using a **large language model (LLM)**
- User-friendly web interface built with **Streamlit**
- Modular design allows swapping embeddings or vector databases
- Accurate, context-aware responses grounded in documents

## Tools & Technologies

- **Python** – main programming language
- **Streamlit** – web interface
- **LangChain** – orchestration of retrieval and generation
- **OpenAI Embeddings** – for converting text into vectors
- **Chroma** – vector database for embedding storage and retrieval
- **FAISS** (optional for local embeddings) – alternative vector search

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Gone-vamshi233/RAG-based-assistant.git
cd rag-assistant

2. Install dependencies:
pip install -r requirements.txt
