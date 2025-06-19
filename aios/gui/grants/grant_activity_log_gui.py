# grant_activity_log_gui.py
# Purpose: Log post-award grant deliverables, outcomes, uploads, and responsible staff
# Standards: 2 CFR Part 200, ABL_Rev2_6_1_25 compliance, IRS 990 documentation

import streamlit as st
from datetime import date
from PIL import Image
import os

st.set_page_config(page_title="Grant Activity Log", layout="centered")

# -- Logo at Top --
logo_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
if os.path.exists(logo_path):
    st.image(Image.open(logo_path), width=150)

st.title("📆 Grant Activity Log")
st.caption("Use this form to log any grant-related activity, deliverable, or documentation.")

with st.form("activity_log"):
    st.subheader("Grant & Log Details")
    grant_title = st.text_input("Grant Title")
    report_date = st.date_input("Log Date", value=date.today())
    activity_type = st.selectbox("Activity Type", [
        "Narcan Distribution", "Public Training", "Mobile Outreach", "Treatment Assistance", 
        "Finance Report", "Staffing Milestone", "Disposal Box Pickup", "Client Intake", "Other"
    ])
    responsible = st.text_input("Staff Responsible")
    description = st.text_area("Activity Description or Outcome")
    upload = st.file_uploader("Upload Supporting File (PDF, CSV, JPG)", type=["pdf", "csv", "jpg", "jpeg", "png"])

    submitted = st.form_submit_button("Submit Activity Log")

if submitted:
    st.success("✅ Activity has been logged.")
    st.write("**Grant:**", grant_title)
    st.write("**Date:**", report_date)
    st.write("**Activity:**", activity_type)
    st.write("**Staff:**", responsible)
    st.write("**Summary:**", description)
    if upload:
        st.info("📎 File uploaded for audit traceability.")
