# PART 1: Terminal Command
# mkdir -p ~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/gui/hr && \
# nano ~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/gui/hr/employee_full_application_gui_v5.py

# PART 2: Python Script
import streamlit as st
import pandas as pd
import os
from datetime import date
from pathlib import Path

st.set_page_config(page_title="Full Employment Application", layout="centered")

# Logo
logo_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
if os.path.exists(logo_path):
    st.image(logo_path, width=120)

st.title("📝 Full Employment Application")
st.caption("Please complete all sections to be considered for employment.")

# Contact Info
st.subheader("Contact Information")
col1, col2 = st.columns([3,1])
with col1:
    full_name = st.text_input("Full Name")
with col2:
    st.markdown("ⓘ Enter your full legal name.")

col1, col2 = st.columns([3,1])
with col1:
    email = st.text_input("Email")
with col2:
    st.markdown("ⓘ Provide a working email address.")

col1, col2 = st.columns([3,1])
with col1:
    phone = st.text_input("Cell Phone Number")
with col2:
    st.markdown("ⓘ Used for application follow-up.")

text_ok = st.checkbox("📲 May we text you at this number?")

col1, col2 = st.columns([3,1])
with col1:
    street = st.text_input("Street Address")
with col2:
    st.markdown("ⓘ Include apartment/unit number if needed.")

city = st.text_input("City")
state = st.text_input("State")
zip_code = st.text_input("ZIP Code")

# Emergency Contact
st.subheader("Emergency Contact")
col1, col2 = st.columns([3,1])
with col1:
    em_contact_name = st.text_input("Emergency Contact Name")
with col2:
    st.markdown("ⓘ Who should we call in an emergency?")

col1, col2 = st.columns([3,1])
with col1:
    em_contact_phone = st.text_input("Emergency Contact Phone")
with col2:
    st.markdown("ⓘ Provide a direct phone number.")

# Education
st.subheader("Education History")
edu = []
for i in range(3):
    with st.expander(f"Education #{i+1}"):
        school = st.text_input(f"School Name #{i+1}")
        degree = st.text_input(f"Degree or Certificate #{i+1}")
        grad_year = st.text_input(f"Year Graduated #{i+1}")
        edu.extend([school, degree, grad_year])
st.caption("Limit 3 entries max")

# Employment
st.subheader("Employment History")
jobs = []
for i in range(3):
    with st.expander(f"Employer #{i+1}"):
        emp = st.text_input(f"Employer Name #{i+1}")
        title = st.text_input(f"Job Title #{i+1}")
        duration = st.text_input(f"Employment Duration #{i+1}")
        duties = st.text_area(f"Key Responsibilities #{i+1}")
        jobs.extend([emp, title, duration, duties])
st.caption("Limit 3 entries max")

# References
st.subheader("References")
refs = []
for i in range(3):
    with st.expander(f"Reference #{i+1}"):
        name = st.text_input(f"Reference Name #{i+1}")
        contact = st.text_input(f"Reference Contact Info #{i+1}")
        refs.extend([name, contact])
st.caption("Limit 3 entries max")

# Final Questions
st.subheader("Final Questions")
auth_status = st.selectbox("Work Authorization Status", ["U.S. Citizen", "Permanent Resident", "Work Visa / Other"])
felony = st.radio("Felony Conviction?", ["No", "Yes"])

with st.expander("What documents do I need for the I-9?"):
    st.markdown("""
    To complete an I-9, you must bring one of the following:
    - U.S. Passport or Passport Card
    - Permanent Resident Card (Green Card)
    - OR a combination of:
        - State ID or Driver's License
        - AND Social Security Card or Birth Certificate
    """)
i9_ack = st.checkbox("I understand I must provide I-9 and W-4 documentation.")

avail_date = st.date_input("Available Start Date", min_value=date.today())
resume = st.file_uploader("Upload Resume (PDF/DOC/DOCX)", type=["pdf", "doc", "docx"])
confirm = st.checkbox("I confirm the information above is true and complete.")

# Submission
if st.button("Submit Application"):
    if not (full_name and email and phone and i9_ack and confirm):
        st.error("Please complete all required fields and confirm.")
    else:
        row = [
            full_name, email, phone, text_ok, street, city, state, zip_code,
            em_contact_name, em_contact_phone
        ] + edu + jobs + refs + [auth_status, felony, avail_date.isoformat(), resume.name if resume else "", i9_ack, confirm]

        headers = ["full_name", "email", "cell", "text_ok", "street", "city", "state", "zip",
                   "emergency_contact_name", "emergency_contact_phone"]
        for i in range(1, 4):
            headers += [f"education_{i}_school", f"education_{i}_degree", f"education_{i}_year"]
        for i in range(1, 4):
            headers += [f"employment_{i}_employer", f"employment_{i}_title", f"employment_{i}_duration", f"employment_{i}_responsibilities"]
        for i in range(1, 4):
            headers += [f"reference_{i}_name", f"reference_{i}_contact"]
        headers += ["authorization_status", "felony_status", "available_date", "resume_uploaded", "i9_ack", "certify"]

        path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/data/hr/employee_full_applications.csv")
        with open(path, "a", newline="") as f:
            pd.DataFrame([row], columns=headers).to_csv(f, header=not os.path.exists(path), index=False)

        st.success("✅ Application submitted successfully.")

# PART 3: Run the script
# streamlit run ~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/gui/hr/employee_full_application_gui_v5.py

