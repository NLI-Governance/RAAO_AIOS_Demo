# employee_exit_interview_gui.py
# Purpose: Capture structured employee feedback during exit interview process
# Standards: EEOC, HRSA, ABL Internal Exit Interview Protocol

import streamlit as st
import pandas as pd
from pathlib import Path

# Path to save the exit interview CSV file
CSV_PATH = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_exit_interviews.csv").expanduser()

st.set_page_config(page_title="Employee Exit Interview", layout="centered")
st.image(str(Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png").expanduser()), width=100)
st.title("Employee Exit Interview Form")

st.markdown("Please complete this form to help us improve our workplace.")

with st.form("exit_interview_form"):
    name = st.text_input("Employee Name")
    employee_id = st.text_input("Employee ID")
    department = st.text_input("Department")
    last_day = st.date_input("Last Day Worked")

    reason = st.selectbox("Reason for Leaving", [
        "Another job opportunity",
        "Relocation",
        "Health or personal reasons",
        "Work environment",
        "Compensation",
        "Other"
    ], help="Why are you choosing to leave the organization?")

    satisfaction = st.slider("Overall Job Satisfaction (1=Low, 5=High)", 1, 5,
                              help="How satisfied were you with your job overall?")

    supervisor_feedback = st.text_area("Feedback on Supervisor",
        help="Provide any feedback about your supervisor or team leadership.")

    improvement_suggestions = st.text_area("Suggestions for Improvement",
        help="Share ideas on how the organization could improve.")

    rehire_eligible = st.radio("Would you consider working here again in the future?", ["Yes", "No"],
        help="Would you consider returning to this organization if circumstances were right?")

    submit = st.form_submit_button("Submit Exit Interview")

    if submit:
        row = pd.DataFrame([{
            "Employee Name": name,
            "Employee ID": employee_id,
            "Department": department,
            "Last Day": str(last_day),
            "Reason": reason,
            "Satisfaction": satisfaction,
            "Supervisor Feedback": supervisor_feedback,
            "Improvement Suggestions": improvement_suggestions,
            "Rehire Eligible": rehire_eligible
        }])

        if not CSV_PATH.exists():
            row.to_csv(CSV_PATH, index=False)
        else:
            row.to_csv(CSV_PATH, mode='a', header=False, index=False)

        st.success("Exit interview submitted successfully. Thank you for your feedback!")

