from dotenv import load_dotenv
import streamlit as st

import os

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",

google_api_key=st.secrets["GOOGLE_API_KEY"]
    temperature=0.3
)

def generate_answer(query, docs):

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a professional assistant.

Answer ONLY from the provided context.

If the answer is not available in the context, say:
"I could not find this information in the document."

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return response.content