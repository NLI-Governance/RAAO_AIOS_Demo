# hr_onboarding_gui_v2.py
# Purpose: Finalized HR onboarding GUI with address fields and hover info icons
# Compliance: I-9, W-4, EEOC, ISO 9001, air-gapped support

import streamlit as st
import pandas as pd
import os
from datetime import date
from io import StringIO

st.set_page_config(page_title="HR Onboarding Form", layout="centered")

st.image("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png", width=120)
st.title("🎯 HR Onboarding Form")
st.markdown("Please complete onboarding for the new hire below.")

st.header("Employee Information")
name = st.text_input("Full Legal Name", help="Enter the employee’s full name as it appears on legal documents.")
email = st.text_input("Email", help="Work or personal email used for communication.")
phone = st.text_input("Phone", help="Primary phone number to reach the employee.")
street = st.text_input("Street Address", help="Home street address (include Apt/Suite if applicable).")
city = st.text_input("City", help="City of residence.")
state = st.text_input("State", help="Two-letter state abbreviation (e.g., FL).")
zip_code = st.text_input("ZIP Code", help="5-digit ZIP code.")
start_date = st.date_input("Start Date", value=date.today(), help="Employee’s first official day of work.")
emp_id = st.text_input("Assigned Employee ID", help="Unique ID for internal tracking.")

st.header("Emergency Contact")
em_contact = st.text_input("Emergency Contact Name", help="Person to contact in case of emergency.")
em_phone = st.text_input("Emergency Contact Phone", help="Phone number of the emergency contact.")

st.header("Department & Management")
department = st.text_input("Department", help="Department where the employee will work.")
manager = st.text_input("Manager Name", help="Supervisor or manager responsible for this employee.")
role = st.selectbox("System Role", ["Viewer", "Staff", "Manager", "Admin"], help="Determines access level in the AIOS system.")

st.header("Compliance Documentation")
w4_received = st.checkbox("W-4 received", help="Check this if the W-4 tax form has been completed and submitted.")
i9_complete = st.checkbox("I-9 verification completed", help="Check this if I-9 eligibility verification is finished.")
doc_tip = "You must provide one of the following: A U.S. passport, or a combination of a state ID and Social Security card. Other acceptable documents include permanent resident cards and employment authorization documents. Visit USCIS.gov for the full list."
st.selectbox("📑 What documents are acceptable for I-9 verification?", options=[
    "U.S. Passport",
    "Driver's License + Social Security Card",
    "Permanent Resident Card",
    "Employment Authorization Document"
], help=doc_tip)
uploaded_files = st.file_uploader("Upload presented ID(s)", accept_multiple_files=True, type=['pdf', 'jpg', 'png'], help="Upload copies of IDs used for I-9 verification.")

st.header("HR Certification")
hr_cert_name = st.text_input("HR Staff Name", help="Full name of HR staff completing this onboarding.")
notes = st.text_area("Internal Notes", help="Optional notes about onboarding (visible to HR only).")
certified = st.checkbox("I certify that the above onboarding steps have been completed.", help="Required before submission.")

if st.button("Submit Onboarding Record"):
    if name and email and emp_id and department and manager and certified:
        record = {
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Street": street,
            "City": city,
            "State": state,
            "ZIP": zip_code,
            "Start Date": start_date.strftime("%Y-%m-%d"),
            "Employee ID": emp_id,
            "Emergency Contact": em_contact,
            "Emergency Phone": em_phone,
            "Department": department,
            "Manager": manager,
            "Role": role,
            "W-4 Received": w4_received,
            "I-9 Complete": i9_complete,
            "HR Certifier": hr_cert_name,
            "Notes": notes
        }

        csv_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/onboarded_employees.csv")
        df = pd.DataFrame([record])
        if os.path.exists(csv_path):
            df.to_csv(csv_path, mode='a', index=False, header=False)
        else:
            df.to_csv(csv_path, index=False)
        st.success("✅ Onboarding record saved successfully.")
    else:
        st.error("❌ Please complete all required fields before submitting.")
