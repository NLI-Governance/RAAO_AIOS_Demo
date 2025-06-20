import streamlit as st
from components.shared_ui_components import display_logo, display_abl_footer

st.set_page_config(page_title="AIOS Module", layout="wide")
display_logo()

st.selectbox("🌐 Language", ["English", "Español", "Français"])

with st.expander("About this form"):
    st.markdown("This form is part of the Adaptive Integrated Operations System (AIOS). It supports employee workflows at Rising Against All Odds. Please complete all required fields and submit to your supervisor or system administrator.")

st.markdown("#### 💬 Need help?")
st.info("Our AI assistant is available in each module to provide support and answer questions based on official policy.")

display_abl_footer()
st.code(__file__.split("/")[-1], language="plaintext")
