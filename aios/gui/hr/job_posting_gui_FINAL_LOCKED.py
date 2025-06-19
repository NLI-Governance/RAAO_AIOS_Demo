import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import date

st.image(str(Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png").expanduser()), width=100)
st.title("📢 Job Posting Entry")
st.markdown("Use this form to post a new job opportunity to the internal system.")

# Input fields with info icons
position_title = st.text_input("Position Title ℹ️", help="Official title of the position being offered.")
department = st.text_input("Department ℹ️", help="Which department this position falls under.")
job_type = st.selectbox("Job Type ℹ️", ["Full-Time", "Part-Time", "Temporary", "Internship", "Volunteer"], help="Nature of employment.")
location = st.text_input("Work Location (City, State) ℹ️", help="Enter city and state where the job is based.")
start_date = st.date_input("Start Date ℹ️", value=date.today(), help="Date the candidate is expected to start.")
salary_range = st.text_input("Salary or Hourly Range (e.g. $18–$25/hr) ℹ️", help="Use a range if available.")

benefits = st.text_area("Benefits Summary ℹ️", help="Summarize key medical, dental, PTO, or retirement benefits.")
job_description = st.text_area("Job Description and Duties ℹ️", height=200, help="Detailed description of responsibilities.")
qualifications = st.text_area("Required Qualifications ℹ️", height=100, help="List education, skills, certifications, and experience.")
application_deadline = st.date_input("Application Deadline ℹ️", help="Last date for accepting applications.")

uploaded_file = st.file_uploader("Upload Full Job Description (optional)", type=["pdf", "docx"], help="Attach a formal job posting document.")

# Submit logic
if st.button("Submit Job Posting"):
    csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/job_postings.csv").expanduser()
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    new_entry = {
        "Position Title": position_title,
        "Department": department,
        "Job Type": job_type,
        "Location": location,
        "Start Date": start_date.isoformat(),
        "Salary Range": salary_range,
        "Benefits": benefits,
        "Job Description": job_description,
        "Qualifications": qualifications,
        "Application Deadline": application_deadline.isoformat()
    }

    if csv_path.exists():
        df = pd.read_csv(csv_path)
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    else:
        df = pd.DataFrame([new_entry])

    df.to_csv(csv_path, index=False)
    st.success("✅ Job posting submitted and saved.")
