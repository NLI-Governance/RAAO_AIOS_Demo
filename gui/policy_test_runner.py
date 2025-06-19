import streamlit as st
import pandas as pd
import sys
from pathlib import Path

# Append parent directory for proper imports
sys.path.append(str(Path(__file__).resolve().parent.parent))

from query_policy_rag_helper import query_policy_with_synonyms

def main():
    st.title("AI Policy Assistant – Benchmark Test")

    uploaded_file = st.file_uploader("Upload Benchmark CSV", type="csv")

    if uploaded_file:
        questions_df = pd.read_csv(uploaded_file)

        results = []
        index_path = "../data/policies/policy_faiss_index"
        synonyms_file = "../data/policies/lookup_aids/synonym_context_expander.json"

        for question in questions_df["Question"]:
            answer = query_policy_with_synonyms(question, index_path, synonyms_file)
            results.append({"Question": question, "Answer": answer})

        results_df = pd.DataFrame(results)
        st.write(results_df)

if __name__ == "__main__":
    main()
