import streamlit as st
import pandas as pd
import os
import sys

st.set_page_config(page_title="Employee Application", layout="wide")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from tools.shared_ui_components import (
    display_logo,
    display_abl_footer,
    display_gui_version,
    display_about_this_form,
    display_language_toggle_button,
    display_policy_assistant_button
)

# Top layout
cols = st.columns([6, 1, 1])
with cols[0]: display_logo()
with cols[1]: display_language_toggle_button()
with cols[2]: display_policy_assistant_button()

display_about_this_form(
    header="All applicants and HR onboarding reviewers",
    purpose="Submit a new employee application to begin onboarding.",
    usage="Complete all fields with accurate contact and background info. Hover over 🛈 icons for guidance.",
    routing="Data is reviewed by HR and added to the employee records system."
)

st.title("📋 Employee Application Form")

with st.form("application_form"):
    full_name = st.text_input("Full Name 🛈", help="Enter your full legal name.")
    email = st.text_input("Email Address 🛈", help="Provide a valid email address for contact.")
    phone = st.text_input("Phone Number 🛈", help="Primary number to reach you during onboarding.")
    start_date = st.date_input("Proposed Start Date 🛈", help="Preferred date to begin employment.")
    position = st.text_input("Position Applied For 🛈", help="Title or type of role you're applying for.")
    department = st.selectbox("Department 🛈", ["HR", "Outreach", "Operations", "IT", "Development"], help="Choose your target department.")
    notes = st.text_area("Additional Notes 🛈", help="Anything else you'd like HR to know.")
    submit = st.form_submit_button("Submit Application")

if submit:
    st.success(f"Application for {full_name} submitted.")

# Example application log
st.subheader("🗂️ Application Log (example)")
example = pd.DataFrame({
    "Name": ["J. Doe", "M. Garcia"],
    "Email": ["jdoe@example.com", "mgarcia@example.com"],
    "Position": ["Coordinator", "Field Staff"]
})
st.dataframe(example)

csv = example.to_csv(index=False).encode("utf-8")
st.download_button("📥 Export Application Log", data=csv, file_name="employee_application_log.csv")

# Footer
display_abl_footer()
display_gui_version("employee_application_gui.py", version="v3.1")
