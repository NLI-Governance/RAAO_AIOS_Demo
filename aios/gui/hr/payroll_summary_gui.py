# payroll_summary_gui.py
# Purpose: Review employee payroll summaries and funding source breakdowns
# Standards: Internal financial tracking, grant compliance, HR alignment

import streamlit as st
import pandas as pd
import os

CSV_PATH = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/payroll_summary.csv")
LOGO_PATH = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")

st.set_page_config(page_title="Payroll Summary Viewer", layout="centered")
if os.path.exists(LOGO_PATH):
    st.image(LOGO_PATH, width=120)

st.title("💵 Payroll Summary")
st.caption("View payroll totals and grant funding splits by employee.")

if os.path.exists(CSV_PATH):
    df = pd.read_csv(CSV_PATH)
    st.dataframe(df, use_container_width=True)
else:
    st.warning("⚠️ No payroll summary CSV found.")

with st.expander("ℹ️ Explanation of Fields"):
    st.markdown("""
    - **Employee Name**: Full name of the staff member.
    - **Employee ID**: Unique internal ID for HR/payroll tracking.
    - **Period Start / End**: The start and end of the pay period.
    - **Total Hours**: All hours logged by the employee during the period.
    - **Base Pay**: Standard wage for the employee before grants.
    - **Overtime**: Additional pay beyond standard hours.
    - **Funding Source(s)**: Breakdown of which grants or accounts the time was charged to.
    - **Total Pay**: Gross pay before deductions.
    """)
