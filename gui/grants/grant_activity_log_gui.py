import streamlit as st
import pandas as pd
import os
import sys

st.set_page_config(page_title="Grant Activity Log", layout="wide")
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
    header="Program staff, evaluators, and grant managers",
    purpose="Log detailed activities supported by grant funding, including outreach, staffing, or events.",
    usage="Use this form to record activities by grant, date, and type. These logs support reporting and reimbursement.",
    routing="Entries are saved to grant_activity_log.csv and reviewed by both program leads and compliance staff."
)

st.title("📝 Grant Activity Log")

# Activity input form
with st.form("activity_form"):
    grant_name = st.text_input("Grant Name 🛈", help="Enter the name of the grant funding this activity.")
    activity_date = st.date_input("Activity Date 🛈", help="Date the activity took place.")
    activity_type = st.selectbox("Activity Type 🛈", ["Outreach", "Training", "Staffing", "Evaluation", "Other"], help="Select the type of activity performed.")
    description = st.text_area("Activity Description 🛈", help="Summarize what occurred, who was involved, and any outcomes.")
    submitted = st.form_submit_button("Log Activity")

if submitted:
    st.success(f"Activity for grant '{grant_name}' logged.")

# Example activity table
st.subheader("🗂️ Activity Log (example)")
example = pd.DataFrame({
    "Grant": ["Youth Services", "Food Distribution"],
    "Date": ["2024-04-10", "2024-04-14"],
    "Type": ["Outreach", "Staffing"]
})
st.dataframe(example)

csv = example.to_csv(index=False).encode("utf-8")
st.download_button("📥 Export Activity Log", data=csv, file_name="grant_activity_log.csv")

# Footer
display_abl_footer()
display_gui_version("grant_activity_log_gui.py", version="v3.1")
