from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from aios_secrets.openai_key import openai_api_key

def load_faiss_index(index_path):
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    return FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

def perform_query(query, faiss_index, top_k=3):
    results = faiss_index.similarity_search(query, k=top_k)
    return results

def load_synonym_expansions(synonyms_file):
    import json
    with open(synonyms_file, 'r', encoding='utf-8') as file:
        return json.load(file)
