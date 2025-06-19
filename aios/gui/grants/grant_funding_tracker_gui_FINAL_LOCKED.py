import streamlit as st
import pandas as pd
from pathlib import Path

# Logo and Title
st.image(str(Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png").expanduser()), width=120)
st.title("💸 Grant Funding Tracker")
st.caption("Log expenses against specific grants and track usage against awarded amounts.")

# Load grant code data safely
grant_csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants/grant_codes.csv").expanduser()
if not grant_csv_path.exists():
    st.error("⚠️ grant_codes.csv not found. Please create it first.")
    st.stop()

grant_df = pd.read_csv(grant_csv_path)

# Validate required columns
required_columns = {"Grant Name", "Grant Code"}
if not required_columns.issubset(grant_df.columns):
    st.error(f"⚠️ grant_codes.csv is missing required columns: {required_columns}")
    st.stop()

# Pull-down menus for grant names and codes
grant_names = grant_df["Grant Name"].dropna().unique().tolist()
grant_codes = grant_df["Grant Code"].dropna().unique().tolist()

# Input form
with st.form("grant_funding_form"):
    grant_name = st.selectbox("Grant Name ❓", grant_names, help="Select the grant this funding is tied to.")
    grant_code = st.selectbox("Grant Code ❓", grant_codes, help="Select the corresponding tracking code.")
    amount = st.number_input("Amount Spent ❓", min_value=0.00, format="%.2f", help="Enter the amount spent.")
    date = st.date_input("Date of Expense ❓", help="Date the transaction occurred.")
    description = st.text_area("Description ❓", help="Optional notes or purpose of the expense.")
    submit = st.form_submit_button("Submit Expense")

# Save entry to CSV
if submit:
    log_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants/grant_funding_log.csv").expanduser()
    new_entry = pd.DataFrame([{
        "Grant Name": grant_name,
        "Grant Code": grant_code,
        "Amount": amount,
        "Date": date.strftime("%Y-%m-%d"),
        "Description": description
    }])
    if log_path.exists():
        existing = pd.read_csv(log_path)
        result = pd.concat([existing, new_entry], ignore_index=True)
    else:
        result = new_entry
    result.to_csv(log_path, index=False)
    st.success("✅ Expense recorded successfully.")
