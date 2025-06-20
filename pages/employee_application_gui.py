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

st.set_page_config(page_title="Employee Application")

display_logo()
display_language_toggle_button()
st.title("Employee Application")

# About this form section
display_about_this_form(
    header="All new or returning job applicants at RAAO",
    purpose="Collect employee application details for onboarding, HR, and compliance.",
    usage="Complete all required fields. Use the information icons for help. Submit once finished.",
    routing="HR will review your submission and contact you within 3 business days."
)

st.write("📄 This is a placeholder for the employee application module.")

if st.button("⬅️ Back to Navigation"):
    st.switch_page("navigation_menu_gui.py")

display_assistant_shell()
display_abl_footer()
display_gui_version("employee_application_gui.py", "v1.0")
