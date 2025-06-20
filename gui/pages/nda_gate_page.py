import sys
import streamlit as st

# Extend path to access shared components
sys.path.append("/Users/timothygriffin/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/tools/")

from shared_ui_components import (
    display_logo,
    display_abl_footer,
    display_language_toggle_button,
    display_assistant_shell,
    display_about_this_form,
    display_gui_version
)

st.set_page_config(page_title="NDA Gate")

display_logo()
display_language_toggle_button()
st.title("Confidential Access Agreement")
st.markdown("This system is protected under a Non-Disclosure Agreement (NDA). To continue, you must accept the confidentiality terms.")

# Simulate NDA agreement checkbox and entry
agree = st.checkbox("✅ I Agree – Enter System")
if agree:
    st.success("Access granted. Redirecting...")
    st.switch_page("gui/pages/navigation_menu_gui.py")  # ✅ Cloud-safe path

display_assistant_shell()
display_abl_footer()
display_gui_version("nda_gate_page.py", "v1.0")
