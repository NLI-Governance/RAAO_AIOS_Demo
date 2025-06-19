import streamlit as st

def language_toggle():
    languages = {
        "en": "English",
        "es": "Español",
        "fr": "Français"
    }
    choice = st.sidebar.selectbox("🌐 Select Language", options=list(languages.keys()), format_func=lambda x: languages[x])
    st.session_state["preferred_language"] = choice
    return choice
