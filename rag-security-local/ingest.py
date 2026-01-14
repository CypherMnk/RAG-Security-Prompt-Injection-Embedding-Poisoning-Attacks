import os
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

docs = []

for folder in ["clean_docs", "poisoned_docs"]:
    folder_path = os.path.join("data", folder)
    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(folder_path, file))
            docs.extend(loader.load())

embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectordb = Chroma.from_documents(
    documents=docs,
    embedding=embedding,
    persist_directory="vectorstore"
)

vectordb.persist()
print("✅ Clean + Poisoned documents stored in vector DB")
