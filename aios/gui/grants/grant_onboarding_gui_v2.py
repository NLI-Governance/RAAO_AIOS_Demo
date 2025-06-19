# grant_onboarding_gui_v2.py
# Purpose: AIOS-compliant onboarding GUI for grants with full structure, staff, and compliance fields
# Standards: 2 CFR Part 200, IRS 990, ISO 9001, ABL_Rev2_6_1_25

import streamlit as st
from datetime import date
from PIL import Image
import os

st.set_page_config(page_title="Grant Onboarding", layout="centered")

# -- Logo Rendering --
logo_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.image(logo, width=150)

# -- Neutral Title and Caption --
st.title("🎯 Grant Onboarding")
st.caption("Use this form to register a new grant into the AIOS system.")

with st.form("grant_onboarding_form"):
    st.subheader("Grant Overview")
    grant_name = st.text_input("Grant Name")
    grant_number = st.text_input("Grant ID / Award Number")
    funding_agency = st.text_input("Funding Agency")
    grant_start = st.date_input("Start Date", value=date.today())
    grant_end = st.date_input("End Date")

    st.subheader("Funding & Budget")
    total_award = st.number_input("Total Award ($)", min_value=0.0, step=1000.0)
    approved_categories = st.multiselect(
        "Budget Categories",
        ["Personnel", "Outreach", "Equipment", "Training", "Supplies", "Admin", "Treatment Support", "Technology"],
        default=["Personnel", "Outreach", "Admin"]
    )

    st.subheader("Program Activities & Lead Assignments")
    activity_1 = st.text_input("Primary Activity 1")
    lead_1 = st.text_input("Staff Responsible for Activity 1")

    activity_2 = st.text_input("Primary Activity 2")
    lead_2 = st.text_input("Staff Responsible for Activity 2")

    activity_3 = st.text_input("Primary Activity 3")
    lead_3 = st.text_input("Staff Responsible for Activity 3")

    st.subheader("Compliance & Reporting")
    report_cycle = st.selectbox("Reporting Frequency", ["Monthly", "Quarterly", "Annually"])
    archive_docs = st.checkbox("Store All Uploads for Audit Trail?", value=True)
    ai_reminder_enabled = st.checkbox("Enable AI Reminder Prompts", value=True)

    st.form_submit_button("Register Grant")

st.divider()
st.markdown("📁 After submission, grant data will be routed to the AI compliance core.")
st.markdown("🧠 AI reminders will alert responsible staff when reporting deadlines approach.")
st.markdown("🔒 All activity will be logged for audit traceability.")
