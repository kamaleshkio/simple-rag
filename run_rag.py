import os
import streamlit as st
from run_rag import run_rag_pipeline

# Load environment variables from .env (e.g. OPENROUTER_API_KEY)
from dotenv import load_dotenv
load_dotenv()

# Set Streamlit config directory (for metrics, etc.)
streamlit_config_dir = "/app/.streamlit"
os.environ["STREAMLIT_CONFIG_DIR"] = streamlit_config_dir
os.makedirs(streamlit_config_dir, exist_ok=True)

# Predefined settings
API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = "mistralai/mistral-7b-instruct"
PDF_PATH = "components/Bakthi.pdf"

# Streamlit UI setup
st.set_page_config(page_title="RAG Q&A App", layout="wide")
st.title("📘 RAG Q&A using OpenRouter + Langchain")

query = st.text_input("Ask a question based on the PDF:")

if query:
    with st.spinner("Generating answer..."):
        try:
            answer = run_rag_pipeline(
                pdf_path=PDF_PATH,
                query=query,
                openai_api_key=API_KEY,
                model_name=MODEL_NAME
            )
            st.subheader("🧠 Answer:")
            st.markdown(answer)
        except Exception as e:
            st.error(f"❌ Error: {e}")
else:
    st.info("Please enter your question above.")
