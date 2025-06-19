# employee_full_application_gui_v6.py
# Purpose: Streamlit GUI for full employment applications, including address and ID compliance guidance
# Standards: EEOC, I-9, W-4, HIPAA (if collected), GDPR, ISO 30414 (Human Capital Reporting)

import streamlit as st
import pandas as pd
import os
from datetime import date

st.set_page_config(page_title="Full Employment Application", layout="centered")

# Logo
st.image(os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png"), width=120)

st.title("📝 Full Employment Application")
st.markdown("Please complete all sections to be considered for employment.")

with st.form("full_application_form"):
    st.header("Contact Information")
    full_name = st.text_input("Full Name", help="Enter your legal first and last name.")
    email = st.text_input("Email", help="Used for communication and document processing.")
    phone = st.text_input("Cell Phone Number", help="Include area code.")
    allow_text = st.checkbox("📱 May we text you at this number?")
    street = st.text_input("Street Address", help="Enter your current street address.")
    city = st.text_input("City", help="Enter the city you reside in.")
    state = st.text_input("State", help="Enter your state abbreviation (e.g., FL).")
    zip_code = st.text_input("ZIP Code", help="5-digit ZIP code.")

    st.header("Education History")
    education_entries = []
    for i in range(1, 4):
        with st.expander(f"Education #{i}"):
            school = st.text_input(f"Most Recent School #{i}")
            degree = st.text_input(f"Degree or Certificate #{i}")
            graduation_year = st.text_input(f"Year Graduated #{i}")
            if school or degree or graduation_year:
                education_entries.append({
                    "School": school, "Degree": degree, "Year": graduation_year
                })

    st.header("Employment History")
    employment_entries = []
    for i in range(1, 4):
        with st.expander(f"Employer #{i}"):
            employer = st.text_input(f"Most Recent Employer #{i}")
            title = st.text_input(f"Job Title #{i}")
            duration = st.text_input(f"Employment Duration #{i}")
            responsibilities = st.text_area(f"Key Responsibilities #{i}")
            if employer or title or duration or responsibilities:
                employment_entries.append({
                    "Employer": employer,
                    "Title": title,
                    "Duration": duration,
                    "Responsibilities": responsibilities
                })

    st.header("References")
    reference_entries = []
    for i in range(1, 4):
        with st.expander(f"Reference #{i}"):
            ref_name = st.text_input(f"Reference Name #{i}")
            ref_contact = st.text_input(f"Reference Contact Info #{i}")
            if ref_name or ref_contact:
                reference_entries.append({
                    "Name": ref_name,
                    "Contact": ref_contact
                })

    st.header("Final Questions")
    work_auth = st.selectbox("Select your current U.S. work authorization status:", [
        "U.S. Citizen",
        "Permanent Resident (Green Card)",
        "Work Visa Holder",
        "Other (Please explain in resume)"
    ], help="Required to meet employment eligibility (I-9 requirements).")
    felony = st.radio("Have you ever been convicted of a felony?", ["No", "Yes"], help="Some positions may require background clearance.")
    confirm = st.checkbox("I confirm that the above information is true and complete.", help="Falsifying information may disqualify your application.")
    available_date = st.date_input("Date Available to Start Work", value=date.today(), help="Select the first day you're available to begin employment.")
    resume = st.file_uploader("Upload Your Resume (PDF preferred)", type=["pdf", "docx"], help="Optional resume upload to assist with screening.")

    # I-9 ID guidance tooltip info text
    st.markdown("### I-9 Compliance Acknowledgement ✅")
    st.markdown("""
<small><i>
To complete hiring, you must provide acceptable identification as defined by the U.S. Department of Homeland Security for I-9 verification. Acceptable combinations include:
<ul>
<li>Passport (alone)</li>
<li>OR Driver’s License <b>and</b> Social Security Card</li>
<li>OR Driver’s License <b>and</b> Birth Certificate</li>
<li>Permanent Resident Card</li>
<li>Other DHS-authorized documents</li>
</ul>
Documents must be valid and unexpired at time of hire.
</i></small>
""", unsafe_allow_html=True)

    submitted = st.form_submit_button("Submit Full Application")
    if submitted:
        data = {
            "Name": full_name,
            "Email": email,
            "Phone": phone,
            "Allow Text": "Yes" if allow_text else "No",
            "Street": street,
            "City": city,
            "State": state,
            "ZIP": zip_code,
            "Work Authorization": work_auth,
            "Felony": felony,
            "Confirmed": confirm,
            "Available Date": str(available_date),
        }

        # Save basic data to CSV
        save_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/data/hr/full_applicants.csv")
        df = pd.DataFrame([data])
        if os.path.exists(save_path):
            df.to_csv(save_path, mode='a', header=False, index=False)
        else:
            df.to_csv(save_path, index=False)

        st.success("✅ Full employment application submitted successfully.")
