import streamlit as st
import pandas as pd
import os
import sys

st.set_page_config(page_title="Payroll Summary Viewer", layout="wide")
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
    header="Payroll administrators and executive review teams",
    purpose="Review summary payroll data for all employees across multiple pay periods.",
    usage="View, filter, and export pre-aggregated payroll summaries stored in payroll_summary.csv.",
    routing="Used for oversight, audits, and comparative trend analysis. Output does not affect time entries."
)

st.title("📊 Payroll Summary Viewer")

csv_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/payroll_summary.csv")

# Load payroll summary
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    st.dataframe(df)
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download Payroll Summary", data=csv, file_name="payroll_summary.csv")
else:
    st.warning("No payroll summary data found.")

# Footer
display_abl_footer()
display_gui_version("payroll_summary_viewer_gui.py", version="v3.1")
