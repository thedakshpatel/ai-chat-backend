# services/vector_store.py
import chromadb
from sentence_transformers import SentenceTransformer

# Initialize ChromaDB client and collection
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection("agent_knowledge")

# Use SentenceTransformer to convert text into embeddings
encoder = SentenceTransformer("all-MiniLM-L6-v2")

def add_knowledge(id, content):
    embedding = encoder.encode([content])[0].tolist()
    collection.add(documents=[content], ids=[id], embeddings=[embedding])

def search_knowledge(query, top_k=1):
    query_embedding = encoder.encode([query])[0].tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    return results['documents'][0] if results['documents'] else []
