import sys
import streamlit as st

# Extend path to locate shared components from the tools directory
sys.path.append("/Users/timothygriffin/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/tools/")

from shared_ui_components import (
    display_logo,
    display_abl_footer,
    display_language_toggle_button,
    display_assistant_shell
)

st.set_page_config(page_title="Navigation Menu")

display_logo()
display_language_toggle_button()

st.title("Navigation Menu")

# Example navigation buttons (can be customized)
if st.button("Employee Application"):
    st.switch_page("employee_application_gui.py")
if st.button("Training Tracker"):
    st.switch_page("training_tracker_gui.py")
if st.button("Disciplinary Actions"):
    st.switch_page("disciplinary_actions_gui.py")

display_assistant_shell()
display_abl_footer()
