import os
from dotenv import load_dotenv

load_dotenv()


import streamlit as st
import tempfile

from run_rag import get_llm_chain



api_key = os.environ["OPENROUTER_API_KEY"]

model_name = "mistralai/mistral-7b-instruct"

st.set_page_config(page_title="LangSmith Monitored RAG", layout="wide")
st.title("📖 LangSmith-Enabled RAG Pipeline")

query = st.text_input("Ask something from the PDF:")

if query:
    with st.spinner("Running RAG pipeline..."):

        try:
            answer = get_llm_chain(
                query=query,
                openai_api_key="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",
                model_name=model_name
            )
            st.subheader("📌 Answer:")
            st.markdown(answer)
        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.info("Please ask your query ")
