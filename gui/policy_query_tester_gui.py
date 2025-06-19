import streamlit as st
import json

alias_path = "../data/policies/lookup_aids/keyword_alias_dictionary.json"
synonym_path = "../data/policies/lookup_aids/synonym_context_expander.json"
fallback_path = "../data/policies/lookup_aids/rag_fallback_topics.json"

st.title("🧪 Policy Query Tester")
query = st.text_input("Enter a test query:")

if query:
    norm = query.lower().strip()

    with open(alias_path, "r") as f:
        aliases = json.load(f)
    with open(synonym_path, "r") as f:
        synonyms = json.load(f)
    with open(fallback_path, "r") as f:
        fallbacks = json.load(f)

    alias_hit = any(alias in norm for alias in aliases)
    synonym_hit = any(syn in norm for syn in synonyms)
    fallback_hit = norm in fallbacks

    if fallback_hit:
        match = fallbacks[norm]
        st.success("📄 Fallback match found.")
        st.json(match)
    elif alias_hit or synonym_hit:
        st.info(f"Match type: {'Alias' if alias_hit else ''} {'Synonym' if synonym_hit else ''}")
    else:
        st.warning("No match — will require GPT/vector fallback.")
