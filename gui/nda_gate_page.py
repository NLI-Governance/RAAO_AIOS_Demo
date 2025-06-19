import streamlit as st

st.set_page_config(
    page_title="Confidential Access Agreement",
    page_icon="🛡️",
    layout="centered"
)

# --- HEADER ---
st.markdown("## 🛡️ Confidential Access Agreement")
st.markdown("""
This system is protected under a Non-Disclosure Agreement (NDA).  
To continue, you must accept the confidentiality terms.
""")

# --- FORM ---
with st.form("nda_form"):
    agree = st.checkbox("✅ I Agree – Enter System")
    submitted = st.form_submit_button("Enter System")

    if submitted:
        if agree:
            try:
                st.switch_page("pages/navigation_menu_gui.py")
            except Exception as e:
                st.error("Navigation failed. Please contact the system administrator.")
                st.stop()
        else:
            st.warning("You must agree to the confidentiality terms to proceed.")
