import sys
import streamlit as st

# Extend path to access shared UI components
sys.path.append("/Users/timothygriffin/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/tools/")

from shared_ui_components import (
    display_logo,
    display_abl_footer,
    display_language_toggle_button,
    display_assistant_shell,
    display_about_this_form,
    display_gui_version
)

st.set_page_config(page_title="Training Tracker")

display_logo()
display_language_toggle_button()
st.title("Training Tracker")

# About this form section
display_about_this_form(
    header="Employees required to complete safety or professional development training",
    purpose="Track completion of required training modules, certification status, and expiration dates.",
    usage="Select an employee and training type. Enter completion date. Use info icons for help.",
    routing="HR and compliance teams will use this record to manage follow-ups and renewals."
)

st.write("🎯 This is a placeholder for the training tracker module.")

if st.button("⬅️ Back to Navigation"):
    st.switch_page("navigation_menu_gui.py")

display_assistant_shell()
display_abl_footer()
display_gui_version("training_tracker_gui.py", "v1.0")
