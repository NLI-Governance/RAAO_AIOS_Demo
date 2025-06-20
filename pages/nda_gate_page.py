import streamlit as st
from components.shared_ui_components import display_logo, display_abl_footer

st.set_page_config(page_title="NDA Gate", layout="wide")
display_logo()
st.selectbox("🌐 Language", ["English", "Español", "Français"])

st.title("Non-Disclosure Agreement")
st.info("By accessing this system, you agree to maintain the confidentiality of all internal data, client information, and proprietary materials.")

confirm = st.checkbox("✅ I have read and agree to the NDA terms.")

if confirm:
    st.success("Access granted. You may proceed to the main system.")
    st.page_link("pages/navigation_menu_gui.py", label="Enter System", icon="➡️")
else:
    st.warning("You must agree to the NDA before proceeding.")

display_abl_footer()