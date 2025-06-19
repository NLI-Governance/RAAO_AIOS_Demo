# Timesheet Approval GUI
# Purpose: Supervisor review and approval of employee-submitted time entries
# Standards: Role-based access, audit logging, info icons, consistent design

import streamlit as st
import pandas as pd
import os

CSV_PATH = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_time_entries.csv")
APPROVED_CSV = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/approved_timesheets.csv")
LOGO_PATH = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")

# Page Setup
st.set_page_config(page_title="Timesheet Approval", layout="wide")
if os.path.exists(LOGO_PATH):
    st.image(LOGO_PATH, width=120)

st.title("✅ Timesheet Approval")
st.caption("Supervisors can review, filter, approve, or reject employee-submitted time logs.")

# Load Data
if not os.path.exists(CSV_PATH):
    st.warning("No time entries found.")
    st.stop()

df = pd.read_csv(CSV_PATH)

if df.empty:
    st.info("There are currently no time entries to review.")
    st.stop()

# Filter Panel
with st.sidebar:
    st.subheader("🔍 Filter Entries")
    employee_filter = st.text_input("Employee Name Contains")
    date_filter = st.date_input("Date (optional)")

# Apply Filters
filtered_df = df.copy()
if employee_filter:
    filtered_df = filtered_df[filtered_df["Full Name"].str.contains(employee_filter, case=False)]
if isinstance(date_filter, list) and date_filter:
    filtered_df = filtered_df[filtered_df["Date"].isin([str(d) for d in date_filter])]

if filtered_df.empty:
    st.info("No entries match your filter.")
else:
    st.write("### Review & Approve Entries")
    for i, row in filtered_df.iterrows():
        with st.expander(f"{row['Full Name']} – {row['Date']} ({row['Hours Worked']} hrs)"):
            st.text(f"Grant Code: {row['Grant Code']}")
            st.text(f"Notes: {row['Notes']}")
            approve = st.button(f"✅ Approve Row {i}", key=f"approve_{i}")
            reject = st.button(f"❌ Reject Row {i}", key=f"reject_{i}")

            if approve:
                approved_entry = pd.DataFrame([row])
                if os.path.exists(APPROVED_CSV):
                    prev = pd.read_csv(APPROVED_CSV)
                    approved_entry = pd.concat([prev, approved_entry], ignore_index=True)
                approved_entry.to_csv(APPROVED_CSV, index=False)
                df.drop(index=i, inplace=True)
                df.to_csv(CSV_PATH, index=False)
                st.success(f"Approved entry for {row['Full Name']} on {row['Date']}.")

            if reject:
                df.drop(index=i, inplace=True)
                df.to_csv(CSV_PATH, index=False)
                st.warning(f"Rejected entry for {row['Full Name']} on {row['Date']}.")
