import streamlit as st
import pandas as pd
import os
import sys

st.set_page_config(page_title="Grant Funding Code Manager", layout="wide")
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
    header="Grant writers, finance staff, and executive reviewers",
    purpose="Create, edit, and manage official internal grant funding codes.",
    usage="Use this form to add or revise a code assigned to each grant. These codes are used in reporting, milestones, and funding alignment.",
    routing="Entries are saved to the central grant codes log and linked to the grant tracking system."
)

st.title("🏷️ Grant Funding Code Manager")

# Grant Code Form
with st.form("funding_code_form"):
    grant_name = st.text_input("Grant Name 🛈", help="Enter the formal name of the grant or funding program.")
    funding_source = st.text_input("Funding Source 🛈", help="Enter the federal, state, or private source name.")
    code = st.text_input("Funding Code 🛈", help="Enter the internal tracking code or external grant number.")
    notes = st.text_area("Notes / Restrictions 🛈", help="Include any relevant fiscal restrictions or category details.")
    submitted = st.form_submit_button("Save Entry")

if submitted:
    st.success(f"Funding code `{code}` added for {grant_name}.")

# Example Table
st.subheader("📄 Existing Codes (example)")
example = pd.DataFrame({
    "Grant Name": ["Community Health Outreach", "STEM Education"],
    "Funding Source": ["CDC", "NSF"],
    "Code": ["CH001", "STEM22"],
    "Notes": ["Restricted to health access programs", "Year 2 allocation only"]
})
st.dataframe(example)

# Export Button
csv = example.to_csv(index=False).encode("utf-8")
st.download_button("📥 Export Code Log", data=csv, file_name="funding_codes.csv")

# Bottom layout
display_abl_footer()
display_gui_version("grant_funding_code_manager_gui.py", version="v3.1")
