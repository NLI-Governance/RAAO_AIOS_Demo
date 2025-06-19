# grant_proposal_intake_gui_FINAL_LOCKED.py
# Purpose: Intake GUI for grant opportunities in pre-application or active application stage
# Standards: 2 CFR Part 200, nonprofit best practices, ISO 9001 traceability

import streamlit as st
from datetime import date
from PIL import Image
import os

st.set_page_config(page_title="Grant Proposal Intake", layout="centered")

# --- LOGO ---
logo_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
if os.path.exists(logo_path):
    st.image(Image.open(logo_path), width=150)

st.title("📝 Grant Proposal Intake")
st.caption("Use this form to record early-stage grant opportunities prior to submission.")

with st.form("grant_intake"):
    st.subheader("Opportunity Details")
    grant_name = st.text_input("Grant Title")
    grantor = st.text_input("Funding Organization or Agency")
    grant_id = st.text_input("Grant ID / Reference Code (if any)")
    funding_type = st.selectbox("Funding Type", ["Federal", "State", "Private", "Foundation", "Other"])
    recurring = st.selectbox("Is this recurring?", ["No", "Yes – Annual", "Yes – Multi-Year"])
    fiscal_year = st.selectbox("Target Fiscal Year", ["2025", "2026", "2027"])

    st.subheader("Submission Planning")
    internal_owner = st.text_input("Internal Owner or Lead")
    submission_deadline = st.date_input("Submission Deadline", value=date.today())
    estimated_award = st.text_input("Estimated Grant Value ($)")
    purpose = st.text_area("Brief Description of Grant Purpose, Services, or Target Populations")

    st.subheader("Grant Files")
    upload_files = st.file_uploader("Upload Application Docs (RFPs, LOIs, Drafts)", accept_multiple_files=True)

    submitted = st.form_submit_button("Submit Intake Record")

if submitted:
    st.success("✅ Grant intake has been recorded.")
    st.write("**Grant:**", grant_name)
    st.write("**Funder:**", grantor)
    st.write("**Deadline:**", submission_deadline)
    st.write("**Purpose:**", purpose)
    if upload_files:
        st.info(f"{len(upload_files)} file(s) uploaded.")
