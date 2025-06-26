from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_docs(docs, chunk_size = 1000, chunk_overlap = 20):
    splitter = RecursiveCharacterTextSplitter(chunk_size = chunk_size, chunk_overlap = chunk_overlap)
    return splitter.split_documents(docs)