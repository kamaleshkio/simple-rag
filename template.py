import os

dir = [
    os.path.join("components")
]

files = [
    os.path.join("components", "load_pdf.py"),
    os.path.join("components", "split_docs.py"),
    os.path.join("components", "embede_model.py"),
    os.path.join("components", "vector_store.py"),
    os.path.join("components", "retrieval.py"),
    os.path.join("components", "llm_chain.py"),
    os.path.join("run_rag.py"),
    os.path.join("app.py")
]

for i in dir:
    os.makedirs(i, exist_ok=True)


for file in files:
    with open(file, 'w') as f:
        f.write("")