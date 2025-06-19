# employee_application_gui.py
# With fixed dynamic CSV path + dropdown enforcement

import streamlit as st
import pandas as pd
import os
from datetime import date

st.set_page_config(page_title="Employee Application", layout="centered")
st.image("logo.png", width=120)
st.title("Employee Application Form")

# Dynamic absolute path to ~/.../data/employee_records.csv
csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "employee_records.csv"))

# Ensure /data exists
os.makedirs(os.path.dirname(csv_path), exist_ok=True)

# Load or create file
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
else:
    df = pd.DataFrame(columns=[
        "Full Name", "Date of Birth", "Phone Number",
        "Email", "Department", "Position", "Start Date",
        "Employment Type", "Citizenship Status", "Referred By"
    ])

# Dropdown-controlled inputs
departments = [
    "Outreach", "Shelter", "Administration", "Case Management",
    "HR", "Finance", "Facilities", "Development", "Volunteer Services"
]

employment_types = ["Full Time", "Part Time", "Temporary", "Contract", "Internship"]
citizenship_statuses = ["U.S. Citizen", "Permanent Resident", "Work Visa", "DACA", "Other"]

positions = [
    "Case Manager", "Peer Specialist", "Intake Coordinator",
    "Outreach Worker", "Admin Assistant", "Maintenance", "Intern (Admin)"
]

referrers = ["Employee", "Job Fair", "Partner Org", "Walk-in", "Indeed", "Other"]

with st.form("application_form"):
    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("Full Name 🛈", placeholder="Alice Johnson")
        date_of_birth = st.date_input("Date of Birth 🛈", min_value=date(1900, 1, 1), max_value=date.today())
        phone = st.text_input("Phone Number 🛈", placeholder="(555) 123-4567")
        email = st.text_input("Email 🛈", placeholder="alice@example.com")
        department = st.selectbox("Preferred Department 🛈", departments)
    with col2:
        position = st.selectbox("Position Applied For 🛈", positions)
        start_date = st.date_input("Available Start Date 🛈", value=date.today())
        employment_type = st.selectbox("Employment Type 🛈", employment_types)
        citizenship_status = st.selectbox("Citizenship Status 🛈", citizenship_statuses)
        referred_by = st.selectbox("How did you hear about us? 🛈", referrers)

    submitted = st.form_submit_button("Submit Application")
    if submitted:
        new_entry = {
            "Full Name": full_name,
            "Date of Birth": date_of_birth,
            "Phone Number": phone,
            "Email": email,
            "Department": department,
            "Position": position,
            "Start Date": start_date,
            "Employment Type": employment_type,
            "Citizenship Status": citizenship_status,
            "Referred By": referred_by
        }
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_csv(csv_path, index=False)
        st.success("Application submitted successfully.")

# Admin view toggle
if st.checkbox("Show Application Log (Admin Only)"):
    st.markdown("### Application Log")
    if df.empty:
        st.info("No employee applications submitted yet.")
    else:
        st.dataframe(df, use_container_width=True)

st.download_button("Download CSV", data=df.to_csv(index=False), file_name="employee_records.csv", mime="text/csv")

st.markdown("---")
st.markdown("© 2025 Rising Against All Odds | Employment System Intake")
