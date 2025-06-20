import streamlit as st

from components.shared_ui_components import (
    display_logo,
    display_abl_footer,
    display_language_toggle_button,
    display_assistant_shell,
    display_gui_version
)

from components.navigation_utils import safe_switch_page

st.set_page_config(page_title="Navigation Menu")

display_logo()
display_language_toggle_button()
st.title("Navigation Menu")

st.markdown("Welcome to the AIOS system. Use the buttons below to access each functional module.")

# Human Resources
st.subheader("🧑‍💼 Human Resources")
if st.button("📋 Employee Application"):
    safe_switch_page("employee_app_gui.py")
if st.button("📄 Disciplinary Actions"):
    safe_switch_page("disciplinary_actions_gui.py")
if st.button("📝 Training Tracker"):
    safe_switch_page("training_tracker_gui.py")

# Finance & Grants
st.subheader("💰 Finance & Grants")
if st.button("🕒 Payroll Timecode Entry"):
    safe_switch_page("payroll_timecode_entry_gui.py")
if st.button("🎯 Grant Funding Code Manager"):
    safe_switch_page("grant_funding_code_manager_gui.py")

# Vendors & Clients
st.subheader("📦 Vendors & Clients")
if st.button("📬 Vendor Onboarding"):
    safe_switch_page("vendor_onboarding_gui.py")
if st.button("📥 Customer Onboarding"):
    safe_switch_page("customer_onboarding_gui.py")

# Executive & Tools
st.subheader("📊 System Tools")
if st.button("📈 CEO Reports Dashboard"):
    safe_switch_page("ceo_reports_dashboard_gui.py")
if st.button("🧠 AI Policy Test Runner"):
    safe_switch_page("policy_test_runner.py")

display_assistant_shell()
display_abl_footer()
display_gui_version("navigation_menu_gui.py", "v3.0-fullmenu")
