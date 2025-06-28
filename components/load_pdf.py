from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader

def load_pdf():#--> add path (path)
    #loader = PyPDFLoader("Bakthi.pdf")
    loader = WebBaseLoader("https://aws.amazon.com/what-is/retrieval-augmented-generation/")
    return loader.load()
