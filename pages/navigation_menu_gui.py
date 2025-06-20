import streamlit as st

from shared_ui_components import (
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

# --- Employee/HR Modules ---
st.subheader("🧑‍💼 Human Resources")
if st.button("Employee Application"):
    st.switch_page("gui/pages/employee_application_gui.py")
if st.button("Training Tracker"):
    st.switch_page("gui/pages/training_tracker_gui.py")
if st.button("Disciplinary Actions"):
    st.switch_page("gui/pages/disciplinary_actions_gui.py")
if st.button("Benefits Enrollment"):
    st.switch_page("gui/pages/benefits_enrollment_gui.py")

# --- Vendor/Customer Modules ---
st.subheader("🔄 External Relations")
if st.button("Vendor Onboarding"):
    st.switch_page("gui/pages/vendor_onboarding_gui.py")
if st.button("Customer Onboarding"):
    st.switch_page("gui/pages/customer_onboarding_gui.py")

# --- Finance Modules ---
st.subheader("💵 Finance & Grants")
if st.button("Payroll Timecode Entry"):
    st.switch_page("gui/pages/payroll_timecode_entry_gui.py")
if st.button("Grant Funding Code Manager"):
    st.switch_page("gui/pages/grant_funding_code_manager_gui.py")

# --- Executive & Admin Tools ---
st.subheader("📊 Admin & Executive Tools")
if st.button("CEO Reports Dashboard"):
    st.switch_page("gui/pages/ceo_reports_dashboard_gui.py")
if st.button("Policy Test Runner"):
    st.switch_page("gui/pages/policy_test_runner.py")
if st.button("AI Policy Assistant"):
    st.switch_page("gui/pages/policy_procedure_rag_gui.py")

display_assistant_shell()
display_abl_footer()
display_gui_version("navigation_menu_gui.py", "v1.0")
