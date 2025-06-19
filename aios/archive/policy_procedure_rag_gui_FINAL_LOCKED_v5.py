import streamlit as st
import os
import sys
import json

# ✅ Fix: Add the /tools/ and /aios_secrets/ folders to sys.path
current_dir = os.path.dirname(__file__)
base_dir = os.path.abspath(os.path.join(current_dir, ".."))
tools_dir = os.path.join(base_dir, "tools")
secrets_dir = os.path.join(base_dir, "aios_secrets")

for path in [tools_dir, secrets_dir]:
    if path not in sys.path:
        sys.path.insert(0, path)

from query_policy_rag_helper import query_policy_with_synonyms

st.title("📘 AI Policy Assistant + GPT Fallback")

language = st.selectbox("🌐 Select Language", ["English"])

user_question = st.text_input("Ask a policy question:")

if user_question:
    try:
        result = query_policy_with_synonyms(user_question)

        st.markdown("### Normalized & Expanded Query")
        st.code(result, language="json")

        if isinstance(result, dict) and result.get("status") == "match":
            st.success(result["answer"])
        elif isinstance(result, dict) and result.get("status") == "gpt":
            st.info(result["answer"])
        else:
            st.warning("Unstructured answer: no formal policy matched.")
    except Exception as e:
        st.error(f"❌ Unexpected error occurred:\n\n{e}")
