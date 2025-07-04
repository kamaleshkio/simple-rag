import os 

from components.load_pdf import load_pdf
from components.split_docs import split_docs
from components.embede_model import get_embedding_model
from components.vector_store import creat_vectorstore
from components.retrieval import retrieve_docs
from components.llm_chain import get_llm_chain


from langsmith import traceable


@traceable(name = "rag-test")
def run_rag_pipeline(query, openai_api_key, model_name = "mistralai/mistral-7b-instruct" ):
    docs = load_pdf()#file or SQL configuration
    chunks = split_docs(docs)
    embedding_model = get_embedding_model()
    vectore_store = creat_vectorstore(chunks, embedding_model)
    retrieved = retrieve_docs(vectorstore=vectore_store, query=query)
    chain = get_llm_chain(openai_api_key, model_name=model_name)
    result = chain.invoke({"context": retrieved, "input": query})
    return result