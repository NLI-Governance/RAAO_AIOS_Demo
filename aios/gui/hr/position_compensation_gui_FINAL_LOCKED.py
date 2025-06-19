# Position & Compensation GUI
# Purpose: Record employee roles, pay rates, and wage types (hourly/salaried)
# Standards: Role-based access, integrated with payroll and HR systems

import streamlit as st
import pandas as pd
import os

CSV_PATH = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/position_compensation.csv")
LOGO_PATH = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")

st.set_page_config(page_title="Position & Compensation", layout="centered")
if os.path.exists(LOGO_PATH):
    st.image(LOGO_PATH, width=120)

st.title("💼 Position & Compensation Setup")
st.caption("Assign pay rates and roles to employees for payroll use.")

with st.form("position_form"):
    employee_name = st.text_input("Employee Name")
    employee_id = st.text_input("Employee ID")
    job_title = st.text_input("Job Title")
    department = st.text_input("Department")
    wage_type = st.radio("Wage Type", ["Hourly", "Salary"])
    pay_rate = st.number_input("Pay Rate ($)", min_value=0.0, step=0.01)
    effective_date = st.date_input("Effective Date")
    notes = st.text_area("Notes (e.g. raise reason or classification)", height=100)

    st.markdown(
        "<div style='font-size: small; margin-top: 10px;'>"
        "❓ <b>Pay Rate:</b> Enter hourly rate or annual salary depending on the wage type."
        "</div>",
        unsafe_allow_html=True
    )

    submit = st.form_submit_button("Save Record")

    if submit:
        if employee_name and employee_id and pay_rate > 0:
            entry = pd.DataFrame([[
                employee_name, employee_id, job_title, department, wage_type,
                pay_rate, str(effective_date), notes
            ]], columns=[
                "Employee Name", "Employee ID", "Job Title", "Department",
                "Wage Type", "Pay Rate", "Effective Date", "Notes"
            ])
            if os.path.exists(CSV_PATH):
                existing = pd.read_csv(CSV_PATH)
                entry = pd.concat([existing, entry], ignore_index=True)
            entry.to_csv(CSV_PATH, index=False)
            st.success("✅ Position and compensation recorded.")
        else:
            st.error("Please complete all required fields and enter a valid pay rate.")
