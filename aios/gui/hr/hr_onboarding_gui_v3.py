# hr_onboarding_gui_v3.py
# Purpose: Final HR onboarding GUI with address, compliance, tooltips
# Standards: W-4, I-9, EEOC, ISO 9001, air-gapped support

import streamlit as st
import pandas as pd
import os
from datetime import date

st.set_page_config(page_title="HR Onboarding Form", layout="centered")

logo_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
st.image(logo_path, width=120)
st.title("🎯 HR Onboarding Form")
st.markdown("Please complete onboarding for the new hire below.")

st.header("Employee Information")
name = st.text_input("Full Legal Name", help="Enter the employee’s full legal name.")
email = st.text_input("Email", help="Work or personal email used for HR communication.")
phone = st.text_input("Phone", help="Primary contact phone number.")
street = st.text_input("Street Address", help="Home street address.")
city = st.text_input("City", help="City of residence.")
state = st.text_input("State", help="Two-letter state code (e.g., CA).")
zip_code = st.text_input("ZIP Code", help="5-digit postal code.")
start_date = st.date_input("Start Date", value=date.today(), help="First official day of employment.")
emp_id = st.text_input("Assigned Employee ID", help="Unique internal employee ID.")

st.header("Emergency Contact")
em_name = st.text_input("Emergency Contact Name", help="Full name of emergency contact.")
em_phone = st.text_input("Emergency Contact Phone", help="Phone number to reach the contact.")

st.header("Department & Management")
department = st.text_input("Department", help="Department employee will be assigned to.")
manager = st.text_input("Manager Name", help="Direct supervisor responsible.")
role = st.selectbox("System Role", ["Viewer", "Staff", "Manager", "Admin"], help="Role determines access level in the system.")

st.header("Compliance Documentation")
w4 = st.checkbox("W-4 received", help="Check once the employee has completed a W-4 form.")
i9 = st.checkbox("I-9 verification completed", help="Check after acceptable I-9 documents have been presented.")
st.markdown("ℹ️ **What documents are acceptable for I-9 verification?**")
st.caption("You may use one of the following combinations:\n"
           "- U.S. Passport or Passport Card\n"
           "- Driver's license + Social Security Card\n"
           "- Permanent Resident Card (Green Card)\n"
           "- Employment Authorization Document\n"
           "More info at USCIS.gov.")
uploaded_ids = st.file_uploader("Upload presented ID(s)", accept_multiple_files=True, type=['pdf', 'jpg', 'png'], help="Upload ID files used for I-9 verification.")

st.header("HR Certification")
hr_cert = st.text_input("HR Staff Name", help="Your name as the onboarding HR rep.")
notes = st.text_area("Internal Notes", help="Internal HR notes, optional.")
certify = st.checkbox("I certify that the above onboarding steps have been completed.", help="Required to complete the onboarding record.")

if st.button("Submit Onboarding Record"):
    if name and email and emp_id and department and manager and certify:
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
            "Emergency Contact": em_name,
            "Emergency Phone": em_phone,
            "Department": department,
            "Manager": manager,
            "Role": role,
            "W-4 Received": w4,
            "I-9 Complete": i9,
            "HR Certifier": hr_cert,
            "Notes": notes
        }

        csv_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/onboarded_employees.csv")
        df = pd.DataFrame([record])
        if os.path.exists(csv_path):
            df.to_csv(csv_path, mode='a', index=False, header=False)
        else:
            df.to_csv(csv_path, index=False)
        st.success("✅ Onboarding record saved.")
    else:
        st.error("❌ Please fill in all required fields and check certification.")
