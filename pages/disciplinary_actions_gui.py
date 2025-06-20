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

st.set_page_config(page_title="Disciplinary Actions")

display_logo()
display_language_toggle_button()
st.title("Disciplinary Actions")

# About this form section
display_about_this_form(
    header="Supervisors or HR staff documenting incidents or employee conduct",
    purpose="Capture disciplinary issues, corrective actions, and outcomes for HR and compliance records.",
    usage="Use detailed language. Complete all required fields. Hover over icons for documentation tips.",
    routing="This record will be routed to HR and, if needed, executive review for follow-up."
)

st.write("⚠️ This is a placeholder for the disciplinary actions module.")

if st.button("⬅️ Back to Navigation"):
    st.switch_page("navigation_menu_gui.py")

display_assistant_shell()
display_abl_footer()
display_gui_version("disciplinary_actions_gui.py", "v1.0")
