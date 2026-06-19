from src.retriever import load_retriever

retriever = load_retriever()

query = "What are Laxmi Dornal's skills?"

docs = retriever.invoke(query)

print("\nRetrieved Chunks:\n")

for i, doc in enumerate(docs, 1):
    print(f"\nChunk {i}")
    print("-" * 50)
    print(doc.page_content[:500])