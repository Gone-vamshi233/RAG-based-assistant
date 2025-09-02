import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import os

# App title
st.title("📚 RAG Assistant (Local)")

# Load documents from data/ folder
docs = []
doc_files = [f for f in os.listdir("docs") if f.endswith(".txt")]

for file in doc_files:
    with open(os.path.join("docs", file), "r", encoding="utf-8") as f:
        docs.append(f.read())

# Check if we have documents
if not docs:
    st.warning("No text files found in data/ folder.")
else:
    # Load local embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Create embeddings for documents
    embeddings = model.encode(docs, convert_to_numpy=True)

    # Build FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    # Input box for user question
    query = st.text_input("Ask me a question about your documents:")

    if query:
        query_emb = model.encode([query], convert_to_numpy=True)
        distances, indices = index.search(query_emb, k=1)
        answer = docs[indices[0][0]]
        st.success(answer)
