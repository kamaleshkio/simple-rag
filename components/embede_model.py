from langchain_huggingface import HuggingFaceEmbeddings

def get_embedding_model():
    return HuggingFaceEmbeddings(
        model_name = "sentence-transformers/all-mpnet-base-v2",
        model_kwargs = {"device": "cpu"},
        encode_kwargs = {"normalize_embeddings": False}
    )