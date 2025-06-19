import streamlit as st
import pandas as pd
import os
import sys

st.set_page_config(page_title="Training Tracker", layout="wide")
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
    header="HR staff and program trainers",
    purpose="Log completed employee trainings and track certification or safety compliance.",
    usage="Select an employee, choose the training type, and record certification details. Use info buttons for help.",
    routing="Entries are saved to employee_training_log.csv and reviewed monthly by HR and department heads."
)

st.title("🎓 Employee Training Tracker")

# Load employee records
employee_df = pd.read_csv(os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_records.csv"))
employee_names = employee_df["Full Name"].tolist()

# Load training catalog
catalog_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/training_catalog.csv")
catalog_df = pd.read_csv(catalog_path)
training_titles = catalog_df["Training Title"].tolist()
expiration_lookup = dict(zip(catalog_df["Training Title"], catalog_df["Expiration Days"]))

# Training entry form
with st.form("training_form"):
    name = st.selectbox("Employee Name 🛈", employee_names, help="Select the employee who completed the training.")
    employee_id = employee_df.loc[employee_df["Full Name"] == name, "Employee ID"].values[0]
    training = st.selectbox("Training Title 🛈", training_titles, help="Choose the training completed.")
    completion = st.date_input("Date Completed 🛈", help="When was the training completed?")
    expiration = completion + pd.Timedelta(days=int(expiration_lookup.get(training, 0)))
    st.write(f"🗓️ Certification expires on: **{expiration.date()}**")
    notes = st.text_area("Notes 🛈", help="Optional comments, such as trainer, format, or location.")
    submit = st.form_submit_button("Log Training")

if submit:
    st.success(f"{training} logged for {name} (ID: {employee_id})")

# Display sample training log
st.subheader("🗂️ Sample Training Log")
example = pd.DataFrame({
    "Employee": ["A. Johnson", "B. Singh"],
    "Training": ["CPR", "OSHA Safety"],
    "Completed": ["2024-05-01", "2024-06-15"]
})
st.dataframe(example)

csv = example.to_csv(index=False).encode("utf-8")
st.download_button("📥 Export Training Log", data=csv, file_name="employee_training_log.csv")

# Footer
display_abl_footer()
display_gui_version("training_tracker_gui.py", version="v3.1")
