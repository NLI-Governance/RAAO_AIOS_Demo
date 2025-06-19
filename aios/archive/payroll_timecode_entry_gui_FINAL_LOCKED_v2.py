# payroll_timecode_entry_gui.py
# Time entry GUI with Grant Code dropdown enforcement

import streamlit as st
import pandas as pd
import os
from datetime import date

st.set_page_config(page_title="Timecode Entry", layout="centered")
st.image("logo.png", width=120)
st.title("Payroll Timecode Entry")

st.markdown("Use this form to log time worked and assign hours to valid grant codes and departments.")

# File setup
base = os.path.dirname(__file__)
csv_path = os.path.abspath(os.path.join(base, "..", "data", "payroll_journal.csv"))
grant_path = os.path.abspath(os.path.join(base, "..", "data", "grant_codes.csv"))
os.makedirs(os.path.dirname(csv_path), exist_ok=True)

# Load grant codes
if os.path.exists(grant_path):
    grant_df = pd.read_csv(grant_path)
    grant_codes = grant_df["Grant Code"].dropna().tolist()
else:
    grant_codes = []

# Load or create payroll log
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
else:
    df = pd.DataFrame(columns=[
        "Employee Name", "Employee ID", "Department",
        "Date Worked", "Hours Worked", "Time Code",
        "Grant Code", "Job Site / Program", "Entered By", "Approved By"
    ])

# Controlled dropdowns
departments = [
    "Outreach", "Shelter", "Administration", "Case Management",
    "HR", "Finance", "Facilities", "Development", "Volunteer Services"
]

time_codes = ["ADMIN", "FIELD", "DIRECT", "TRAINING", "TRAVEL", "GRANT"]
job_sites = ["Main Office", "Shelter A", "Mobile Unit", "Virtual", "Other"]
approvers = ["Brian White", "HR Director", "Cynthia Rios", "Finance Manager"]

with st.form("time_form"):
    col1, col2 = st.columns(2)
    with col1:
        employee_name = st.text_input("Employee Name 🛈", placeholder="Alice Johnson")
        employee_id = st.text_input("Employee ID 🛈", placeholder="EMP005")
        department = st.selectbox("Department 🛈", departments)
        date_worked = st.date_input("Date Worked 🛈", value=date.today())
        hours = st.number_input("Hours Worked 🛈", min_value=0.0, step=0.25)
    with col2:
        time_code = st.selectbox("Time Code 🛈", time_codes)
        grant_code = st.selectbox("Grant Code 🛈", grant_codes)
        job_site = st.selectbox("Job Site / Program 🛈", job_sites)
        entered_by = st.text_input("Entered By 🛈", placeholder="System User")
        approved_by = st.selectbox("Approved By 🛈", approvers)

    submitted = st.form_submit_button("Submit Time Entry")

if submitted:
    new_entry = {
        "Employee Name": employee_name,
        "Employee ID": employee_id,
        "Department": department,
        "Date Worked": date_worked,
        "Hours Worked": hours,
        "Time Code": time_code,
        "Grant Code": grant_code,
        "Job Site / Program": job_site,
        "Entered By": entered_by,
        "Approved By": approved_by
    }
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(csv_path, index=False)
    st.success("Time entry saved successfully.")

st.markdown("### Logged Time Entries")
if df.empty:
    st.info("No time entries recorded yet.")
else:
    st.dataframe(df, use_container_width=True)

st.download_button("Download CSV", data=df.to_csv(index=False), file_name="payroll_journal.csv", mime="text/csv")

st.markdown("---")
st.markdown("© 2025 Rising Against All Odds | Payroll Journal Entry System")
