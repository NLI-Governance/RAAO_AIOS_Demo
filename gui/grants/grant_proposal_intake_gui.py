import streamlit as st
import pandas as pd
import os
import sys

st.set_page_config(page_title="Grant Proposal Intake", layout="wide")
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
    header="Program directors and grant writers",
    purpose="Submit a new grant proposal to begin approval, routing, and tracking.",
    usage="Complete this form for any new funding opportunity you'd like the organization to pursue.",
    routing="Entries are saved to grant_proposal_intake_log.csv and reviewed by executive leadership."
)

st.title("📄 Grant Proposal Intake")

# Intake form
with st.form("proposal_form"):
    proposal_name = st.text_input("Proposal Title 🛈", help="What is the official or working title of the proposal?")
    funder = st.text_input("Funder / Opportunity 🛈", help="Name of the foundation, government program, or RFP source.")
    deadline = st.date_input("Submission Deadline 🛈", help="What is the date this proposal must be submitted by?")
    priority = st.selectbox("Strategic Priority 🛈", ["High", "Medium", "Low"], help="Estimate how aligned this is with organizational goals.")
    notes = st.text_area("Initial Notes 🛈", help="Include eligibility notes, internal lead ideas, or requirements.")
    submitted = st.form_submit_button("Submit Proposal Intake")

if submitted:
    st.success(f"Proposal intake for '{proposal_name}' submitted.")

# Example table
st.subheader("🗂️ Proposal Intake Log (example)")
example = pd.DataFrame({
    "Proposal": ["Digital Literacy", "Food Resilience"],
    "Funder": ["Local Gov Tech Initiative", "USDA"],
    "Deadline": ["2024-07-01", "2024-08-01"]
})
st.dataframe(example)

csv = example.to_csv(index=False).encode("utf-8")
st.download_button("📥 Export Proposal Log", data=csv, file_name="grant_proposal_intake_log.csv")

# Footer
display_abl_footer()
display_gui_version("grant_proposal_intake_gui.py", version="v3.1")
