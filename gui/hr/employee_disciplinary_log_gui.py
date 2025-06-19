import streamlit as st
import pandas as pd
import os
import sys

st.set_page_config(page_title="Employee Disciplinary Log", layout="wide")
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
    header="Supervisors, HR representatives, and compliance officers",
    purpose="Document all employee disciplinary actions for review and compliance purposes.",
    usage="Use this form to log written warnings, performance issues, or formal notices. Complete all fields and use hover help.",
    routing="Records are saved to employee_disciplinary_log.csv and reviewed by HR and leadership teams."
)

st.title("⚠️ Employee Disciplinary Action Log")

# Disciplinary form
with st.form("disciplinary_form"):
    employee_name = st.text_input("Employee Name 🛈", help="Full legal name of the employee receiving the action.")
    department = st.text_input("Department 🛈", help="Which department the employee is assigned to.")
    incident_date = st.date_input("Incident Date 🛈", help="Date the infraction occurred.")
    action_type = st.selectbox("Action Type 🛈", ["Verbal Warning", "Written Warning", "Final Notice", "Suspension", "Termination"], help="Level of disciplinary action.")
    description = st.text_area("Incident Description 🛈", help="Detailed description of the incident including people involved, location, and behavior.")
    resolution = st.text_area("Resolution Summary 🛈", help="Document the outcome of the investigation or corrective action taken.")
    submit = st.form_submit_button("Log Action")

if submit:
    st.success(f"Disciplinary action for '{employee_name}' recorded.")

# Example table
st.subheader("🗂️ Disciplinary Log (example)")
example = pd.DataFrame({
    "Employee": ["C. Barnes", "N. Patel"],
    "Action": ["Written Warning", "Final Notice"],
    "Date": ["2024-01-18", "2024-03-05"]
})
st.dataframe(example)

csv = example.to_csv(index=False).encode("utf-8")
st.download_button("📥 Export Disciplinary Log", data=csv, file_name="employee_disciplinary_log.csv")

# Footer
display_abl_footer()
display_gui_version("employee_disciplinary_log_gui.py", version="v3.1")
