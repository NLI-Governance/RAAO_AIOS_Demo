# grant_funding_code_manager_gui.py
# Now with info icons for new input fields, dropdowns for critical categories

import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Grant Funding Code Manager", layout="centered")
st.image("logo.png", width=120)
st.title("Grant Funding Code Manager")

st.markdown("Use this screen to manage grant codes used in payroll, HR, and compliance systems.")

# CSV path setup
base_path = os.path.dirname(__file__)
csv_path = os.path.abspath(os.path.join(base_path, "..", "data", "grant_codes.csv"))
os.makedirs(os.path.dirname(csv_path), exist_ok=True)

# Load or initialize CSV
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
else:
    df = pd.DataFrame(columns=[
        "Grant Code", "Grant Name", "Funding Source",
        "Linked Department", "Status", "Expiration Date"
    ])

# Controlled dropdowns
departments = [
    "Outreach", "Shelter", "Administration", "Case Management",
    "HR", "Finance", "Facilities", "Development", "Volunteer Services"
]

statuses = ["Active", "Inactive", "Expired", "Pending Approval"]

with st.form("grant_form"):
    col1, col2 = st.columns(2)
    with col1:
        grant_code = st.text_input("Grant Code 🛈", help="Use the internal grant reference (e.g., GR-1001 or system-issued tag).")
        grant_name = st.text_input("Grant Name 🛈", help="Use the full formal title of the grant as it appears in award letters.")
        funding_source = st.text_input("Funding Source 🛈", help="Enter the agency or funder (e.g., HUD, United Way, CDC).")
    with col2:
        linked_department = st.selectbox("Linked Department 🛈", departments, help="Select the department responsible for managing the grant.")
        status = st.selectbox("Status 🛈", statuses, help="Active = in use; Inactive = not currently used; Expired = past term.")
        expiration_date = st.date_input("Expiration Date 🛈", help="When the grant funding expires or must be renewed.")

    submitted = st.form_submit_button("Save Grant Entry")
    if submitted:
        new_entry = {
            "Grant Code": grant_code,
            "Grant Name": grant_name,
            "Funding Source": funding_source,
            "Linked Department": linked_department,
            "Status": status,
            "Expiration Date": expiration_date
        }
        if grant_code in df["Grant Code"].values:
            df.loc[df["Grant Code"] == grant_code] = new_entry
        else:
            df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_csv(csv_path, index=False)
        st.success("Grant information saved.")

st.markdown("### Current Grant Codes")
if df.empty:
    st.info("No entries yet.")
else:
    st.dataframe(df, use_container_width=True)

st.download_button("Download CSV", data=df.to_csv(index=False), file_name="grant_codes.csv", mime="text/csv")

st.markdown("---")
st.markdown("© 2025 Rising Against All Odds | Grant Funding Registry")
