import streamlit as st
import pandas as pd
import os
import sys

st.set_page_config(page_title="Grant Milestone Tracker", layout="wide")
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
    header="Grant coordinators, reporting staff, and executive team",
    purpose="Track progress and completion of grant-funded deliverables and deadlines.",
    usage="Log each milestone as it's planned and then update the completion date when achieved.",
    routing="Records are stored in grant_milestones_log.csv and reviewed during funder reporting."
)

st.title("📅 Grant Milestone Tracker")

# Milestone input form
with st.form("milestone_form"):
    grant_name = st.text_input("Grant Name 🛈", help="Specify the grant this milestone relates to.")
    milestone = st.text_input("Milestone Description 🛈", help="Briefly describe the expected deliverable.")
    due_date = st.date_input("Due Date 🛈", help="Enter the date by which this milestone is due.")
    completion_date = st.date_input("Date Completed 🛈", help="Fill only after the milestone is complete.")
    submitted = st.form_submit_button("Add Milestone")

if submitted:
    st.success(f"Milestone for '{grant_name}' added.")

# Example milestone log
st.subheader("🗂️ Milestone Log (example)")
example = pd.DataFrame({
    "Grant": ["Community Outreach", "STEM Lab Expansion"],
    "Milestone": ["Host first clinic", "Order equipment"],
    "Due Date": ["2024-06-01", "2024-08-15"],
    "Completed": ["2024-06-05", ""]
})
st.dataframe(example)

csv = example.to_csv(index=False).encode("utf-8")
st.download_button("📥 Export Milestone Log", data=csv, file_name="grant_milestones_log.csv")

# Footer
display_abl_footer()
display_gui_version("grant_milestone_tracker_gui.py", version="v3.1")
