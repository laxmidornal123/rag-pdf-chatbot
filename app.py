import streamlit as st

from src.pdf_loader import load_pdf
from src.embeddings import create_vector_store
from src.retriever import load_retriever
from src.rag_chain import generate_answer

st.set_page_config(
    page_title="RAG PDF Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 RAG PDF Chatbot")
st.markdown("Ask questions from your PDF documents")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:

    st.header("📄 Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose PDF",
        type=["pdf"]
    )

    if uploaded_file:

        with open(
            f"data/{uploaded_file.name}",
            "wb"
        ) as f:

            f.write(
                uploaded_file.getbuffer()
            )

        with st.spinner(
            "Creating Vector Database..."
        ):

            chunks = load_pdf(
                f"data/{uploaded_file.name}"
            )

            db = create_vector_store(
                chunks
            )

            db.save_local(
                "vectorstore/faiss_index"
            )

        st.success(
            "PDF Processed Successfully"
        )

for msg in st.session_state.messages:

    with st.chat_message(
        msg["role"]
    ):
        st.markdown(
            msg["content"]
        )

query = st.chat_input(
    "Ask anything from PDF..."
)

if query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user"):
        st.markdown(query)

    retriever = load_retriever()

    docs = retriever.invoke(query)

    answer = generate_answer(
        query,
        docs
    )

    with st.chat_message(
        "assistant"
    ):
        st.markdown(answer)

        with st.expander(
            "📚 Sources"
        ):
            for doc in docs:
                st.write(
                    doc.page_content[:400]
                )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )