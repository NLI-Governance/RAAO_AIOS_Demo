import streamlit as st

st.set_page_config(
    page_title="Confidential Access Agreement",
    page_icon="🛡️",
    layout="centered",
)

st.markdown("## 🛡️ Confidential Access Agreement")
st.markdown(
    "This system is protected under a Non-Disclosure Agreement (NDA). "
    "To continue, you must accept the confidentiality terms."
)

agree = st.checkbox("✅ I Agree – Enter System")

if agree:
    if st.button("Enter System"):
        st.switch_page("navigation_menu_gui.py")  # This must match filename
