import streamlit as st
import tempfile
import os
from run_rag import run_rag_pipeline

from dotenv import load_dotenv

api_key = os.environ["OPENROUTER_API_KEY"]

model_name = "mistralai/mistral-7b-instruct"

st.set_page_config(page_title="LangSmith Monitored RAG", layout="wide")
st.title("📖 LangSmith-Enabled RAG Pipeline")

query = st.text_input("Ask something from the PDF:")

if query:
    with st.spinner("Running RAG pipeline..."):

        try:
            answer = run_rag_pipeline(
                pdf_path="components/Bakthi.pdf",
                query=query,
                openai_api_key=api_key,
                model_name=model_name
            )
            st.subheader("📌 Answer:")
            st.markdown(answer)
        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.info("Please ask your query ")