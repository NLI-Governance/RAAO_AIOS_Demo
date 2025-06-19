import streamlit as st

def main():
    st.markdown(
        """
        <style>
            .stButton>button {
                color: white;
                background-color: #FF4B4B;
                font-size: 1.2em;
                padding: 0.5em 1em;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("🛡️ Confidential Access Agreement")
    st.write("This system is protected under a Non-Disclosure Agreement (NDA). To continue, you must accept the confidentiality terms.")

    agreed = st.checkbox("✅ I Agree – Enter System")

    if agreed:
        if st.button("Enter System"):
            st.switch_page("navigation_menu_gui.py")

if __name__ == "__main__":
    main()
