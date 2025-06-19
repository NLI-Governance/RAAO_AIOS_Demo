# grant_onboarding_gui_v2_FINAL_LOCKED.py
# Standards: AI-enabled grant intake, role-based validation, nonprofit-agnostic interface
import streamlit as st
from datetime import date

st.set_page_config(page_title="Grant Onboarding", layout="centered")

# --- HEADER ---
with st.container():
    st.markdown("## 🎯 Grant Onboarding – AIOS")
    st.caption("Use this form to enter a new grant opportunity into the system.")
    st.markdown("---")

# --- FORM ---
with st.form("grant_form"):
    col1, col2 = st.columns(2)

    with col1:
        grant_name = st.text_input("Grant Name")
        grant_source = st.text_input("Funding Agency or Source")
        contact_name = st.text_input("Agency Contact Name")
        contact_email = st.text_input("Agency Contact Email")
        submission_deadline = st.date_input("Submission Deadline", min_value=date.today())

    with col2:
        grant_amount = st.text_input("Estimated Grant Amount ($)")
        funding_type = st.selectbox("Funding Type", ["Federal", "State", "Private Foundation", "Other"])
        recurring = st.selectbox("Is this a recurring grant?", ["No", "Yes – Annual", "Yes – Multi-Year"])
        internal_owner = st.text_input("Primary Internal Owner (Name or Department)")
        fiscal_year = st.selectbox("Fiscal Year", ["2025", "2026", "2027"])

    st.markdown("#### Grant Description")
    description = st.text_area("Summary of purpose, deliverables, or targeted populations.")

    st.markdown("#### Grant Requirements")
    deliverables = st.text_area("Enter reporting obligations, metrics, or restrictions if known.")

    logo_uploaded = st.file_uploader("Upload Logo (Optional)", type=["png", "jpg", "jpeg"])

    submitted = st.form_submit_button("Submit Grant")

# --- CONFIRMATION ---
if submitted:
    st.success("✅ Grant record has been submitted.")
    st.write("**Grant Name:**", grant_name)
    st.write("**Funding Source:**", grant_source)
    st.write("**Deadline:**", submission_deadline)
    st.write("**Description:**", description)
    st.write("**Deliverables:**", deliverables)
