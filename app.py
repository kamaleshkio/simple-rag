import streamlit as st
import tempfile
import os
from run_rag import run_rag_pipeline

st.set_page_config(page_title="LangSmith Monitored RAG", layout="wide")
st.title("📖 LangSmith-Enabled RAG Pipeline")

openai_api_key = st.sidebar.text_input("🔐 OpenRouter API Key", type="password")
model_name = st.sidebar.text_input("Model Name", value="mistralai/mistral-7b-instruct")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
query = st.text_input("Ask something from the PDF:")

if uploaded_file and query and openai_api_key:
    with st.spinner("Running RAG pipeline..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name

        try:
            answer = run_rag_pipeline(
                pdf_path=tmp_path,
                query=query,
                openai_api_key=openai_api_key,
                model_name=model_name
            )
            st.subheader("📌 Answer:")
            st.markdown(answer)
        except Exception as e:
            st.error(f"Error: {e}")
        finally:
            os.remove(tmp_path)
else:
    st.info("Upload a PDF, enter a query, and API key to start.")