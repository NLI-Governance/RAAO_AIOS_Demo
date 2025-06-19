# employee_status_change_gui.py
# Purpose: Submit and log employee role/status changes (promotions, department moves, etc.)
# Standards: EEOC, ISO 9001 (HR), ABL Rev2, internal audit policy

import streamlit as st
from pathlib import Path
import pandas as pd
from datetime import date

# Load logo (expands ~ properly)
logo_path = str(Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png").expanduser())
st.image(logo_path, width=100)

st.title("Employee Status Change")

CSV_PATH = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_status_change_log.csv").expanduser()
CSV_PATH.parent.mkdir(parents=True, exist_ok=True)

with st.form("status_change_form"):
    col1, col2 = st.columns([2, 1])
    with col1:
        name = st.text_input("Employee Name", help="Enter the full name of the employee.")
        emp_id = st.text_input("Employee ID", help="Enter the unique employee ID or payroll code.")
    with col2:
        change_type = st.selectbox("Change Type", ["Promotion", "Transfer", "Leave", "Termination", "Return from Leave", "Other"], help="Select the type of employment change being made.")
        eff_date = st.date_input("Effective Date", date.today(), help="The date this change becomes official.")

    reason = st.text_area("Reason for Change", help="Enter a brief explanation for the change. This will be used for internal auditing.")
    followup = st.text_area("Follow-Up Instructions (Optional)", help="Include any instructions for payroll, HR, or IT.")
    approved_by = st.text_input("Approved By", help="Enter the full name of the supervisor or manager authorizing the change.")

    submitted = st.form_submit_button("Submit Change")

if submitted:
    new_entry = {
        "Employee Name": name,
        "Employee ID": emp_id,
        "Change Type": change_type,
        "Effective Date": eff_date.strftime("%Y-%m-%d"),
        "Reason": reason,
        "Follow-Up": followup,
        "Approved By": approved_by
    }

    try:
        if CSV_PATH.exists():
            existing = pd.read_csv(CSV_PATH)
            updated = pd.concat([existing, pd.DataFrame([new_entry])], ignore_index=True)
        else:
            updated = pd.DataFrame([new_entry])

        updated.to_csv(CSV_PATH, index=False)
        st.success("✅ Status change recorded.")
    except Exception as e:
        st.error(f"❌ Failed to save data: {e}")
