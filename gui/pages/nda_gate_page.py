import streamlit as st

st.set_page_config(page_title="Confidential Access Agreement", page_icon="🛡️", layout="centered")

def main():
    st.markdown("<h1 style='text-align: center;'>🔒 Confidential Access Agreement</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: center; font-size: 1.1rem; margin-top: 1.5em;'>
        This system is protected under a Non-Disclosure Agreement (NDA).<br>
        To continue, you must accept the confidentiality terms.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### ")

    agree = st.checkbox("✅ I Agree – Enter System")

    if agree:
        if st.button("Enter System"):
            # ✅ Page label from file title
            st.switch_page("Navigation Menu GUI")

if __name__ == "__main__":
    main()
