import streamlit as st

from components.shared_ui_components import (
    display_logo,
    display_abl_footer,
    display_language_toggle_button,
    display_assistant_shell,
    display_gui_version
)

st.set_page_config(page_title="Navigation Menu")

display_logo()
display_language_toggle_button()
st.title("Navigation Menu")

st.markdown("Use the button below to navigate to the Employee Application module.")

# ✅ This label must exactly match the sidebar name
if st.button("📋 Employee Application"):
    st.switch_page("Employee Application Gui")

display_assistant_shell()
display_abl_footer()
display_gui_version("navigation_menu_gui.py", "v1.0-test")
