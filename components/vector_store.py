from langchain_community.vectorstores import Chroma

def creat_vectorstore(docs, embeddings, presist_dir = "chrome_db"):
    return Chroma.from_documents(docs, embeddings, presist_dir=presist_dir)