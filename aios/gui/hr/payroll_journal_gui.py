import streamlit as st
import pandas as pd
from pathlib import Path

# Logo
st.image("/Users/timothygriffin/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png", width=120)

# Title
st.title("💵 Payroll Journal")
st.markdown("Review detailed payroll journal entries, including grant allocations and deductions.")

# CSV path
csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/payroll_journal.csv").expanduser()

# Load CSV
if not csv_path.exists():
    st.warning("⚠️ No payroll journal CSV found.")
    st.markdown("""
    <details>
    <summary style='cursor: pointer; color: #e74c3c'><strong>📘 Explanation of Fields</strong></summary>
    <ul>
        <li><strong>Employee Name</strong>: Full legal name of employee.</li>
        <li><strong>Employee ID</strong>: Unique ID from HR onboarding.</li>
        <li><strong>Pay Period Start/End</strong>: The beginning and end dates of the payroll cycle.</li>
        <li><strong>Base Pay</strong>: Standard gross pay based on position.</li>
        <li><strong>Overtime Pay</strong>: Pay beyond standard hours.</li>
        <li><strong>Deductions</strong>: Withholdings (e.g., taxes, benefits).</li>
        <li><strong>Grant Allocations</strong>: Breakdown of funding sources by percentage or dollar.</li>
        <li><strong>Net Pay</strong>: Final amount after deductions.</li>
    </ul>
    </details>
    """, unsafe_allow_html=True)
else:
    df = pd.read_csv(csv_path)
    st.dataframe(df, use_container_width=True)
    st.download_button("📥 Download Payroll Journal", data=df.to_csv(index=False), file_name="payroll_journal.csv")
