# employee_application_gui_FINAL_LOCKED_0604B.py
# Purpose: Applicant-facing basic employment application
# Standards: EEOC, FMLA, I-9/W-4 readiness, ABL_Rev2_6_1_25

import streamlit as st
import os
from PIL import Image

st.set_page_config(page_title="Employment Application", layout="centered")

# Logo
logo_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
if os.path.exists(logo_path):
    st.image(Image.open(logo_path), width=150)

st.title("📄 Employment Application")
st.caption("Please complete the application form. Required fields marked.")

with st.form("job_application_form"):

    full_name = st.text_input("Full Name", help="Enter your legal first and last name.")
    phone = st.text_input("Phone Number", help="Enter a valid contact number.")
    email = st.text_input("Email Address", help="Use an address where you can be reached.")

    position = st.text_input("Position Applying For", help="Enter the role or title you are applying to.")
    availability = st.text_area("Availability / Preferred Schedule", help="Include days and hours you are available to work.")

    eligible = st.radio("Are you eligible to work in the United States?", ["Yes", "No"],
                        help="This is required for federal employment documentation (I-9).")

    resume = st.file_uploader("Upload Resume (optional)", type=["pdf", "doc", "docx"],
                              help="Attach your resume or work history, if available.")

    i9_ack = st.checkbox("I understand I will need to provide employment eligibility documents (I-9/W-4)",
                         help="This includes a government-issued ID and social security card or equivalent.")

    submitted = st.form_submit_button("Submit Application")

if submitted:
    if not i9_ack:
        st.warning("✅ You must acknowledge the I-9/W-4 requirement to submit.")
    else:
        st.success("✅ Application submitted successfully.")
        st.write("**Name:**", full_name)
        st.write("**Phone:**", phone)
        st.write("**Email:**", email)
        st.write("**Position:**", position)
        st.write("**Eligible to Work:**", eligible)
        if resume:
            st.info(f"📎 Resume uploaded: {resume.name}")
