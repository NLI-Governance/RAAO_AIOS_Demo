import streamlit as st
import pandas as pd
import os
import sys

st.set_page_config(page_title="Employee Status Change", layout="wide")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from tools.shared_ui_components import (
    display_logo,
    display_abl_footer,
    display_gui_version,
    display_about_this_form,
    display_language_toggle_button,
    display_policy_assistant_button
)

# Top layout
cols = st.columns([6, 1, 1])
with cols[0]: display_logo()
with cols[1]: display_language_toggle_button()
with cols[2]: display_policy_assistant_button()

display_about_this_form(
    header="Supervisors and HR department",
    purpose="Record changes in employee job status such as promotions, department transfers, or role reclassifications.",
    usage="Submit this form any time an employee's role, title, or department officially changes.",
    routing="Updates are stored in employee_status_change_log.csv and tracked by HR."
)

st.title("🔁 Employee Status Change Form")

# Status change form
with st.form("status_change_form"):
    employee_name = st.text_input("Employee Name 🛈", help="Enter the full name of the employee affected.")
    old_status = st.text_input("Previous Role or Department 🛈", help="What was their prior title or department?")
    new_status = st.text_input("New Role or Department 🛈", help="What is their new title or department?")
    effective_date = st.date_input("Effective Date 🛈", help="Date the change goes into effect.")
    reason = st.text_area("Reason for Change 🛈", help="Briefly explain the reason for this change (e.g. promotion, restructure).")
    submitted = st.form_submit_button("Submit Status Change")

if submitted:
    st.success(f"Status change for {employee_name} submitted.")

# Example log table
st.subheader("🗂️ Status Change Log (example)")
example = pd.DataFrame({
    "Employee": ["T. Miller", "D. Wang"],
    "Old Status": ["Coordinator", "Intern"],
    "New Status": ["Manager", "Program Assistant"]
})
st.dataframe(example)

csv = example.to_csv(index=False).encode("utf-8")
st.download_button("📥 Export Status Log", data=csv, file_name="employee_status_change_log.csv")

# Footer
display_abl_footer()
display_gui_version("employee_status_change_gui.py", version="v3.1")
