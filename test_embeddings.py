from langchain_community.embeddings import HuggingFaceEmbeddings
embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
print(embedder.embed_query("Test"))