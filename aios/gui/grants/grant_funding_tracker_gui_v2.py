import streamlit as st
import pandas as pd
from pathlib import Path
from datetime import date

# Set paths
data_dir = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants").expanduser()
tracker_path = data_dir / "grant_funding_tracker.csv"
code_path = data_dir / "grant_code_manager.csv"

# Load existing grant names and codes
if code_path.exists():
    code_df = pd.read_csv(code_path)
    grant_names = code_df["Grant Name"].dropna().unique().tolist()
    grant_codes = code_df["Grant Code"].dropna().unique().tolist()
else:
    grant_names = []
    grant_codes = []

st.set_page_config(page_title="Grant Funding Tracker", layout="centered")
st.image(str(Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png").expanduser()), width=100)

st.title("💸 Grant Funding Tracker")

with st.form("grant_funding_form"):
    col1, col2 = st.columns(2)

    with col1:
        grant_name = st.selectbox("Grant Name", options=grant_names)
        amount_spent = st.number_input("Amount Spent", min_value=0.0, step=1.0, format="%.2f")
        date_of_expense = st.date_input("Date", value=date.today())
    with col2:
        grant_code = st.selectbox("Grant Code", options=grant_codes)
        category = st.text_input("Category (e.g., Equipment, Staff, Services)")
        entered_by = st.text_input("Entered By (Initials or Name)")

    description = st.text_area("Brief Description")

    submitted = st.form_submit_button("Add Entry")
    if submitted:
        if not all([grant_name, grant_code, amount_spent, category, entered_by]):
            st.error("❗ All fields must be filled out.")
        else:
            new_entry = pd.DataFrame([{
                "Grant Name": grant_name,
                "Grant Code": grant_code,
                "Amount Spent": amount_spent,
                "Category": category,
                "Description": description,
                "Date": date_of_expense.strftime("%Y-%m-%d"),
                "Entered By": entered_by
            }])
            if tracker_path.exists():
                existing = pd.read_csv(tracker_path)
                updated = pd.concat([existing, new_entry], ignore_index=True)
            else:
                updated = new_entry
            updated.to_csv(tracker_path, index=False)
            st.success("✅ Entry successfully added to the grant funding tracker!")

# Optional: Display current entries
if tracker_path.exists():
    with st.expander("📊 View All Entries"):
        st.dataframe(pd.read_csv(tracker_path))
