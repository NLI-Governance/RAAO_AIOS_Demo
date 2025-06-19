import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Employee Records Viewer", layout="wide")

# Load logo
st.image("/Users/timothygriffin/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png", width=120)

st.title("👤 Employee Records Viewer")
st.markdown("Browse and filter complete employee records stored in your HR system.")

# Path to CSV
csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employees.csv").expanduser()

if not csv_path.exists():
    st.warning("⚠️ No employee records found.")
    st.stop()

# Load data
df = pd.read_csv(csv_path)

# Filters
st.sidebar.header("🔍 Filter Records")
filter_dept = st.sidebar.selectbox("Department", ["All"] + sorted(df["Department"].dropna().unique()))
filter_mgr = st.sidebar.selectbox("Manager", ["All"] + sorted(df["Manager"].dropna().unique()))

if filter_dept != "All":
    df = df[df["Department"] == filter_dept]
if filter_mgr != "All":
    df = df[df["Manager"] == filter_mgr]

st.markdown(f"### Displaying {len(df)} Employee Record(s)")
st.dataframe(df, use_container_width=True)

st.download_button(
    label="📥 Download Filtered Employee CSV",
    data=df.to_csv(index=False).encode("utf-8"),
    file_name="filtered_employees.csv",
    mime="text/csv"
)

# Info block
with st.expander("ℹ️ Field Descriptions"):
    st.markdown("""
    - **Full Name:** Legal name of the employee
    - **Position:** Job title or role
    - **Start Date:** Employment begin date
    - **Email / Phone:** Contact info on record
    - **Department:** Assigned internal division
    - **Manager:** Direct supervisor
    - **Employee ID:** Unique HR identifier
    - **Tax Form Received:** HR confirmation (Yes/No)
    - **Notes:** Internal notes (not shown to employees)
    """)

