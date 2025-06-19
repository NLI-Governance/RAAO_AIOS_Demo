import streamlit as st
import pandas as pd
import os
import sys

st.set_page_config(page_title="Grant Writer Workspace", layout="wide")
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
    header="Grant writing staff, directors, and reviewers",
    purpose="Provide a collaborative space for planning, drafting, and managing grant proposals.",
    usage="Add proposal concepts, assign writing roles, and track status.",
    routing="Data is saved to the grant_writer_workspace_log.csv file and reviewed by your program manager."
)

st.title("🧠 Grant Writer Workspace")

# Proposal input form
with st.form("writer_workspace_form"):
    proposal_title = st.text_input("Proposal Title 🛈", help="Enter the working title or theme of your grant concept.")
    lead_writer = st.text_input("Lead Writer 🛈", help="Who is responsible for coordinating this proposal?")
    status = st.selectbox("Proposal Status 🛈", ["Draft", "In Progress", "Submitted", "Awarded", "Not Awarded"])
    notes = st.text_area("Notes 🛈", help="Track deadlines, challenges, or routing details here.")
    submitted = st.form_submit_button("Add to Workspace")

if submitted:
    st.success(f"Proposal '{proposal_title}' added to the workspace.")

# Example workspace log
st.subheader("🗂️ Current Workspace Log (example)")
example = pd.DataFrame({
    "Title": ["Food Security", "Tech Education"],
    "Writer": ["A. Smith", "B. Jones"],
    "Status": ["In Progress", "Draft"]
})
st.dataframe(example)

csv = example.to_csv(index=False).encode("utf-8")
st.download_button("📥 Export Workspace Log", data=csv, file_name="grant_writer_workspace_log.csv")

# Footer
display_abl_footer()
display_gui_version("grant_writer_workspace_gui.py", version="v3.1")
