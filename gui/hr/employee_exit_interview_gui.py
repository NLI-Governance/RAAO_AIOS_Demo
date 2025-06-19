import streamlit as st
import pandas as pd
import os
import sys

st.set_page_config(page_title="Employee Exit Interview", layout="wide")
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
    header="Departing employees and HR team",
    purpose="Collect structured feedback from employees who are voluntarily or involuntarily leaving the organization.",
    usage="Use this form to document insights about work environment, leadership, and improvement opportunities.",
    routing="Forms are saved to employee_exit_interviews.csv and reviewed by HR and leadership."
)

st.title("📤 Employee Exit Interview Form")

# Exit interview form
with st.form("exit_interview_form"):
    employee_name = st.text_input("Employee Name 🛈", help="Enter the full name of the departing employee.")
    department = st.text_input("Department 🛈", help="Department where the employee last worked.")
    departure_type = st.selectbox("Departure Type 🛈", ["Voluntary", "Involuntary", "Retirement"], help="Type of departure.")
    reason = st.text_area("Primary Reason for Leaving 🛈", help="Summarize why the employee is leaving.")
    suggestions = st.text_area("Suggestions for Improvement 🛈", help="Any suggestions for improving the organization.")
    submit = st.form_submit_button("Submit Exit Interview")

if submit:
    st.success(f"Exit interview for {employee_name} recorded.")

# Example display
st.subheader("🗂️ Exit Interview Log (example)")
example = pd.DataFrame({
    "Employee": ["A. Lee", "R. Morgan"],
    "Type": ["Voluntary", "Retirement"],
    "Department": ["Operations", "Finance"]
})
st.dataframe(example)

csv = example.to_csv(index=False).encode("utf-8")
st.download_button("📥 Export Exit Interviews", data=csv, file_name="employee_exit_interviews.csv")

# Footer
display_abl_footer()
display_gui_version("employee_exit_interview_gui.py", version="v3.1")
