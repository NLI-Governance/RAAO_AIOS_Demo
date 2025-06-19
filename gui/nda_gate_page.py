import streamlit as st

st.set_page_config(
    page_title="Confidential Access Agreement",
    layout="wide"
)

def main():
    st.markdown("## 🛡️ Confidential Access Agreement")
    st.write(
        "This system is protected under a Non-Disclosure Agreement (NDA). "
        "To continue, you must accept the confidentiality terms."
    )

    agree = st.checkbox("✅ I Agree – Enter System")

    if agree:
        if st.button("Enter System"):
            # ✅ Correct Streamlit Cloud page-relative path
            st.switch_page("pages/navigation_menu_gui.py")

if __name__ == "__main__":
    main()
