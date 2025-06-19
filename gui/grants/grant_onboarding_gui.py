import streamlit as st
import pandas as pd
import os
import sys

st.set_page_config(page_title="Grant Onboarding Form", layout="wide")
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
    header="Program directors and grants onboarding team",
    purpose="Enter essential details to onboard a newly awarded grant into the tracking system.",
    usage="Complete this form once a grant has been awarded. This step connects it to tracking, reporting, and compliance tools.",
    routing="Submissions go into grant_onboarding_log.csv and are visible to finance and executive leadership."
)

st.title("🚀 Grant Onboarding Form")

# Onboarding form
with st.form("onboarding_form"):
    grant_name = st.text_input("Grant Name 🛈", help="Enter the full official name of the awarded grant.")
    award_amount = st.number_input("Award Amount 🛈", min_value=0.0, help="Total dollar value of the grant.")
    start_date = st.date_input("Start Date 🛈", help="When does the grant begin?")
    end_date = st.date_input("End Date 🛈", help="When does the grant period end?")
    notes = st.text_area("Internal Notes 🛈", help="Add setup steps, budget items, or strategic alignments.")
    submitted = st.form_submit_button("Onboard Grant")

if submitted:
    st.success(f"Grant '{grant_name}' successfully onboarded.")

# Example log
st.subheader("🗂️ Onboarded Grants Log (example)")
example = pd.DataFrame({
    "Grant": ["Green Workforce", "Early Reading"],
    "Amount": ["$125,000", "$90,000"],
    "Start": ["2024-04-01", "2024-05-15"],
    "End": ["2025-03-31", "2025-05-14"]
})
st.dataframe(example)

csv = example.to_csv(index=False).encode("utf-8")
st.download_button("📥 Export Onboarding Log", data=csv, file_name="grant_onboarding_log.csv")

# Footer
display_abl_footer()
display_gui_version("grant_onboarding_gui.py", version="v3.1")
