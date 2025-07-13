from langchain.vectorstores import FAISS
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import os
import ollama

# For embedding and vector indexing
def create_faiss_index(text):
    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.create_documents([text])
    
    # Use Ollama's local embedding model (or fallback to fake vector for now)
    embeddings = OllamaEmbeddings(model='nomic-embed-text')  # or use 'mistral' if embeddings unsupported

    db = FAISS.from_documents(chunks, embeddings)
    return db

# For retrieving relevant context from stored vector index
def retrieve_context(db, query):
    docs = db.similarity_search(query, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])
    return context