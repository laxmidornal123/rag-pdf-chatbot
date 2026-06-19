from src.pdf_loader import load_pdf
from src.embeddings import create_vector_store

chunks = load_pdf("data/Sample.pdf")

db = create_vector_store(chunks)

db.save_local("vectorstore/faiss_index")

print("FAISS Vector Database Created Successfully!")