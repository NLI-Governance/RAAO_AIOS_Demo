# hr_onboarding_gui_FINAL_LOCKED_v3.py
# Purpose: Fully compliant HR onboarding form with enforcement of required fields
# Standards: W-4, I-9, EEOC, ISO 9001, ABL Rev2 air-gap support

import streamlit as st
import csv
import os
from datetime import date

st.set_page_config(page_title="HR Onboarding", layout="centered")

LOGO_PATH = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
DATA_PATH = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/data/hr/employees.csv")

if os.path.exists(LOGO_PATH):
    st.image(LOGO_PATH, width=120)

st.title("🎯 HR Onboarding Form")

# --- Employee Information ---
st.subheader("Employee Information")
name = st.text_input("Full Legal Name", help="Full legal name of the new employee.")
email = st.text_input("Email", help="Primary contact email.")
phone = st.text_input("Phone", help="Cell phone number.")
start_date = st.date_input("Start Date", value=date.today(), help="First official workday.")
emp_id = st.text_input("Assigned Employee ID", help="Unique HR or payroll identifier.")

# --- Address Details ---
street = st.text_input("Street Address", help="Employee’s home street address.")
city = st.text_input("City", help="City of residence.")
state = st.text_input("State", help="Two-letter state abbreviation.")
zip_code = st.text_input("ZIP Code", help="5-digit ZIP code.")

# --- Emergency Contact ---
st.subheader("Emergency Contact")
em_name = st.text_input("Emergency Contact Name", help="Person to notify in case of emergency.")
em_phone = st.text_input("Emergency Contact Phone", help="Phone number of emergency contact.")

# --- Department and Role Assignment ---
st.subheader("Department & Role Assignment")
department = st.text_input("Department", help="Department or team assignment.")
manager = st.text_input("Manager Name", help="Direct manager or supervisor (optional).")
role = st.selectbox("System Role", ["Viewer", "Staff", "Accounting", "HR", "Manager", "Admin"], help="Access level for internal systems.")

# --- Compliance Section ---
st.subheader("Compliance Documentation")
w4 = st.checkbox("W-4 Received", help="Check if the employee submitted a W-4 form.")
i9 = st.checkbox("I-9 Verified", help="Check if legal eligibility to work has been verified.")
st.caption("📄 Acceptable documents for I-9 include: Passport, Green Card, or a combination of State ID and Social Security Card.")
upload = st.file_uploader("Upload I-9 ID(s)", type=["pdf", "jpg", "png"], help="Upload photos or scans of ID documents used for verification.")

# --- Certification Section ---
st.subheader("HR Certification")
certifier = st.text_input("HR Staff Name", help="Person completing this onboarding form.")
notes = st.text_area("Internal Notes", help="Optional notes, visible to HR only.")
certify = st.checkbox("I certify that all required onboarding steps are complete.", help="You must check this to proceed.")

# --- Submission Logic ---
if st.button("Submit Onboarding Record"):
    if all([name, email, emp_id, department, role, em_name, em_phone, w4, i9, certify]):
        record = {
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Start Date": start_date.strftime("%Y-%m-%d"),
            "Employee ID": emp_id,
            "Street": street,
            "City": city,
            "State": state,
            "ZIP": zip_code,
            "Emergency Contact": em_name,
            "Emergency Phone": em_phone,
            "Department": department,
            "Manager": manager,
            "System Role": role,
            "W-4 Received": w4,
            "I-9 Verified": i9,
            "HR Certifier": certifier,
            "Notes": notes
        }
        header = list(record.keys())
        file_exists = os.path.exists(DATA_PATH)
        with open(DATA_PATH, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=header)
            if not file_exists:
                writer.writeheader()
            writer.writerow(record)
        st.success("✅ Onboarding record saved successfully.")
    else:
        st.error("❌ All required fields must be completed including legal compliance and role assignment.")
