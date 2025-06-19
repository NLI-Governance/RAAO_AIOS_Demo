import streamlit as st

def main():
    st.set_page_config(page_title="Confidential Preview Access", layout="centered")

    st.markdown("""
        <h1 style='text-align: center;'>🛡️ Confidential Access Agreement</h1>
        <p style='text-align: center;'>This system is protected under a Non-Disclosure Agreement (NDA). To continue, you must accept the confidentiality terms.</p>
    """, unsafe_allow_html=True)

    if st.button("✅ I Agree – Enter System"):
        st.switch_page("navigation_menu_gui.py")

if __name__ == "__main__":
    main()