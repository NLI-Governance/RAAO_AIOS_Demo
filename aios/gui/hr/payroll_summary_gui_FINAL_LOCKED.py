import streamlit as st
import pandas as pd
from pathlib import Path

# Logo
st.image("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png", width=120)

st.markdown("## 💵 Payroll Summary")
st.caption("View payroll totals and grant funding splits by employee.")

# Load payroll CSV
csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/payroll_summary.csv").expanduser()

if csv_path.exists():
    df = pd.read_csv(csv_path)

    # Optional filters could be added here
    st.dataframe(df, use_container_width=True)
else:
    st.warning("⚠️ No payroll summary CSV found.")

# Expandable Explanation of Fields
with st.expander("📘 Explanation of Fields"):
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
