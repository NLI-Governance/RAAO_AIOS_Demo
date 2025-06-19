# employee_full_application_gui_FINAL_LOCKED_0604B.py
# Purpose: Detailed employee application with extended sections and hover tooltips
# Standards: EEOC, ABL_Rev2_6_1_25, I-9/W-4, FMLA

import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Full Employment Application", layout="centered")

# Logo
logo_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
if os.path.exists(logo_path):
    st.image(Image.open(logo_path), width=150)

st.title("📝 Full Employment Application")
st.caption("Please complete all sections to be considered for employment.")

with st.form("full_application"):

    st.subheader("Contact Information")
    name = st.text_input("Full Name", help="First and last name, as shown on your ID.")
    email = st.text_input("Email", help="Best email for communication.")
    phone = st.text_input("Phone Number", help="Primary number to reach you.")

    st.subheader("Education History")
    school = st.text_input("Most Recent School", help="Enter the name of the most recent school you attended.")
    degree = st.text_input("Degree or Certificate", help="Type of diploma, certification, or area of study.")
    graduation_year = st.text_input("Year Graduated", help="Enter the year you completed this program.")

    st.subheader("Employment History")
    employer = st.text_input("Most Recent Employer", help="Company name or organization.")
    job_title = st.text_input("Job Title", help="What was your role at this company?")
    duration = st.text_input("Employment Duration", help="Approximate dates you worked (e.g. 2021–2023).")
    responsibilities = st.text_area("Key Responsibilities", help="Describe your responsibilities at that job.")

    st.subheader("References")
    ref_name = st.text_input("Reference Name", help="Enter someone familiar with your work.")
    ref_contact = st.text_input("Reference Contact Info", help="Email or phone number of your reference.")

    st.subheader("Final Questions")
    eligible = st.radio("Are you legally authorized to work in the U.S.?", ["Yes", "No"],
                        help="This is required for I-9/W-4 eligibility.")
    conviction = st.radio("Have you ever been convicted of a felony?", ["No", "Yes"],
                          help="Answering 'Yes' does not automatically disqualify you.")

    st.checkbox("I confirm that the above information is true and complete.", key="confirm",
                help="Providing false information may disqualify your application.")

    submitted = st.form_submit_button("Submit Full Application")

if submitted:
    st.success("✅ Application submitted successfully.")
    st.write("Thank you,", name)
