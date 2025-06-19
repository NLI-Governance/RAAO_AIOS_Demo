import streamlit as st

def render_language_toggle(current_language="English"):
    languages = ["English", "Spanish", "French"]
    selected_language = st.selectbox(
        "🌐 Language",
        languages,
        index=languages.index(current_language),
        key="language_toggle",
        label_visibility="collapsed"  # Keeps it compact and minimal
    )
    return selected_language
