import streamlit as st
import pandas as pd
from datetime import date, datetime
from PIL import Image
import os

st.set_page_config(page_title="Full Employment Application", layout="wide")

# ---- Branding Logo ----
logo_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.image(logo, width=200)

st.title("Full Employment Application")

def circular_info(text):
    st.markdown(f'<span style="border-radius: 50%; background:#ccc; padding: 3px 9px;">i</span> {text}', unsafe_allow_html=True)

# ---- Personal Info ----
st.header("Personal Information")
with st.form("personal_info"):
    col1, col2 = st.columns(2)
    first_name = col1.text_input("First Name")
    last_name = col2.text_input("Last Name")
    phone = col1.text_input("Phone Number")
    email = col2.text_input("Email Address")
    address = st.text_input("Mailing Address")
    circular_info("Enter your contact info so HR can reach you.")
    submitted_personal = st.form_submit_button("Save Personal Info")

# ---- Employment History ----
st.header("Employment History (Last 3 Employers)")
job_entries = []
for i in range(1, 4):
    st.markdown(f"🔽 **Click to expand and complete Job #{i} details:**")
    with st.expander(f"Job #{i}"):
        job_entries.append({
            "Employer": st.text_input(f"Employer Name #{i}"),
            "Address": st.text_input(f"Employer Address #{i}"),
            "Phone": st.text_input(f"Employer Phone #{i}"),
            "Email": st.text_input(f"Employer Email #{i}"),
            "Website": st.text_input(f"Company Website #{i}"),
            "Supervisor": st.text_input(f"Supervisor Name #{i}"),
            "Position": st.text_input(f"Position Held #{i}"),
            "Start Date": st.date_input(f"Start Date #{i}", key=f"start_{i}"),
            "End Date": st.date_input(f"End Date #{i}", key=f"end_{i}"),
            "Reason for Leaving": st.text_input(f"Reason for Leaving #{i}")
        })

# ---- Education ----
st.header("Education History")
education_entries = []
for i in range(1, 4):
    st.markdown(f"🔽 **Click to expand and complete Education #{i}:**")
    with st.expander(f"Education #{i}"):
        education_entries.append({
            "School": st.text_input(f"School Name #{i}"),
            "Degree": st.text_input(f"Degree or Certificate #{i}"),
            "Field": st.text_input(f"Field of Study #{i}"),
            "Start Date": st.date_input(f"Start Date #{i}", key=f"edu_start_{i}"),
            "End Date": st.date_input(f"End Date #{i}", key=f"edu_end_{i}")
        })

# ---- References ----
st.header("References (3 Required)")
refs = []
for i in range(1, 4):
    st.markdown(f"🔽 **Click to expand and complete Reference #{i}:**")
    with st.expander(f"Reference #{i}"):
        refs.append({
            "Name": st.text_input(f"Name #{i}", key=f"ref_name_{i}"),
            "Phone": st.text_input(f"Phone #{i}", key=f"ref_phone_{i}"),
            "Email": st.text_input(f"Email #{i}", key=f"ref_email_{i}"),
            "Relationship": st.text_input(f"Relationship #{i}", key=f"ref_relation_{i}"),
            "Years Known": st.text_input(f"Years Known #{i}", key=f"ref_years_{i}")
        })

# ---- Availability and Authorization ----
st.header("Availability")
st.markdown("📅 **Choose your available start date and work type:**")
available_start = st.date_input("Available Start Date", min_value=date.today())
work_type = st.radio("Type of Work Desired", ["Full-Time", "Part-Time", "Temporary"])

st.markdown("✅ **Check all that apply below:**")
us_auth = st.checkbox("I am legally authorized to work in the United States.")
convicted_felon = st.checkbox("I have been convicted of a felony.", value=False)
felony_explanation = ""
if convicted_felon:
    felony_explanation = st.text_area("Please explain:")

# ---- Demographic Data ----
st.header("Voluntary Demographic Data")
st.markdown("📝 **Select from the dropdowns below (optional):**")
gender = st.selectbox("Gender", ["Prefer not to say", "Male", "Female", "Non-binary", "Other"])
ethnicity = st.selectbox("Ethnicity", ["Prefer not to say", "Hispanic or Latino", "White", "Black or African American", "Asian", "Native American", "Other"])
veteran = st.selectbox("Are you a veteran?", ["Prefer not to say", "Yes", "No"])
disability = st.selectbox("Do you identify as having a disability?", ["Prefer not to say", "Yes", "No"])

# ---- Certification ----
st.header("Certification")
st.markdown("✍️ **Type your name and certify before submitting:**")
signed_name = st.text_input("Type your full name to sign")
agree = st.checkbox("I certify that the above information is true and complete.")

# ---- Submission and CSV Export ----
if st.button("Submit Full Application"):
    if agree and signed_name:
        record = {
            "Timestamp": datetime.now().isoformat(),
            "First Name": first_name,
            "Last Name": last_name,
            "Phone": phone,
            "Email": email,
            "Address": address,
            "Available Start": available_start,
            "Work Type": work_type,
            "US Authorized": us_auth,
            "Felony": convicted_felon,
            "Felony Explanation": felony_explanation,
            "Gender": gender,
            "Ethnicity": ethnicity,
            "Veteran": veteran,
            "Disability": disability,
            "Signed Name": signed_name
        }

        for idx, job in enumerate(job_entries, 1):
            for key, val in job.items():
                record[f"Job{idx}_{key}"] = val

        for idx, edu in enumerate(education_entries, 1):
            for key, val in edu.items():
                record[f"Edu{idx}_{key}"] = val

        for idx, ref in enumerate(refs, 1):
            for key, val in ref.items():
                record[f"Ref{idx}_{key}"] = val

        df = pd.DataFrame([record])
        csv_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/data/hr/applicants.csv")
        folder_path = os.path.dirname(csv_path)
        os.makedirs(folder_path, exist_ok=True)

        if os.path.exists(csv_path):
            df.to_csv(csv_path, mode='a', index=False, header=False)
        else:
            df.to_csv(csv_path, index=False)

        st.success("Application submitted and saved.")
    else:
        st.error("You must sign and certify before submitting.")
