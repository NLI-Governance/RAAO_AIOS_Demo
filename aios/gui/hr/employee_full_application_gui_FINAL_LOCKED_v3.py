# employee_full_application_gui_FINAL_LOCKED_v3.py
# Purpose: Final employment application intake form with max-entry limits and CSV-ready format
# Standards: EEOC, ADA, IRS W-4 onboarding, FCRA (reference screening), ABL standard icon help format

import streamlit as st
import pandas as pd
import datetime
from pathlib import Path

st.set_page_config(page_title="Full Employment Application", layout="centered")

# Logo
st.image(str(Path.home()) + "/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png", width=120)

st.title("📝 Full Employment Application")
st.caption("Please complete all sections to be considered for employment.")

# Initialize session state lists if not present
for key in ["schools", "jobs", "refs"]:
    if key not in st.session_state:
        st.session_state[key] = []

# Contact Info
st.subheader("Contact Information")
full_name = st.text_input("Full Name", help="Your legal full name.")
email = st.text_input("Email", help="Your personal or work email address.")
cell_phone = st.text_input("Cell Phone Number", help="Used to contact you about your application.")
text_ok = st.checkbox("📲 May we text you at this number?")

st.text_input("Street Address", key="street", help="Number and street name where you currently reside.")
st.text_input("City", key="city", help="City where you currently reside.")
st.text_input("State", key="state", help="Enter two-letter state code (e.g., FL).")
st.text_input("ZIP Code", key="zip", help="Five-digit postal code.")

# Education History
st.subheader("Education History")
if len(st.session_state.schools) < 3:
    if st.button("+ Add Another School"):
        st.session_state.schools.append(f"School #{len(st.session_state.schools)+1}")

for i, school in enumerate(st.session_state.schools):
    st.text_input(f"School Name #{i+1}", key=f"school_name_{i}", help="Name of institution attended.")
    st.text_input(f"Degree or Certificate #{i+1}", key=f"degree_{i}", help="What credential did you earn?")
    st.text_input(f"Graduation Year #{i+1}", key=f"grad_year_{i}", help="When did you graduate or finish?")

# Employment History
st.subheader("Employment History")
if len(st.session_state.jobs) < 3:
    if st.button("+ Add Another Employer"):
        st.session_state.jobs.append(f"Employer #{len(st.session_state.jobs)+1}")

for i, job in enumerate(st.session_state.jobs):
    st.text_input(f"Employer Name #{i+1}", key=f"emp_name_{i}", help="Most recent employer or company.")
    st.text_input(f"Job Title #{i+1}", key=f"title_{i}", help="Your role or position.")
    st.text_input(f"Employment Duration #{i+1}", key=f"duration_{i}", help="e.g., Jan 2022 – Apr 2023.")
    st.text_area(f"Key Responsibilities #{i+1}", key=f"duties_{i}", help="Brief summary of your responsibilities.")

# References
st.subheader("References")
if len(st.session_state.refs) < 3:
    if st.button("+ Add Another Reference"):
        st.session_state.refs.append(f"Reference #{len(st.session_state.refs)+1}")

for i, ref in enumerate(st.session_state.refs):
    st.text_input(f"Reference Name #{i+1}", key=f"ref_name_{i}", help="Full name of reference.")
    st.text_input(f"Reference Contact Info #{i+1}", key=f"ref_contact_{i}", help="Phone number or email.")

# Final Questions
st.subheader("Final Questions")
auth_status = st.selectbox(
    "Select your current U.S. work authorization status:",
    ["U.S. Citizen", "Permanent Resident (Green Card)", "Work Visa / Other"],
    help="Used for compliance with federal employment verification rules."
)
felony = st.radio("Have you ever been convicted of a felony?", ["No", "Yes"], help="Required by company policy.")

confirm = st.checkbox("I confirm that the above information is true and complete.", help="Required to submit application.")

# Save
if st.button("Submit Full Application") and confirm:
    data = {
        "Full Name": full_name,
        "Email": email,
        "Phone": cell_phone,
        "Text OK": "Yes" if text_ok else "No",
        "Street": st.session_state.street,
        "City": st.session_state.city,
        "State": st.session_state.state,
        "ZIP": st.session_state.zip,
        "Authorization": auth_status,
        "Felony": felony,
        "Submission Date": datetime.datetime.now().isoformat()
    }

    for i in range(len(st.session_state.schools)):
        data[f"School {i+1}"] = st.session_state[f"school_name_{i}"]
        data[f"Degree {i+1}"] = st.session_state[f"degree_{i}"]
        data[f"Grad Year {i+1}"] = st.session_state[f"grad_year_{i}"]

    for i in range(len(st.session_state.jobs)):
        data[f"Employer {i+1}"] = st.session_state[f"emp_name_{i}"]
        data[f"Title {i+1}"] = st.session_state[f"title_{i}"]
        data[f"Duration {i+1}"] = st.session_state[f"duration_{i}"]
        data[f"Duties {i+1}"] = st.session_state[f"duties_{i}"]

    for i in range(len(st.session_state.refs)):
        data[f"Reference {i+1}"] = st.session_state[f"ref_name_{i}"]
        data[f"Reference Contact {i+1}"] = st.session_state[f"ref_contact_{i}"]

    df = pd.DataFrame([data])
    csv_path = Path.home() / "Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_full_applications.csv"
    df.to_csv(csv_path, mode='a', header=not csv_path.exists(), index=False)
    st.success("✅ Application submitted successfully.")
