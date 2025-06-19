# Employee Leave Tracker GUI
# Purpose: Track leave balances, time off requests, and approvals
# Standards: Includes federal leave categories, tooltips, and branding consistency

import streamlit as st
import pandas as pd
import os
from datetime import date

CSV_PATH = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_leave_log.csv")
LOGO_PATH = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")

st.set_page_config(page_title="Employee Leave Tracker", layout="centered")
if os.path.exists(LOGO_PATH):
    st.image(LOGO_PATH, width=120)

st.title("🏖️ Employee Leave Tracker")
st.caption("Log time off requests and view balances.")

with st.form("leave_form"):
    name = st.text_input("Employee Name", help="Full name of the employee requesting leave.")
    emp_id = st.text_input("Employee ID", help="Enter the internal ID number of the employee.")
    leave_type = st.selectbox(
        "Leave Type ❓", 
        [
            "Vacation", "Sick", "Personal", "Bereavement",
            "Parental (Maternity/Paternity)", "FMLA – Medical Leave",
            "Military Leave", "Jury Duty", "Voting Leave", "Other"
        ],
        help="Choose the category of leave. Some types are legally protected."
    )
    start_date = st.date_input("Start Date ❓", help="The first day the employee will be absent.")
    end_date = st.date_input("End Date ❓", help="The last day of the absence.")
    total_days = st.number_input("Total Days Requested ❓", min_value=0.5, step=0.5, help="Partial days allowed (e.g. 0.5 for half-day).")
    reason = st.text_area("Reason (optional)", help="Optional. Enter details if required for this leave type.")
    approval_status = st.selectbox(
        "Approval Status ❓",
        ["Pending", "Approved", "Denied"],
        help="HR/Management selects status based on policy."
    )

    submit = st.form_submit_button("Submit Request")

    if submit:
        if name and emp_id and total_days > 0:
            record = pd.DataFrame([[name, emp_id, leave_type, str(start_date), str(end_date), total_days, reason, approval_status]],
                                  columns=[
                                      "Employee Name", "Employee ID", "Leave Type", "Start Date",
                                      "End Date", "Days Requested", "Reason", "Approval Status"
                                  ])
            if os.path.exists(CSV_PATH):
                existing = pd.read_csv(CSV_PATH)
                updated = pd.concat([existing, record], ignore_index=True)
            else:
                updated = record

            updated.to_csv(CSV_PATH, index=False)
            st.success("✅ Leave request submitted.")
        else:
            st.error("Please complete all required fields and enter a valid number of days.")
