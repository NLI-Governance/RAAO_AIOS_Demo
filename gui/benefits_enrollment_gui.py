# benefits_enrollment_gui.py
# Connects Employee Name + ID from HR CSV, Grant Code from grants CSV

import streamlit as st
import pandas as pd
import os
from datetime import date

st.set_page_config(page_title="Benefits Enrollment", layout="centered")
st.image("logo.png", width=120)
st.title("Employee Benefits Enrollment")

st.markdown("Enroll employees into eligible benefits. Data links to HR records and grant tracking systems.")

# Paths
base = os.path.dirname(__file__)
csv_path = os.path.abspath(os.path.join(base, "..", "data", "employee_benefits_log.csv"))
hr_path = os.path.abspath(os.path.join(base, "..", "data", "employee_records.csv"))
grant_path = os.path.abspath(os.path.join(base, "..", "data", "grant_codes.csv"))
os.makedirs(os.path.dirname(csv_path), exist_ok=True)

# Load HR employee list
if os.path.exists(hr_path):
    hr_df = pd.read_csv(hr_path)
    emp_names = hr_df["Full Name"].dropna().tolist() if "Full Name" in hr_df.columns else []
    emp_ids = dict(zip(hr_df["Full Name"], hr_df["Employee ID"])) if "Employee ID" in hr_df.columns else {}
    departments = dict(zip(hr_df["Full Name"], hr_df["Department"])) if "Department" in hr_df.columns else {}
else:
    emp_names = ["Alice Johnson", "Marcus Lee"]
    emp_ids = {"Alice Johnson": "EMP001", "Marcus Lee": "EMP002"}
    departments = {"Alice Johnson": "Outreach", "Marcus Lee": "Finance"}

# Load grant codes
if os.path.exists(grant_path):
    grant_df = pd.read_csv(grant_path)
    grant_codes = grant_df["Grant Code"].dropna().tolist()
else:
    grant_codes = []

# Load log
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
else:
    df = pd.DataFrame(columns=[
        "Employee Name", "Employee ID", "Department",
        "Grant Code", "Coverage Level", "Status",
        "Benefit Type", "Enrollment Date"
    ])

coverage_levels = ["Individual", "Employee + Spouse", "Employee + Children", "Family"]
statuses = ["Active", "Pending", "Terminated"]
benefit_types = ["Health", "Dental", "Vision", "Life Insurance", "401(k)", "Disability"]

with st.form("benefits_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.selectbox("Employee Name 🛈", emp_names)
        emp_id = emp_ids.get(name, "UNKNOWN")
        dept = departments.get(name, "UNKNOWN")
        grant_code = st.selectbox("Grant Code (if applicable) 🛈", grant_codes)
    with col2:
        coverage = st.selectbox("Coverage Level 🛈", coverage_levels)
        status = st.selectbox("Status 🛈", statuses)
        benefit = st.selectbox("Benefit Type 🛈", benefit_types)
        enroll_date = st.date_input("Enrollment Date 🛈", value=date.today())

    submitted = st.form_submit_button("Save Enrollment")

if submitted:
    new_entry = {
        "Employee Name": name,
        "Employee ID": emp_id,
        "Department": dept,
        "Grant Code": grant_code,
        "Coverage Level": coverage,
        "Status": status,
        "Benefit Type": benefit,
        "Enrollment Date": enroll_date
    }
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(csv_path, index=False)
    st.success("Enrollment saved successfully.")

st.markdown("### Enrolled Records")
if df.empty:
    st.info("No enrollments recorded yet.")
else:
    st.dataframe(df, use_container_width=True)

st.download_button("Download CSV", data=df.to_csv(index=False), file_name="employee_benefits_log.csv", mime="text/csv")

st.markdown("---")
st.markdown("© 2025 Rising Against All Odds | Benefits Enrollment Portal")
