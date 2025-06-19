from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from aios_secrets.openai_key import openai_api_key

def load_faiss_index(index_path):
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    faiss_index = FAISS.load_local(
        index_path, 
        embeddings, 
        allow_dangerous_deserialization=True
    )
    return faiss_index
