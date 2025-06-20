import streamlit as st
from components.shared_ui_components import display_logo, display_abl_footer

st.set_page_config(page_title="Disciplinary Actions", layout="wide")
display_logo()
st.selectbox("🌐 Language", ["English", "Español", "Français"])

with st.expander("About this form"):
    st.markdown("Log and manage formal disciplinary actions for employees.")

st.markdown("#### 💬 Need help?")
st.info("Use this form to document disciplinary findings and actions taken.")

display_abl_footer()
st.code(__file__.split("/")[-1], language="plaintext")