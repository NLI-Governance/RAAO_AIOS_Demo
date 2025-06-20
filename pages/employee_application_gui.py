import streamlit as st
from components.shared_ui_components import display_logo, display_abl_footer

st.set_page_config(page_title="Employee Application", layout="wide")
display_logo()

st.selectbox("🌐 Language", ["English", "Español", "Français"])

with st.expander("About this form"):
    st.markdown("This application form is used by employees to register their basic information and begin onboarding at Rising Against All Odds.")

st.markdown("#### 💬 Need help?")
st.info("Our AI assistant is available in this module to provide support and answer questions based on official policy.")

display_abl_footer()
st.code(__file__.split("/")[-1], language="plaintext")