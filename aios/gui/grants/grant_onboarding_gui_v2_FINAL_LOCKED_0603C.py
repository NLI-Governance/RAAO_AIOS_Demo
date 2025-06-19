# grant_onboarding_gui_v2_FINAL_LOCKED_0603B.py
# Purpose: Post-award grant onboarding and structural setup for tracking
# Standards: 2 CFR Part 200, ABL_Rev2_6_1_25, IRS/OMB reporting alignment

import streamlit as st
from datetime import date
from PIL import Image
import os

st.set_page_config(page_title="Grant Onboarding", layout="centered")

# --- Logo Rendering ---
logo_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
if os.path.exists(logo_path):
    st.image(Image.open(logo_path), width=150)

st.title("🎯 Grant Onboarding")
st.caption("Use this form to register a new awarded grant into the AIOS system.")

with st.form("grant_onboarding_form"):

    st.subheader("Grant Overview")

    grant_name = st.text_input("Grant Name")
    with st.expander("ⓘ What is this?"):
        st.markdown("Enter the full official title of the awarded grant.")

    grant_number = st.text_input("Grant ID / Award Number")
    with st.expander("ⓘ What is this?"):
        st.markdown("Use any reference number provided by the grantor (federal tracking ID, internal record, etc.).")

    funding_agency = st.text_input("Funding Agency")
    with st.expander("ⓘ What is this?"):
        st.markdown("Enter the organization or agency that issued the award.")

    grant_start = st.date_input("Start Date", value=date.today())
    with st.expander("ⓘ What is this?"):
        st.markdown("Date the grant becomes active for spending or reporting.")

    grant_end = st.date_input("End Date")
    with st.expander("ⓘ What is this?"):
        st.markdown("Final day the grant is active. After this, spending and activity are closed.")

    st.subheader("Funding & Budget")

    total_award = st.number_input("Total Award ($)", min_value=0.0, step=1000.0)
    with st.expander("ⓘ What is this?"):
        st.markdown("Enter the full dollar amount awarded for this grant.")

    approved_categories = st.multiselect(
        "Budget Categories",
        ["Personnel", "Outreach", "Equipment", "Training", "Supplies", "Admin", "Treatment Support", "Technology"],
        default=["Personnel", "Outreach", "Admin"]
    )
    with st.expander("ⓘ What is this?"):
        st.markdown("Select the major expense categories approved for use in this grant.")

    st.subheader("Program Activities & Lead Assignments")

    activity_1 = st.text_input("Primary Activity 1")
    lead_1 = st.text_input("Staff Responsible for Activity 1")
    with st.expander("ⓘ What is this?"):
        st.markdown("Describe the first key activity funded by the grant and assign who is responsible.")

    activity_2 = st.text_input("Primary Activity 2")
    lead_2 = st.text_input("Staff Responsible for Activity 2")

    activity_3 = st.text_input("Primary Activity 3")
    lead_3 = st.text_input("Staff Responsible for Activity 3")

    st.subheader("Compliance & Reporting")

    report_cycle = st.selectbox("Reporting Frequency", ["Monthly", "Quarterly", "Annually"])
    with st.expander("ⓘ What is this?"):
        st.markdown("Specify how often formal reports must be submitted to the funding agency.")

    archive_docs = st.checkbox("Store All Uploads for Audit Trail?", value=True)
    with st.expander("ⓘ What is this?"):
        st.markdown("If checked, all future uploads and logs tied to this grant will be archived for audit purposes.")

    ai_reminder_enabled = st.checkbox("Enable AI Reminder Prompts", value=True)
    with st.expander("ⓘ What is this?"):
        st.markdown("If checked, AIOS will send alerts when reports are due or compliance tasks are missed.")

    st.form_submit_button("Register Grant")

st.divider()
st.markdown("📁 After submission, this grant will be available for activity logging, reporting, and compliance tracking.")
