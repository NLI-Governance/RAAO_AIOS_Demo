import streamlit as st
import pandas as pd
import os
import sys

st.set_page_config(page_title="Payroll Timecode Entry", layout="wide")
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
    header="Supervisors and payroll staff",
    purpose="Submit and verify timecode entries used for payroll processing.",
    usage="Use dropdowns to select employee and week, then enter hours by category. Hover icons provide guidance.",
    routing="Saved data populates payroll_journal.csv and supports payroll summary reports."
)

st.title("⏱️ Payroll Timecode Entry")

# Load employee data
employee_df = pd.read_csv(os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_records.csv"))
employee_names = employee_df["Full Name"].tolist()

# Time entry form
with st.form("timecode_form"):
    name = st.selectbox("Employee Name 🛈", employee_names, help="Select employee submitting hours.")
    employee_id = employee_df.loc[employee_df["Full Name"] == name, "Employee ID"].values[0]
    week_ending = st.date_input("Week Ending 🛈", help="Last day of the pay period.")
    regular_hours = st.number_input("Regular Hours 🛈", min_value=0.0, help="Enter total regular hours worked.", step=0.5)
    overtime_hours = st.number_input("Overtime Hours 🛈", min_value=0.0, help="Enter total overtime hours worked.", step=0.5)
    sick_hours = st.number_input("Sick Hours 🛈", min_value=0.0, help="Enter sick leave hours, if any.", step=0.5)
    vacation_hours = st.number_input("Vacation Hours 🛈", min_value=0.0, help="Enter vacation or PTO hours, if any.", step=0.5)
    submit = st.form_submit_button("Submit Time Entry")

if submit:
    st.success(f"Time entry submitted for {name} (ID: {employee_id})")

# Sample log
st.subheader("🗂️ Time Entry Log (example)")
example = pd.DataFrame({
    "Employee": ["G. Adams", "K. Liu"],
    "Week Ending": ["2024-06-07", "2024-06-14"],
    "Reg Hrs": [40, 38],
    "OT Hrs": [5, 0]
})
st.dataframe(example)

csv = example.to_csv(index=False).encode("utf-8")
st.download_button("📥 Export Time Journal", data=csv, file_name="payroll_journal.csv")

# Footer
display_abl_footer()
display_gui_version("payroll_timecode_entry_gui.py", version="v3.1")
