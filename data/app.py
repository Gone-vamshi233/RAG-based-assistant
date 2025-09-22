import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import os
import re

st.title("📚 RAG Assistant (Local)")

# Query preprocessing
def preprocess_query(query):
    query = query.lower()
    query = re.sub(r'[^\w\s]', '', query)
    query = re.sub(r'\s+', ' ', query).strip()
    return query

# Load documents
docs = []
doc_files = [f for f in os.listdir("data") if f.endswith(".txt")]
for file in doc_files:
    with open(os.path.join("data", file), "r", encoding="utf-8") as f:
        docs.append(f.read())

if not docs:
    st.warning("No text files found in data/ folder.")
else:
    # Chunk documents
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50
    all_chunks = []
    for doc in docs:
        start = 0
        while start < len(doc):
            end = start + CHUNK_SIZE
            all_chunks.append(doc[start:end])
            start += CHUNK_SIZE - CHUNK_OVERLAP

    # Load model & encode
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(all_chunks, convert_to_numpy=True)

    # Build FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    # User query
    query = st.text_input("Ask me a question about your documents:")
    if query:
        query = preprocess_query(query)
        query_emb = model.encode([query], convert_to_numpy=True)
        k = 3
        distances, indices = index.search(query_emb, k=k)
        answers = [all_chunks[i] for i in indices[0]]
        answer = "\n\n".join(answers)
        st.success(answer)
