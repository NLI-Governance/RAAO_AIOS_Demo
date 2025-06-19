import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import date

# Logo and Title
st.image(str(Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png").expanduser()), width=100)
st.title("📚 Employee Training Tracker")

# Initialize CSV path
csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_training_log.csv").expanduser()

# Form
with st.form("training_form"):
    col1, col2 = st.columns(2)

    with col1:
        emp_name = st.text_input("Employee Name", help="Enter the full name of the employee.")
        emp_id = st.text_input("Employee ID", help="Use the official internal employee identifier.")
        department = st.text_input("Department", help="Which department does the employee work in?")
        trainer = st.text_input("Trainer Name", help="Name of the trainer or system that delivered the training.")
    with col2:
        training_type = st.selectbox("Training Type", ["Onboarding", "Safety", "HIPAA", "Role-Specific", "Other"],
                                     help="Choose the category of training completed.")
        training_name = st.text_input("Training Name", help="Name of the training module or course.")
        date_completed = st.date_input("Date Completed", value=date.today(), help="Select the completion date.")
        expiration = st.date_input("Expiration Date (if any)", help="Optional. Leave blank if not applicable.")

    notes = st.text_area("Notes", help="Add any observations, exceptions, or performance comments.")

    submitted = st.form_submit_button("Submit Training Record")

# Save to CSV
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
    st.success("✅ Training record saved successfully!")
