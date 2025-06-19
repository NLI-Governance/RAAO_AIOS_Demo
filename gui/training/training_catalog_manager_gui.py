import streamlit as st
import pandas as pd
import os
import sys

st.set_page_config(page_title="Training Catalog Manager", layout="wide")
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
    header="Training managers and HR administrators",
    purpose="Manage the master training catalog used across all employee and compliance systems.",
    usage="Add, edit, or update official training modules. Each item must have a unique title and expiration duration.",
    routing="Saved data updates training_catalog.csv and informs expiration calculations in all GUIs."
)

st.title("📘 Training Catalog Manager")

catalog_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/training_catalog.csv")

# Load catalog
if os.path.exists(catalog_path):
    catalog_df = pd.read_csv(catalog_path)
else:
    catalog_df = pd.DataFrame(columns=["Training Title", "Expiration Days"])

st.dataframe(catalog_df)

with st.form("add_training_form"):
    title = st.text_input("Training Title 🛈", help="Enter the name of the training module (e.g., CPR, Harassment Policy).")
    days = st.number_input("Expiration Days 🛈", help="Number of days before this training certification expires.", min_value=0)
    submit = st.form_submit_button("Add to Catalog")

if submit:
    new_entry = pd.DataFrame([{"Training Title": title, "Expiration Days": days}])
    catalog_df = pd.concat([catalog_df, new_entry], ignore_index=True)
    catalog_df.to_csv(catalog_path, index=False)
    st.success(f"{title} added to catalog.")

# Download latest catalog
csv = catalog_df.to_csv(index=False).encode("utf-8")
st.download_button("📥 Export Catalog", data=csv, file_name="training_catalog.csv")

# Footer
display_abl_footer()
display_gui_version("training_catalog_manager_gui.py", version="v3.1")
