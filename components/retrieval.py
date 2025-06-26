def retrieve_docs(vectorstore, query):
    return vectorstore.similarity_search(query)

