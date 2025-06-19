import streamlit as st
import pandas as pd
import os
import sys

st.set_page_config(page_title="Employee Leave Request", layout="wide")
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
    header="All employees and HR leave coordinators",
    purpose="Submit formal requests for time off, including sick days, vacation, and family leave.",
    usage="Complete all fields accurately. Use hover help to select the appropriate leave category and date range.",
    routing="Requests are saved to employee_leave_log.csv and routed to department heads and HR for review."
)

st.title("🌴 Employee Leave Request Form")

# Leave request form
with st.form("leave_form"):
    employee_name = st.text_input("Employee Name 🛈", help="Your full name as registered in HR.")
    department = st.text_input("Department 🛈", help="The department you work in.")
    leave_type = st.selectbox("Leave Type 🛈", ["Vacation", "Sick Leave", "Family Leave", "Unpaid Leave", "Other"], help="Select the correct leave type.")
    start_date = st.date_input("Leave Start Date 🛈", help="First day of requested leave.")
    end_date = st.date_input("Leave End Date 🛈", help="Last day of requested leave.")
    reason = st.text_area("Leave Reason 🛈", help="Provide a brief explanation of the reason for your leave.")
    submitted = st.form_submit_button("Submit Leave Request")

if submitted:
    st.success(f"Leave request for {employee_name} submitted.")

# Example log
st.subheader("🗂️ Leave Requests Log (example)")
example = pd.DataFrame({
    "Employee": ["S. Taylor", "L. Jimenez"],
    "Type": ["Sick Leave", "Vacation"],
    "Dates": ["2024-06-01 to 2024-06-03", "2024-07-15 to 2024-07-20"]
})
st.dataframe(example)

csv = example.to_csv(index=False).encode("utf-8")
st.download_button("📥 Export Leave Requests", data=csv, file_name="employee_leave_log.csv")

# Footer
display_abl_footer()
display_gui_version("employee_leave_request_gui.py", version="v3.1")
