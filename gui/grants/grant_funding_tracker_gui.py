import streamlit as st
import pandas as pd
import os
import sys

st.set_page_config(page_title="Grant Funding Tracker", layout="wide")
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
    header="Grant finance team and program directors",
    purpose="Track received, expected, and pending grant funding by source and date.",
    usage="Enter each new funding line as it is awarded or committed.",
    routing="Data is stored in the central grant_funding_log.csv file and reviewed by finance leadership."
)

st.title("💰 Grant Funding Tracker")

# Funding input form
with st.form("funding_tracker_form"):
    grant_name = st.text_input("Grant Name 🛈", help="Enter the full name of the grant as awarded.")
    amount = st.number_input("Funding Amount 🛈", min_value=0.0, help="Enter the funding amount received or pledged.")
    date = st.date_input("Funding Date 🛈", help="Enter the date the funds were received or committed.")
    funding_status = st.selectbox("Funding Status 🛈", ["Received", "Committed", "Pending"])
    submitted = st.form_submit_button("Add Funding Entry")

if submitted:
    st.success(f"Funding entry for '{grant_name}' added successfully.")

# Example log display
st.subheader("🗂️ Grant Funding Log (example)")
example = pd.DataFrame({
    "Grant": ["Housing Stability", "Rural Broadband"],
    "Amount": ["$250,000", "$180,000"],
    "Date": ["2024-03-01", "2024-06-15"],
    "Status": ["Received", "Pending"]
})
st.dataframe(example)

csv = example.to_csv(index=False).encode("utf-8")
st.download_button("📥 Export Funding Log", data=csv, file_name="grant_funding_log.csv")

# Footer
display_abl_footer()
display_gui_version("grant_funding_tracker_gui.py", version="v3.1")
