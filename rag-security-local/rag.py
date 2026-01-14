from langchain_community.llms import Ollama
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

vectordb = Chroma(
    persist_directory="vectorstore",
    embedding_function=embedding
)

llm = Ollama(model="llama3.2:3b")

query = input("Enter your question: ")

docs = vectordb.similarity_search(query, k=4)
context = "\n".join([doc.page_content for doc in docs])

prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{query}
"""

response = llm.invoke(prompt)
print("\n🟢 Answer:\n", response)
