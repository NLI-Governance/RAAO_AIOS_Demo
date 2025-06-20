import streamlit as st
import pandas as pd
from datetime import timedelta
from components.shared_ui_components import (
    display_logo,
    display_language_toggle,
    display_about_section,
    display_assistant_banner,
    display_gui_identifier,
    display_abl_footer
)

# Load employee records
def load_employees():
    try:
        df = pd.read_csv("data/hr/employee_records.csv")
        return df
    except Exception as e:
        st.error(f"Error loading employee records: {e}")
        return pd.DataFrame(columns=["Employee Name", "Employee ID"])

# Load training catalog
def load_training_manifest():
    try:
        df = pd.read_csv("data/training/training_manifest.csv")
        return df
    except Exception as e:
        st.error(f"Error loading training catalog: {e}")
        return pd.DataFrame(columns=["Training Title", "Valid for (days)"])

st.set_page_config(page_title="Training Tracker", layout="wide")

display_logo()
display_language_toggle()
display_about_section("Tracks employee training completions and calculates certification expiration dates.")
display_assistant_banner()
display_gui_identifier("training_tracker_gui.py")

st.title("Training Tracker")

employees = load_employees()
trainings = load_training_manifest()

with st.form("training_form"):
    name_options = employees["Employee Name"].dropna().unique().tolist()
    training_options = trainings["Training Title"].dropna().unique().tolist()

    employee_name = st.selectbox("Employee Name", name_options, help="Select the employee who completed training.")
    employee_id = employees.loc[employees["Employee Name"] == employee_name, "Employee ID"].values[0] if employee_name else ""
    st.text_input("Employee ID", value=employee_id, disabled=True)

    training_title = st.selectbox("Training Title", training_options, help="Choose the completed training session.")
    completion_date = st.date_input("Completion Date", help="Date the employee completed this training.")

    # Calculate expiration based on training validity
    valid_days = trainings.loc[trainings["Training Title"] == training_title, "Valid for (days)"].values
    expiration_date = completion_date + timedelta(days=int(valid_days[0])) if valid_days.size > 0 else ""

    st.text_input("Certification Expiration", value=expiration_date, disabled=True)

    notes = st.text_area("Additional Notes", help="Any remarks or context about this training instance.")
    submit = st.form_submit_button("Submit")

    if submit:
        st.success("Training record submitted successfully.")

display_abl_footer()