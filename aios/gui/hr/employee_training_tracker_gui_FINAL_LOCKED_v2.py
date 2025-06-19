import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import date

# Paths
logo_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png").expanduser()
csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_training_log.csv").expanduser()
catalog_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/training_catalog.csv").expanduser()

# UI
st.image(str(logo_path), width=100)
st.title("📚 Employee Training Tracker")

# Load training names from catalog
if catalog_path.exists():
    catalog_df = pd.read_csv(catalog_path)
    training_names = catalog_df["Training Name"].dropna().unique().tolist()
else:
    training_names = []

# Form
with st.form("training_form"):
    col1, col2 = st.columns(2)

    with col1:
        emp_name = st.text_input("Employee Name", help="Full name of the employee.")
        emp_id = st.text_input("Employee ID", help="Internal ID assigned to the employee.")
        department = st.text_input("Department", help="Department or team assignment.")
        trainer = st.text_input("Trainer Name", help="Who delivered or oversaw the training.")
    with col2:
        training_type = st.selectbox("Training Type", ["Onboarding", "Safety", "HIPAA", "Role-Specific", "Other"],
                                     help="Choose the broad category.")
        training_name = st.selectbox("Training Name", training_names, help="Select from approved training catalog.")
        date_completed = st.date_input("Date Completed", value=date.today(), help="Date this training was completed.")
        expiration = st.date_input("Expiration Date (if any)", help="Leave blank if not applicable.")

    notes = st.text_area("Notes", help="Extra details or special notes about this training session.")

    submitted = st.form_submit_button("Submit Training Record")

# Save Record
if submitted:
    data = {
        "Employee Name": emp_name,
        "Employee ID": emp_id,
        "Department": department,
        "Training Type": training_type,
        "Training Name": training_name,
        "Trainer": trainer,
        "Date Completed": date_completed.strftime("%Y-%m-%d"),
        "Expiration Date": expiration.strftime("%Y-%m-%d") if expiration else "",
        "Notes": notes
    }

    df_new = pd.DataFrame([data])
    if csv_path.exists():
        df_existing = pd.read_csv(csv_path)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new

    df_combined.to_csv(csv_path, index=False)
    st.success("✅ Training record saved.")
