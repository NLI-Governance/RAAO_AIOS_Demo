import streamlit as st
from datetime import datetime
from pathlib import Path

st.set_page_config(page_title="Grant Activity Log", layout="centered")

# ---- Logo Upload ----
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Picture_icon_BLACK.svg/1024px-Picture_icon_BLACK.svg.png", width=120)
    st.markdown("### Upload Logo (Optional)")
    logo_file = st.file_uploader("Logo", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

# ---- Header ----
st.markdown("## 📝 Grant Activity Log")
st.markdown("Log any action, status change, or event related to an active grant. This activity log helps maintain transparent documentation for audits, updates, and reporting.")

# ---- Input Form ----
with st.form("activity_log_form"):
    grant_name = st.text_input("Grant Name")
    activity_date = st.date_input("Activity Date", value=datetime.today())
    staff_member = st.text_input("Staff Member Logging Activity")
    activity_type = st.selectbox("Activity Type", ["Email", "Phone Call", "Meeting", "Document Submission", "Status Update", "Other"])
    summary = st.text_area("Activity Summary (describe action, result, or content)")
    file_attachment = st.file_uploader("Attach Related Document (optional)", type=["pdf", "docx", "xlsx", "csv", "jpg", "png"])

    submitted = st.form_submit_button("Log Activity")
    if submitted:
        st.success("Activity successfully logged.")
        # Here you'd write logic to save to database or backend system.

# ---- Informational Sidebar Buttons ----
with st.sidebar.expander("ℹ️ What is this page for?"):
    st.write("This form allows staff to record updates about grant activities. These updates can be used for compliance reporting, internal audits, and to track progress over time.")

with st.sidebar.expander("ℹ️ Why upload a document?"):
    st.write("Supporting documents (such as emails, reports, or scanned forms) improve the audit trail and provide verification for the logged activity.")

with st.sidebar.expander("ℹ️ Activity Type Guidance"):
    st.write("- **Email**: Correspondence about deadlines, submissions, etc.\n"
             "- **Phone Call**: Discussion outcomes or commitments\n"
             "- **Meeting**: Notes from in-person or virtual sessions\n"
             "- **Document Submission**: Uploaded items to funders\n"
             "- **Status Update**: Internal notes on grant phase progress")	
