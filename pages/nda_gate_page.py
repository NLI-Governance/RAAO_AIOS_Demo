import streamlit as st
from components.shared_ui_components import (
    display_logo,
    display_language_selector,
    display_about_section,
    display_assistant_panel,
    display_abl_footer
)

st.set_page_config(page_title="NDA Gate", layout="wide")

display_logo()
display_language_selector()
display_about_section("You must agree to the terms of the Non-Disclosure Agreement (NDA) to continue into the system.")

st.title("🔐 Non-Disclosure Agreement (NDA)")

nda_text = """
By entering the Rising Against All Odds system, you agree to maintain the confidentiality of all personal data, internal documents,
training materials, grant submissions, and strategic operations. Sharing or misuse of this information is grounds for disciplinary action,
up to and including termination or legal prosecution.
"""

st.warning(nda_text)

confirm = st.checkbox("✅ I agree to the terms of the NDA")

if confirm:
    st.success("Access granted. Proceed to the system.")
    st.page_link("pages/navigation_menu_gui.py", label="➡️ Enter System")
else:
    st.error("You must agree to the NDA before proceeding.")

display_assistant_panel()
display_abl_footer()
st.caption("nda_gate_page.py | Rev 7.0")