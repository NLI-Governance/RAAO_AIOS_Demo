import streamlit as st
import pandas as pd
import os

# Logo
st.image(os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png"), width=120)

# Title
st.markdown("### 🗂️ Volunteer Records Viewer")
st.caption("View, filter, and export submitted volunteer onboarding records.")

# CSV path
csv_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/volunteers/volunteer_records.csv")

# Load data
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)

    # Sidebar filters
    st.sidebar.header("🔍 Filter Volunteers")
    departments = ["All"] + sorted(df["Assigned Department"].dropna().unique())
    supervisors = ["All"] + sorted(df["Supervisor"].dropna().unique())

    dept_filter = st.sidebar.selectbox("Filter by Department", departments)
    supervisor_filter = st.sidebar.selectbox("Filter by Supervisor", supervisors)

    # Apply filters
    filtered_df = df.copy()
    if dept_filter != "All":
        filtered_df = filtered_df[filtered_df["Assigned Department"] == dept_filter]
    if supervisor_filter != "All":
        filtered_df = filtered_df[filtered_df["Supervisor"] == supervisor_filter]

    # Show results
    st.write(f"### Showing {len(filtered_df)} volunteer record(s)")
    st.dataframe(filtered_df, use_container_width=True)

    # Export
    csv = filtered_df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Download All Filtered Records", csv, "filtered_volunteer_records.csv", "text/csv")

else:
    st.error("Volunteer records CSV not found.")
