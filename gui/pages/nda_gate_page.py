import streamlit as st

st.set_page_config(page_title="Confidential Access Agreement", layout="centered")

def main():
    st.markdown("<h1 style='text-align: center;'>🔐 Confidential Access Agreement</h1>", unsafe_allow_html=True)
    st.markdown("This system is protected under a Non-Disclosure Agreement (NDA). To continue, you must accept the confidentiality terms.")
    
    agree = st.checkbox("✅ I Agree – Enter System")
    
    if agree:
        if st.button("Enter System"):
            st.switch_page("Navigation Menu Gui")  # ✅ Exact match

if __name__ == "__main__":
    main()
