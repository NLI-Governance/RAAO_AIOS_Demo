# volunteer_onboarding_gui_v2.py
# Purpose: Onboard community volunteers with essential fields
# Standards: EEOC, HIPAA (if handling client info), ISO 9001 (HR process), ABL Rev2

import streamlit as st
import csv
import os
from datetime import date

st.set_page_config(page_title="Volunteer Onboarding", layout="centered")

LOGO_PATH = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
DATA_PATH = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/data/hr/volunteers.csv")

if os.path.exists(LOGO_PATH):
    st.image(LOGO_PATH, width=120)

st.title("🤝 Volunteer Onboarding Form")

# --- Volunteer Info ---
st.subheader("Volunteer Details")
name = st.text_input("Full Name", help="Volunteer’s full legal name.")
email = st.text_input("Email", help="Primary email for contact.")
phone = st.text_input("Phone", help="Cell phone number for contact.")
start_date = st.date_input("Start Date", value=date.today(), help="Date volunteer service begins.")
vol_id = st.text_input("Volunteer ID", help="Internal ID for tracking volunteers.")

# --- Address Info ---
street = st.text_input("Street Address", help="Volunteer’s home address.")
city = st.text_input("City", help="City of residence.")
state = st.text_input("State", help="Two-letter state abbreviation.")
zip_code = st.text_input("ZIP Code", help="5-digit postal code.")

# --- Emergency Contact ---
st.subheader("Emergency Contact")
em_name = st.text_input("Emergency Contact Name", help="Name of emergency contact.")
em_phone = st.text_input("Emergency Contact Phone", help="Phone number for emergency contact.")

# --- Assignment Info ---
st.subheader("Volunteer Role & Department")
department = st.text_input("Assigned Department", help="Department or team the volunteer will support.")
supervisor = st.text_input("Supervisor", help="Who will oversee the volunteer?")
role_desc = st.text_area("Volunteer Duties", help="Brief description of expected duties or role.")

# --- Agreement Section ---
st.subheader("Participation Agreement")
code_of_conduct = st.checkbox("I agree to follow RAAO's Code of Conduct.", help="Required to volunteer.")
confidentiality = st.checkbox("I agree to maintain confidentiality when working with clients or files.", help="Required for sensitive tasks.")
certifier = st.text_input("Completed by HR or Coordinator", help="Person completing this form.")
confirm = st.checkbox("I confirm all information is complete and correct.", help="Required to submit.")

# --- Submission ---
if st.button("Submit Volunteer Record"):
    if all([name, email, phone, vol_id, department, code_of_conduct, confidentiality, confirm]):
        record = {
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Start Date": start_date.strftime("%Y-%m-%d"),
            "Volunteer ID": vol_id,
            "Street": street,
            "City": city,
            "State": state,
            "ZIP": zip_code,
            "Emergency Contact": em_name,
            "Emergency Phone": em_phone,
            "Department": department,
            "Supervisor": supervisor,
            "Role Description": role_desc,
            "Code of Conduct": code_of_conduct,
            "Confidentiality Agreement": confidentiality,
            "Certified By": certifier
        }

        file_exists = os.path.exists(DATA_PATH)
        with open(DATA_PATH, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=record.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(record)

        st.success("✅ Volunteer record saved successfully.")
    else:
        st.error("❌ Please complete all required fields and check agreements before submitting.")
