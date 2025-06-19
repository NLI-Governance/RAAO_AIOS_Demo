import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import date

# === File Purpose ===
# HR GUI for selecting benefits during onboarding
# Compliant with ACA, COBRA, HIPAA, ERISA standards

st.set_page_config(page_title="Benefits Enrollment", layout="centered")
st.image(str(Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png").expanduser()), width=100)

st.title("🩺 Employee Benefits Enrollment")

csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_benefits_log.csv").expanduser()
csv_path.parent.mkdir(parents=True, exist_ok=True)

with st.form("benefits_enrollment_form"):
    st.text_input("Full Name", help="Enter your legal name as it appears on official records.")
    st.text_input("Employee ID", help="Use the ID assigned by HR.")
    st.text_input("Department", help="Enter the department you're assigned to.")

    st.subheader("Select Benefits Options")

    st.selectbox("Medical Coverage", ["None", "Employee Only", "Employee + Spouse", "Family"],
                 help="Choose the medical insurance option you wish to enroll in.")
    st.selectbox("Dental Coverage", ["None", "Employee Only", "Employee + Spouse", "Family"],
                 help="Dental coverage options for you and your dependents.")
    st.selectbox("Vision Coverage", ["None", "Employee Only", "Employee + Spouse", "Family"],
                 help="Select if you'd like to enroll in vision care.")
    st.selectbox("Retirement Plan", ["None", "3% Match", "5% Match", "Custom %"],
                 help="Choose a retirement plan contribution option.")
    st.selectbox("Life Insurance", ["None", "$25,000", "$50,000", "$100,000"],
                 help="Select your life insurance coverage amount.")

    st.date_input("Enrollment Date", value=date.today(), help="Date benefits enrollment is effective.")
    st.text_area("Additional Notes", help="Add any specific requests or clarifications here.")

    submitted = st.form_submit_button("Submit Enrollment")

if submitted:
    row = {
        "Name": st.session_state.get("Full Name", ""),
        "Employee ID": st.session_state.get("Employee ID", ""),
        "Department": st.session_state.get("Department", ""),
        "Medical": st.session_state.get("Medical Coverage", ""),
        "Dental": st.session_state.get("Dental Coverage", ""),
        "Vision": st.session_state.get("Vision Coverage", ""),
        "Retirement": st.session_state.get("Retirement Plan", ""),
        "Life Insurance": st.session_state.get("Life Insurance", ""),
        "Enrollment Date": st.session_state.get("Enrollment Date", str(date.today())),
        "Notes": st.session_state.get("Additional Notes", "")
    }

    df = pd.DataFrame([row])
    if csv_path.exists():
        existing = pd.read_csv(csv_path)
        df = pd.concat([existing, df], ignore_index=True)

    df.to_csv(csv_path, index=False)
    st.success("✅ Enrollment successfully submitted.")
