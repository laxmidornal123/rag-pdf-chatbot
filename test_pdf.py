from src.pdf_loader import load_pdf

chunks = load_pdf("data/Sample.pdf")

print("Chunks:", len(chunks))

if len(chunks) > 0:
    print("\nFirst Chunk:\n")
    print(chunks[0].page_content[:500])