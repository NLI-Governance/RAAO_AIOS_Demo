import streamlit as st

st.set_page_config(page_title="Confidential Access", layout="centered")

def main():
    st.markdown("## 🛡️ Confidential Access Agreement")
    st.markdown(
        "This system is protected under a Non-Disclosure Agreement (NDA). "
        "To continue, you must accept the confidentiality terms."
    )

    agree = st.checkbox("✅ I Agree – Enter System")

    if agree:
        st.switch_page("navigation_menu_gui.py")  # ✅ Must match exact page label

if __name__ == "__main__":
    main()
