import streamlit as st
import json
from datetime import datetime
import os
from language_toggle_component import language_toggle

base_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/policies/lookup_aids/")
fallback_path = os.path.join(base_path, "rag_fallback_topics.json")
log_path = os.path.join(base_path, "policy_query_log.json")

st.title("📘 AI Policy Assistant + GPT Fallback")
lang = language_toggle()

translations = {
    "en": {
        "prompt": "Ask a policy question:",
        "info_normal": "Ask a clear policy question. If matched, a source citation will appear below.",
        "info_gpt": "No official policy citation was found. Try rephrasing for better results, or continue exploring with our AI assistant."
    },
    "es": {
        "prompt": "Haz una pregunta sobre política:",
        "info_normal": "Haz una pregunta clara sobre política. Si coincide, verás una cita de origen abajo.",
        "info_gpt": "No se encontró una cita oficial. Intenta reformular tu pregunta o explora con nuestro asistente de IA."
    },
    "fr": {
        "prompt": "Posez une question sur la politique :",
        "info_normal": "Posez une question claire. Si une correspondance est trouvée, une citation apparaîtra.",
        "info_gpt": "Aucune citation officielle trouvée. Essayez de reformuler ou explorez avec notre assistant IA."
    }
}

icon_text = translations[lang]["info_normal"]
query = st.text_input(f"{translations[lang]['prompt']} 🛈", help=icon_text)

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
        icon_text = translations[lang]["info_normal"]
    else:
        st.warning("No structured match found.")
        st.markdown(
            """
<div style='background-color:#262730;padding:1rem;border-radius:0.5rem;margin-top:1rem;'>
<b>GPT Assistant Suggestion (simulated)</b><br>
<em>This would be answered by GPT based on training data and RAG context.</em>
</div>
""",
            unsafe_allow_html=True
        )
        match = {"document": "GPT", "section": "Inferred", "note": "GPT placeholder"}
        method = "GPT"
        icon_text = translations[lang]["info_gpt"]

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
