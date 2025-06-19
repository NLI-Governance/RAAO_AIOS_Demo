import streamlit as st
import os
import sys

# Allow imports from sibling tools/ directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

st.set_page_config(page_title="🧠 Vector Match Debugger", layout="wide")
st.title("🧠 Test Vector Match Against FAISS Index")

# Load FAISS index
@st.cache_resource
def load_index():
    index_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'policies', 'faiss_index')
    index = FAISS.load_local(index_path, OpenAIEmbeddings(), allow_dangerous_deserialization=True)
    return index

index = load_index()

# User input
user_query = st.text_input("Enter a test query to check against the policy vector index:")
score_threshold = st.slider("Minimum score to consider as match", 0.0, 1.0, 0.75, 0.01)
top_k = st.slider("How many top results to show", 1, 10, 3)

if st.button("🔍 Search Vector Index") and user_query.strip():
    try:
        results = index.similarity_search_with_score(user_query, k=top_k)

        if not results:
            st.warning("No results returned.")
        else:
            for i, (doc, score) in enumerate(results, start=1):
                if score < score_threshold:
                    continue

                st.markdown(f"### 🔹 Match {i}")
                st.markdown(f"**Score:** `{round(score, 4)}`")
                st.markdown(f"**Document:** `{doc.metadata.get('source', 'Unknown')}`")
                st.markdown(f"**Section:** `{doc.metadata.get('section', 'Unspecified')}`")
                st.markdown(f"**Lines:** `{doc.metadata.get('lines', 'N/A')}`")
                st.code(doc.page_content)

    except Exception as e:
        st.error(f"Error during FAISS search: {str(e)}")
