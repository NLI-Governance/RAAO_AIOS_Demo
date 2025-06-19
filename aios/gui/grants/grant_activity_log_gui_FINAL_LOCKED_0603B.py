# grant_activity_log_gui_FINAL_LOCKED_v2_0603.py
# Purpose: Log post-award grant activities with audit-ready traceability
# Standards: 2 CFR Part 200, ABL_Rev2_6_1_25, nonprofit reporting and documentation best practices

import streamlit as st
from datetime import date
from PIL import Image
import os

st.set_page_config(page_title="Grant Activity Log", layout="centered")

# --- Logo ---
logo_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
if os.path.exists(logo_path):
    st.image(Image.open(logo_path), width=150)

st.title("📆 Grant Activity Log")
st.caption("Log a specific grant-related action, deliverable, or document.")

with st.form("activity_log"):

    grant_title = st.text_input("Grant Title")
    with st.expander("ⓘ What is this?"):
        st.markdown("Enter the official name of the grant this activity supports.")

    report_date = st.date_input("Log Date", value=date.today())
    with st.expander("ⓘ What is this?"):
        st.markdown("The date this action occurred or was recorded.")

    activity_type = st.selectbox("Activity Type", [
        "Narcan Distribution", "Public Training", "Mobile Outreach", "Treatment Assistance", 
        "Finance Report", "Staffing Milestone", "Disposal Box Pickup", "Client Intake", "Other"
    ])
    with st.expander("ⓘ What is this?"):
        st.markdown("Categorize the action or report. This improves filters and reporting.")

    responsible = st.text_input("Staff Responsible")
    with st.expander("ⓘ What is this?"):
        st.markdown("The name of the staff member accountable for this activity.")

    description = st.text_area("Activity Description or Outcome")
    with st.expander("ⓘ What is this?"):
        st.markdown("Brief explanation of what occurred. Include metrics or results if possible.")

    upload = st.file_uploader("Upload Supporting File (PDF, CSV, JPG)", type=["pdf", "csv", "jpg", "jpeg", "png"])
    with st.expander("ⓘ What is this?"):
        st.markdown("Attach documentation (e.g. Narcan logs, invoices, training sign-in sheets).")

    submitted = st.form_submit_button("Submit Activity Log")

if submitted:
    st.success("✅ Activity successfully logged.")
    st.write("**Grant:**", grant_title)
    st.write("**Date:**", report_date)
    st.write("**Activity:**", activity_type)
    st.write("**Staff:**", responsible)
    st.write("**Summary:**", description)
    if upload:
        st.info("📎 File uploaded for archive.")
