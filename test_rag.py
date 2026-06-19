from src.retriever import load_retriever
from src.rag_chain import generate_answer

retriever = load_retriever()

question = input("Ask a question: ")

docs = retriever.invoke(question)

answer = generate_answer(
    question,
    docs
)

print("\nAnswer:\n")
print(answer)