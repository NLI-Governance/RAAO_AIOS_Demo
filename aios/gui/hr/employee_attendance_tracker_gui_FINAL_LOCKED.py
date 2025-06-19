import streamlit as st
import pandas as pd
from pathlib import Path

# Logo and title
st.image(str(Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png").expanduser()), width=120)
st.title("📅 Employee Attendance Tracker")
st.caption("Track employee daily attendance, late arrivals, and absences.")

# Load CSV path
csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_attendance_log.csv").expanduser()

# Ensure data directory exists
csv_path.parent.mkdir(parents=True, exist_ok=True)

# Initialize CSV
if csv_path.exists():
    df = pd.read_csv(csv_path)
else:
    df = pd.DataFrame(columns=[
        "Employee Name", "Employee ID", "Date", "Status", "Check-In Time", "Check-Out Time", "Notes"
    ])

with st.form("attendance_form"):
    st.subheader("📋 Record Attendance")

    col1, col2 = st.columns(2)
    with col1:
        employee_name = st.text_input("Employee Name", help="Enter the full name of the employee.")
        employee_id = st.text_input("Employee ID", help="Enter the unique ID assigned during onboarding.")
    with col2:
        date = st.date_input("Date", help="Select the date for this attendance record.")
        status = st.selectbox("Attendance Status", ["Present", "Absent", "Late"], help="Mark the employee's status.")

    checkin = st.time_input("Check-In Time", help="Time the employee checked in.")
    checkout = st.time_input("Check-Out Time", help="Time the employee checked out.")
    notes = st.text_area("Notes", help="Optional comments about today's attendance.")

    submitted = st.form_submit_button("Save Record")

    if submitted:
        new_record = {
            "Employee Name": employee_name,
            "Employee ID": employee_id,
            "Date": date,
            "Status": status,
            "Check-In Time": checkin,
            "Check-Out Time": checkout,
            "Notes": notes
        }
        df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)
        df.to_csv(csv_path, index=False)
        st.success("✅ Attendance record saved successfully.")

st.markdown("---")
st.subheader("🗂️ Attendance Log")
if df.empty:
    st.warning("No attendance records found.")
else:
    st.dataframe(df, use_container_width=True)
    st.download_button("📥 Download CSV", data=df.to_csv(index=False), file_name="employee_attendance_log.csv", mime="text/csv")
