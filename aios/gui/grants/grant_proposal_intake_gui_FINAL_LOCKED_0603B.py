# grant_proposal_intake_gui_FINAL_LOCKED_v2_0603.py
# Purpose: Intake GUI for grant opportunities prior to application submission
# Standards: 2 CFR Part 200, ABL_Rev2_6_1_25, nonprofit audit transparency

import streamlit as st
from datetime import date
from PIL import Image
import os

st.set_page_config(page_title="Grant Proposal Intake", layout="centered")

# --- Logo at Top ---
logo_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
if os.path.exists(logo_path):
    st.image(Image.open(logo_path), width=150)

st.title("📝 Grant Proposal Intake")
st.caption("Use this form to register potential grant applications before submission.")

with st.form("grant_intake"):

    st.subheader("Opportunity Details")

    grant_name = st.text_input("Grant Title")
    with st.expander("ⓘ What is this?"):
        st.markdown("Enter the full official title of the grant program.")

    grantor = st.text_input("Funding Organization or Agency")
    with st.expander("ⓘ What is this?"):
        st.markdown("Name of the entity providing the funding—such as a federal agency, state department, or private foundation.")

    grant_id = st.text_input("Grant ID / Reference Code (if any)")
    with st.expander("ⓘ What is this?"):
        st.markdown("If the funder issued a tracking number or reference code for this opportunity, enter it here.")

    funding_type = st.selectbox("Funding Type", ["Federal", "State", "Private", "Foundation", "Other"])
    with st.expander("ⓘ What is this?"):
        st.markdown("Select the broad category of the funder for recordkeeping and classification.")

    recurring = st.selectbox("Is this recurring?", ["No", "Yes – Annual", "Yes – Multi-Year"])
    with st.expander("ⓘ What is this?"):
        st.markdown("Indicate whether this grant is a one-time opportunity or renews periodically.")

    fiscal_year = st.selectbox("Target Fiscal Year", ["2025", "2026", "2027"])
    with st.expander("ⓘ What is this?"):
        st.markdown("Choose the fiscal year when you expect funds to be received or used.")

    st.subheader("Submission Planning")

    internal_owner = st.text_input("Internal Owner or Lead")
    with st.expander("ⓘ What is this?"):
        st.markdown("Enter the name or role of the staff member responsible for submitting the application.")

    submission_deadline = st.date_input("Submission Deadline", value=date.today())
    with st.expander("ⓘ What is this?"):
        st.markdown("Select the last day the grant application must be submitted to the funder.")

    estimated_award = st.text_input("Estimated Grant Value ($)")
    with st.expander("ⓘ What is this?"):
        st.markdown("If known, provide an approximate value of the potential award. This helps with budget planning.")

    purpose = st.text_area("Brief Description of Grant Purpose")
    with st.expander("ⓘ What is this?"):
        st.markdown("Summarize what the grant will support: programs, services, targeted communities, etc.")

    st.subheader("Grant Files")

    upload_files = st.file_uploader("Upload Application Docs (RFPs, LOIs, Drafts)", accept_multiple_files=True)
    with st.expander("ⓘ What is this?"):
        st.markdown("Upload any official documents from the funder: Requests for Proposals (RFPs), Letters of Intent (LOIs), application drafts, or guidelines.")

    submitted = st.form_submit_button("Submit Intake Record")

if submitted:
    st.success("✅ Grant intake has been recorded.")
    st.write("**Grant:**", grant_name)
    st.write("**Funder:**", grantor)
    st.write("**Deadline:**", submission_deadline)
    st.write("**Purpose:**", purpose)
    if upload_files:
        st.info(f"{len(upload_files)} file(s) uploaded for archive and review.")
