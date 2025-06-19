import sys
from pathlib import Path

# Add project root to Python path for module resolution
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

import streamlit as st
from gui.components.language_toggle_component import render_language_toggle

# Display the RAAO logo with white background
st.markdown(
    """
    <div style='background-color:white; padding:10px; text-align:center'>
        <img src='logo.png' width='180'/>
    </div>
    """,
    unsafe_allow_html=True
)

# Language selection UI
st.sidebar.header("🌐 Language Selection")
language = render_language_toggle()

# Display confirmation in selected language
messages = {
    "en": "✅ Language set to: ",
    "es": "✅ Idioma seleccionado: ",
    "fr": "✅ Langue définie sur : "
}
st.success(messages.get(language, "✅ Language set to: ") + language)
