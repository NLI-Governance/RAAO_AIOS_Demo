import streamlit as st
import pandas as pd
from pathlib import Path

# Logo and title
st.image("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png", width=120)
st.markdown("## ⚠️ Employee Disciplinary Log")
st.caption("Log disciplinary actions, assign severity, and track follow-up by HR.")

# CSV path
csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_disciplinary_log.csv").expanduser()
if not csv_path.exists():
    st.error("Disciplinary log CSV not found.")
    st.stop()

# Load existing data
df = pd.read_csv(csv_path)

# New entry form
with st.expander("➕ Add New Disciplinary Entry", expanded=False):
    with st.form("disciplinary_log_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Employee Name", help="Full name of the employee being logged.")
            emp_id = st.text_input("Employee ID", help="Internal HR identifier for the employee.")
            action_date = st.date_input("Date of Incident", help="The date when the disciplinary incident occurred.")
        with col2:
            severity = st.selectbox("Severity Level", ["Low", "Moderate", "High", "Critical"], help="Indicates seriousness of the issue.")
            action_taken = st.text_input("Action Taken", help="Describe what disciplinary action was issued.")
            follow_up = st.text_area("Follow-Up Plan", help="Describe what monitoring or follow-up is planned.")

        submitted_by = st.text_input("Recorded By", help="Name of the HR staff entering this record.")

        submitted = st.form_submit_button("Submit Entry")
        if submitted:
            new_row = pd.DataFrame([{
                "Employee Name": name,
                "Employee ID": emp_id,
                "Date": action_date,
                "Severity": severity,
                "Action Taken": action_taken,
                "Follow-Up": follow_up,
                "Recorded By": submitted_by
            }])
            updated_df = pd.concat([df, new_row], ignore_index=True)
            updated_df.to_csv(csv_path, index=False)
            st.success("✅ Entry submitted successfully.")

# Display existing entries
st.markdown("### 📋 Logged Disciplinary Actions")
st.dataframe(df, use_container_width=True)
