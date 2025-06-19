import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import date

# === Standards Compliance ===
# File: benefits_enrollment_gui.py
# Purpose: Employee selects benefits options during onboarding
# Standards: ACA, IRS 125, ERISA, COBRA, HIPAA, ADA, ABL Rev2

st.set_page_config(page_title="Benefits Enrollment", layout="centered")
st.image(str(Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png").expanduser()), width=100)

st.title("🩺 Employee Benefits Enrollment")

csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_benefits_log.csv").expanduser()
csv_path.parent.mkdir(parents=True, exist_ok=True)

with st.form("benefits_enrollment_form"):
    name = st.text_input("Full Name")
    emp_id = st.text_input("Employee ID")
    department = st.text_input("Department")

    st.subheader("Select Benefits Options")

    medical = st.selectbox("Medical Coverage", ["None", "Employee Only", "Employee + Spouse", "Family"])
    dental = st.selectbox("Dental Coverage", ["None", "Employee Only", "Employee + Spouse", "Family"])
    vision = st.selectbox("Vision Coverage", ["None", "Employee Only", "Employee + Spouse", "Family"])
    retirement = st.selectbox("Retirement Plan", ["None", "3% Match", "5% Match", "Custom %"])
    life = st.selectbox("Life Insurance", ["None", "$25,000", "$50,000", "$100,000"])

    enrollment_date = st.date_input("Enrollment Date", value=date.today())
    notes = st.text_area("Additional Notes")

    submit = st.form_submit_button("Submit Enrollment")

if submit:
    new_entry = pd.DataFrame([{
        "Name": name,
        "Employee ID": emp_id,
        "Department": department,
        "Medical": medical,
        "Dental": dental,
        "Vision": vision,
        "Retirement": retirement,
        "Life Insurance": life,
        "Enrollment Date": enrollment_date,
        "Notes": notes
    }])

    if csv_path.exists():
        existing = pd.read_csv(csv_path)
        combined = pd.concat([existing, new_entry], ignore_index=True)
    else:
        combined = new_entry

    combined.to_csv(csv_path, index=False)
    st.success("✅ Enrollment submitted and saved.")
