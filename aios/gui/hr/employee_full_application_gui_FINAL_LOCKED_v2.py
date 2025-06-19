#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# employee_full_application_gui_FINAL_LOCKED_v3.py
# Purpose: Streamlit GUI for collecting full employment application data
# Standards: EEOC, ADA, IRS W-4, DHS I-9, ABL data structure standards

import streamlit as st
import pandas as pd
from datetime import date
import os

st.set_page_config(page_title="Full Employment Application", page_icon="📝", layout="centered")

LOGO_PATH = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
if os.path.exists(LOGO_PATH):
    st.image(LOGO_PATH, width=120)

st.title("📝 Full Employment Application")
st.markdown("Please complete all sections to be considered for employment.")

st.subheader("Contact Information")
full_name = st.text_input("Full Name", help="Enter your legal first and last name.")
email = st.text_input("Email", help="Provide your current email address.")
phone = st.text_input("Cell Phone Number", help="Use your mobile number for contact.")
allow_text = st.checkbox("May we text you at this number?", value=True)
street_address = st.text_input("Street Address", help="Include apartment or unit number if applicable.")
city = st.text_input("City")
state = st.text_input("State")
zip_code = st.text_input("ZIP Code")

st.subheader("Education History")
education_entries = []
if "education_count" not in st.session_state:
    st.session_state.education_count = 1

for i in range(st.session_state.education_count):
    with st.expander(f"Education #{i+1}"):
        school = st.text_input(f"School Name #{i+1}", key=f"school_{i}")
        degree = st.text_input(f"Degree or Certificate #{i+1}", key=f"degree_{i}")
        year = st.text_input(f"Year Graduated #{i+1}", key=f"year_{i}")
        education_entries.append((school, degree, year))

if st.button("➕ Add Another School"):
    st.session_state.education_count += 1
    st.experimental_rerun()

st.subheader("Employment History")
employment_entries = []
if "job_count" not in st.session_state:
    st.session_state.job_count = 1

for i in range(st.session_state.job_count):
    with st.expander(f"Employer #{i+1}"):
        employer = st.text_input(f"Employer Name #{i+1}", key=f"employer_{i}")
        job_title = st.text_input(f"Job Title #{i+1}", key=f"job_{i}")
        duration = st.text_input(f"Employment Duration #{i+1}", key=f"duration_{i}")
        responsibilities = st.text_area(f"Key Responsibilities #{i+1}", key=f"resp_{i}")
        employment_entries.append((employer, job_title, duration, responsibilities))

if st.button("➕ Add Another Employer"):
    st.session_state.job_count += 1
    st.experimental_rerun()

st.subheader("References")
reference_entries = []
if "ref_count" not in st.session_state:
    st.session_state.ref_count = 1

for i in range(st.session_state.ref_count):
    with st.expander(f"Reference #{i+1}"):
        ref_name = st.text_input(f"Reference Name #{i+1}", key=f"ref_name_{i}")
        ref_contact = st.text_input(f"Reference Contact Info #{i+1}", key=f"ref_contact_{i}")
        reference_entries.append((ref_name, ref_contact))

if st.button("➕ Add Another Reference"):
    st.session_state.ref_count += 1
    st.experimental_rerun()

st.subheader("Final Questions")
auth_status = st.selectbox("Select your current U.S. work authorization status:",
                            ["U.S. Citizen", "Permanent Resident (Green Card)", "Work Visa Holder"],
                            help="Choose the option that matches your legal right to work.")
has_felony = st.radio("Have you ever been convicted of a felony?", ["No", "Yes"], index=0)
confirm = st.checkbox("I confirm that the above information is true and complete.", help="This serves as your digital signature.")

# Submission and Save to CSV
if st.button("Submit Full Application"):
    if confirm:
        data = {
            "Full Name": full_name,
            "Email": email,
            "Phone": phone,
            "Text OK": allow_text,
            "Street Address": street_address,
            "City": city,
            "State": state,
            "ZIP Code": zip_code,
            "Authorization Status": auth_status,
            "Felony Conviction": has_felony,
            "Submitted Date": str(date.today())
        }

        # Combine education
        for idx, (school, degree, year) in enumerate(education_entries, start=1):
            data[f"School #{idx}"] = school
            data[f"Degree #{idx}"] = degree
            data[f"Grad Year #{idx}"] = year

        # Combine employment
        for idx, (employer, job_title, duration, responsibilities) in enumerate(employment_entries, start=1):
            data[f"Employer #{idx}"] = employer
            data[f"Job Title #{idx}"] = job_title
            data[f"Duration #{idx}"] = duration
            data[f"Responsibilities #{idx}"] = responsibilities

        # Combine references
        for idx, (ref_name, ref_contact) in enumerate(reference_entries, start=1):
            data[f"Reference #{idx}"] = ref_name
            data[f"Reference Contact #{idx}"] = ref_contact

        save_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/data/hr/employee_full_applications.csv")
        df = pd.DataFrame([data])
        if not os.path.exists(save_path):
            df.to_csv(save_path, index=False)
        else:
            df.to_csv(save_path, mode='a', header=False, index=False)

        st.success("✅ Application submitted successfully.")
    else:
        st.warning("You must confirm the accuracy of the information before submitting.")

