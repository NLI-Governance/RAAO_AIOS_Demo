import streamlit as st
import pandas as pd
import os

# Properly expand the logo path
logo_path = os.path.expanduser('~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png')

# Load volunteer records CSV
csv_path = os.path.expanduser('~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/volunteers/volunteer_records.csv')
if not os.path.exists(csv_path):
    st.error("Volunteer records CSV not found.")
    st.stop()

df = pd.read_csv(csv_path)

# Page setup
st.set_page_config(page_title="Volunteer Records Viewer", layout="wide")

# Header
if os.path.exists(logo_path):
    st.image(logo_path, width=120)
st.title("📋 Volunteer Records Viewer")
st.markdown("View and filter all submitted volunteer onboarding records.")

# Sidebar filters
st.sidebar.header("🔍 Filter Volunteers")
departments = ["All"] + sorted(df["Assigned Department"].dropna().unique().tolist())
selected_dept = st.sidebar.selectbox("Department", departments)

supervisors = ["All"] + sorted(df["Supervisor"].dropna().unique().tolist())
selected_supervisor = st.sidebar.selectbox("Supervisor", supervisors)

# Apply filters
filtered_df = df.copy()
if selected_dept != "All":
    filtered_df = filtered_df[filtered_df["Assigned Department"] == selected_dept]
if selected_supervisor != "All":
    filtered_df = filtered_df[filtered_df["Supervisor"] == selected_supervisor]

# Results
st.subheader(f"Showing {len(filtered_df)} volunteer record(s)")
st.dataframe(filtered_df, use_container_width=True)

# Download
st.download_button(
    label="📥 Download Filtered Data",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_volunteer_records.csv",
    mime="text/csv"
)
