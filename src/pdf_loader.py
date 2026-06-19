from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_pdf(pdf_path):
    print("Loading PDF...")

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    print("Pages loaded:", len(docs))

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    print("Chunks created:", len(chunks))

    return chunks