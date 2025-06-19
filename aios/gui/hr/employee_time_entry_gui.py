# Employee Time Entry GUI
# Purpose: Allow employees to log hours worked and assign time to grant codes
# Standards: Role-based access, grant tracking, PTO integration, consistent UI formatting

import streamlit as st
import pandas as pd
import os
from datetime import date

# === Constants ===
CSV_PATH = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/hr/employee_time_entries.csv")
LOGO_PATH = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")

# === Page Setup ===
st.set_page_config(page_title="Employee Time Entry", layout="centered")
if os.path.exists(LOGO_PATH):
    st.image(LOGO_PATH, width=120)

st.title("🕒 Employee Time Entry")
st.caption("Log your daily or weekly hours, including grant or program assignment.")

# === Form Input ===
with st.form("time_entry_form"):
    st.subheader("Log Your Hours")

    name = st.text_input("Full Name")
    date_entry = st.date_input("Date", value=date.today())
    hours_worked = st.number_input("Total Hours Worked", min_value=0.0, step=0.25)
    grant_code = st.selectbox("Grant or Program Code", ["Select...", "GRANT-A", "GRANT-B", "ADMIN"])
    notes = st.text_area("Optional Notes", help="Describe the work performed if needed.")

    st.markdown(
        "<div style='margin-top: 10px;'>"
        "<span style='font-size: small;'>"
        "❓ <b>Grant Code:</b> Choose the funding source or administrative category that best matches this work."
        "</span></div>",
        unsafe_allow_html=True
    )

    submit = st.form_submit_button("Submit Entry")

    if submit:
        if name and grant_code != "Select..." and hours_worked > 0:
            new_entry = pd.DataFrame([[name, str(date_entry), hours_worked, grant_code, notes]],
                                     columns=["Full Name", "Date", "Hours Worked", "Grant Code", "Notes"])

            file_exists = os.path.exists(CSV_PATH)
            if file_exists:
                existing = pd.read_csv(CSV_PATH)
                updated = pd.concat([existing, new_entry], ignore_index=True)
            else:
                updated = new_entry

            updated.to_csv(CSV_PATH, index=False)
            st.success("✅ Entry submitted and saved.")
        else:
            st.error("Please complete all required fields and ensure hours are greater than zero.")
