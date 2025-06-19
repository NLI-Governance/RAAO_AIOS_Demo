# ~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/gui/nda_gate_page.py

import streamlit as st

def main():
    st.set_page_config(
        page_title="Confidential Access Agreement",
        layout="centered"
    )

    st.markdown(
        "<h1 style='text-align: center; color: white;'>🔒 Confidential Access Agreement</h1>",
        unsafe_allow_html=True
    )

    st.write("This system is protected under a Non-Disclosure Agreement (NDA). "
             "To continue, you must accept the confidentiality terms.")

    agree = st.checkbox("✅ I Agree – Enter System")

    if agree:
        if st.button("Enter System"):
            # ✅ Corrected path relative to gui/
            st.switch_page("../pages/navigation_menu_gui.py")

if __name__ == "__main__":
    main()
