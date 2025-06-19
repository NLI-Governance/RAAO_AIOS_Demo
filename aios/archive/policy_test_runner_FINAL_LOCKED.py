import streamlit as st
st.set_page_config(page_title="AI Policy Test Runner", layout="wide")

import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools.query_policy_rag_helper import process_policy_query
from tools.load_benchmark_set import load_test_questions
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

@st.cache_resource
def load_index_and_docs():
    index_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'policies', 'faiss_index')
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    index = FAISS.load_local(index_path, embedding, allow_dangerous_deserialization=True)
    documents = list(index.docstore._dict.values())
    return index, documents

index, documents = load_index_and_docs()

st.title("📊 AI Policy Assistant Benchmark Test Runner")

if "run_triggered" not in st.session_state:
    st.session_state["run_triggered"] = False

if st.button("▶️ Run Benchmark Test"):
    st.session_state["run_triggered"] = True

if st.session_state["run_triggered"]:
    test_cases = load_test_questions(limit=25)
    results_log = []

    for test in test_cases:
        response = process_policy_query(test["question"], index, documents)
        results_log.append({
            "ID": test["id"],
            "Query": test["question"],
            "Method": response["method_used"],
            "Document": response.get("citation_info", [{}])[0].get("document", "N/A")
                if isinstance(response["citation_info"], list) else "N/A",
            "Lines": response.get("citation_info", [{}])[0].get("lines", "N/A")
                if isinstance(response["citation_info"], list) else "N/A",
            "Answer Preview": response["raw_answer"][:150] + "..."
                if len(response["raw_answer"]) > 150 else response["raw_answer"]
        })

    df = pd.DataFrame(results_log)

    st.subheader("📋 Benchmark Results")
    st.dataframe(df)

    scorecard = df["Method"].value_counts()
    st.subheader("📈 Method Summary")
    st.json(scorecard.to_dict())

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Export CSV", data=csv, file_name="benchmark_results.csv")

    json_data = df.to_json(orient="records", indent=2)
    st.download_button("📥 Export JSON", data=json_data, file_name="benchmark_results.json")
