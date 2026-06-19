import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

PDF_PATH = "data/sample.pdf"

FAISS_PATH = "vectorstore/faiss_index"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"