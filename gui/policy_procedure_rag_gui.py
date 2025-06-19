import streamlit as st
import json
from datetime import datetime
import os
from language_toggle_component import language_toggle

# Use absolute path for reliability
base_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/policies/lookup_aids/")
fallback_path = os.path.join(base_path, "rag_fallback_topics.json")
log_path = os.path.join(base_path, "policy_query_log.json")

st.title("📘 AI Policy Assistant + GPT Fallback")
lang = language_toggle()

translations = {
    "en": {"prompt": "Ask a policy question:"},
    "es": {"prompt": "Haz una pregunta sobre política:"},
    "fr": {"prompt": "Posez une question sur la politique :"}
}

query = st.text_input(translations[lang]["prompt"])

if query:
    norm_query = query.lower().strip()
    with open(fallback_path, "r", encoding="utf-8") as f:
        fallback_data = json.load(f)

    match = fallback_data.get(norm_query)

    if match:
        st.success(match.get("note", "Policy match found."))
        st.markdown(f"**📘 Source:** `{match['document']}`")
        st.markdown(f"**📎 Section:** {match['section']}")
        method = "Fallback"
    else:
        st.warning("No structured match found.")
        gpt_response = st.text_area("💬 GPT Assistant Suggestion (simulated)",
                                    "This would be answered by GPT based on training data and RAG context.")
        match = {"document": "GPT", "section": "Inferred", "note": gpt_response}
        method = "GPT"

    log_entry = {
        "query": query,
        "method": method,
        "document": match["document"],
        "section": match["section"],
        "timestamp": datetime.now().isoformat()
    }
    try:
        with open(log_path, "r", encoding="utf-8") as lf:
            log_data = json.load(lf)
    except FileNotFoundError:
        log_data = []

    log_data.append(log_entry)
    with open(log_path, "w", encoding="utf-8") as lf:
        json.dump(log_data, lf, indent=2)
