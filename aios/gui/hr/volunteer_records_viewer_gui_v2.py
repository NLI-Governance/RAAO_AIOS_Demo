import streamlit as st
import pandas as pd
import os

# Expandable file paths
logo_path = os.path.expanduser('~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png')
csv_path = os.path.expanduser('~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/volunteers/volunteer_records.csv')

# Streamlit setup
st.set_page_config(page_title="Volunteer Viewer", layout="wide")

# Load logo
if os.path.exists(logo_path):
    st.image(logo_path, width=120)

st.title("📋 Volunteer Records Viewer")
st.markdown("View, filter, and export submitted volunteer onboarding records.")

# Validate CSV path
if not os.path.exists(csv_path):
    st.error("Volunteer records CSV not found.")
    st.stop()

# Load CSV
df = pd.read_csv(csv_path)

# Filters
st.sidebar.header("🔍 Filter Volunteers")
dept_filter = st.sidebar.selectbox("Filter by Department", ["All"] + sorted(df["Assigned Department"].dropna().unique()))
sup_filter = st.sidebar.selectbox("Filter by Supervisor", ["All"] + sorted(df["Supervisor"].dropna().unique()))

filtered_df = df.copy()
if dept_filter != "All":
    filtered_df = filtered_df[filtered_df["Assigned Department"] == dept_filter]
if sup_filter != "All":
    filtered_df = filtered_df[filtered_df["Supervisor"] == sup_filter]

# Auto-expand logic
st.subheader(f"Showing {len(filtered_df)} volunteer record(s)")
for idx, row in filtered_df.iterrows():
    with st.expander(f"🧾 {row['Full Name']} ({row['Assigned Department']})"):
        st.markdown(f"**Email:** {row['Email']}")
        st.markdown(f"**Phone:** {row['Phone']}")
        st.markdown(f"**Start Date:** {row['Start Date']}")
        st.markdown(f"**Volunteer ID:** {row['Volunteer ID']}")
        st.markdown(f"**Address:** {row['Street Address']}, {row['City']}, {row['State']} {row['ZIP Code']}")
        st.markdown(f"**Emergency Contact:** {row['Emergency Contact Name']} – {row['Emergency Contact Phone']}")
        st.markdown(f"**Supervisor:** {row['Supervisor']}")
        st.markdown(f"**Duties:** {row['Volunteer Duties']}")

# Export
st.download_button(
    label="📥 Download All Filtered Records",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_volunteer_records.csv",
    mime="text/csv"
)
