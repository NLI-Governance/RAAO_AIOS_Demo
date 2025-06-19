import streamlit as st
import pandas as pd
from pathlib import Path

# Logo and Title
st.image(str(Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png").expanduser()), width=120)
st.markdown("### 🧭 Volunteer Role Manager")
st.caption("Manage volunteer role categories and update responsibilities.")

st.markdown("### ➕ Add New Volunteer Role")

# Input fields with tooltips
role_name = st.text_input("Role Name", help="Enter the name of the volunteer role (e.g., 'Food Distribution').")
role_description = st.text_area("Role Description", help="Briefly describe the responsibilities for this role.")
is_active = st.checkbox("Role is currently active", help="Uncheck if this role is no longer in use.")

# File path
csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/volunteer_roles.csv").expanduser()

# Create file if it doesn't exist
if not csv_path.exists():
    df = pd.DataFrame(columns=["Role Name", "Description", "Is Active"])
    df.to_csv(csv_path, index=False)

# Add role
if st.button("Add Role"):
    new_data = pd.DataFrame([{
        "Role Name": role_name,
        "Description": role_description,
        "Is Active": is_active
    }])
    existing_data = pd.read_csv(csv_path)
    updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    updated_data.to_csv(csv_path, index=False)
    st.success(f"Role '{role_name}' added.")

# Display existing roles
st.markdown("### 📋 Existing Roles")
try:
    existing_data = pd.read_csv(csv_path)
    st.dataframe(existing_data)
except Exception as e:
    st.error(f"Error loading CSV: {e}")
