import streamlit as st
from query_policy_rag_helper import query_policy_with_synonyms
from secrets.openai_key import openai_api_key

st.set_page_config(page_title="📘 AI Policy Assistant + GPT Fallback", layout="wide")

st.title("📘 AI Policy Assistant + GPT Fallback")
st.markdown("Ask a policy question:")

query = st.text_input(" ", placeholder="e.g. Can I bring my pet to work?")

if query:
    with st.spinner("Searching policies..."):
        result = query_policy_with_synonyms(query)

    if result.get("type") == "structured":
        st.success("✅ Structured policy match found:")
        st.markdown(result["answer"])
        st.caption(f"Source: {result['source']}")
    elif result.get("type") == "fallback":
        st.warning("⚠️ No structured match found.")
        st.markdown(f"**GPT Assistant Suggestion (simulated)**\n\n{result['answer']}")
    elif result.get("type") == "error":
        st.error(f"GPT fallback failed. {result['message']}")

# 🛈 Info icon (updated dynamically)
with st.expander("🛈 What should I ask?"):
    st.markdown("""
    You can ask about workplace policies in natural language.  
    If no exact match is found, the assistant will suggest a response using GPT logic.  
    Tip: Try rephrasing if your question seems unclear or long-winded.
    """)
