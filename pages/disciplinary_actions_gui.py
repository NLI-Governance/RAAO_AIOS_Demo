import streamlit as st
import pandas as pd
from components.shared_ui_components import (
    display_logo,
    display_abl_footer,
    display_about_section,
    display_language_selector,
    display_assistant_panel,
)

st.set_page_config(page_title="Disciplinary Actions", layout="wide")

display_logo()
display_language_selector()
display_about_section("This form documents disciplinary actions for internal HR tracking. Use it to record formal warnings, investigations, or resolutions.")

st.markdown("### 📝 Disciplinary Action Form")

with st.form("disciplinary_form"):
    col1, col2 = st.columns(2)
    with col1:
        employee_name = st.text_input("Employee Name 🛈", help="Enter the full legal name of the employee involved.")
        employee_id = st.text_input("Employee ID 🛈", help="Use the official ID number from HR records.")
        department = st.selectbox("Department 🛈", ["HR", "Finance", "Operations", "IT"], help="Choose the department from the dropdown.")

    with col2:
        date_of_incident = st.date_input("Date of Incident 🛈", help="Select the date the issue occurred.")
        reported_by = st.text_input("Reported By 🛈", help="Enter the name of the person reporting the incident.")
        action_taken = st.selectbox("Action Taken 🛈", ["Verbal Warning", "Written Warning", "Suspension", "Termination"], help="Choose the final action taken.")

    incident_description = st.text_area("Incident Description 🛈", help="Describe the incident in detail including location, people involved, and sequence of events.")
    resolution_summary = st.text_area("Resolution Summary 🛈", help="Summarize the resolution steps and any follow-up required.")

    submitted = st.form_submit_button("Submit Disciplinary Record")
    if submitted:
        st.success("Record submitted successfully.")
        # Placeholder logic for saving
        record = {
            "Employee Name": employee_name,
            "Employee ID": employee_id,
            "Department": department,
            "Date of Incident": str(date_of_incident),
            "Reported By": reported_by,
            "Action Taken": action_taken,
            "Incident Description": incident_description,
            "Resolution Summary": resolution_summary
        }
        df = pd.DataFrame([record])
        df.to_csv("data/disciplinary_records.csv", mode='a', header=not Path("data/disciplinary_records.csv").exists(), index=False)

display_assistant_panel()
display_abl_footer()
st.caption("disciplinary_actions_gui.py | Rev 7.0")