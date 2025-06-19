import streamlit as st

st.set_page_config(page_title="Confidential Access Agreement", layout="centered")

def main():
    st.markdown(
        """
        <h1 style='text-align: center; color: white;'>🛡️ Confidential Access Agreement</h1>
        <p style='text-align: center; font-size: 18px;'>This system is protected under a Non-Disclosure Agreement (NDA). To continue, you must accept the confidentiality terms.</p>
        """,
        unsafe_allow_html=True,
    )

    agree = st.checkbox("✅ I Agree – Enter System")

    if agree:
        if st.button("Enter System"):
            st.switch_page("navigation_menu_gui")  # ✅ Must match label from GUI file

if __name__ == "__main__":
    main()
