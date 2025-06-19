import streamlit as st
import pandas as pd
from pathlib import Path

# Load logo
logo_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png").expanduser()
st.image(str(logo_path), width=120)

# Title
st.title("🧾 Grant Code Manager")
st.caption("Define and manage internal grant codes for fiscal tracking and reporting.")

# Load CSV
csv_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants/grant_codes.csv").expanduser()
csv_path.parent.mkdir(parents=True, exist_ok=True)

if csv_path.exists():
    df = pd.read_csv(csv_path)
else:
    df = pd.DataFrame(columns=["Grant Code", "Funding Source", "Start Date", "End Date", "Amount", "Notes"])

# Entry Form
with st.form("grant_code_form"):
    st.subheader("➕ Add or Update Grant Code")

    grant_code = st.text_input("Grant Code", help="Internal tracking label used in accounting and reports.")
    funding_source = st.text_input("Funding Source", help="Name of the agency, program, or foundation issuing the grant.")
    start_date = st.date_input("Start Date", help="Official beginning of the funded period.")
    end_date = st.date_input("End Date", help="Official conclusion of the funded period.")
    amount = st.number_input("Total Funding Amount ($)", min_value=0.0, step=1000.0, format="%.2f", help="Entire amount awarded to the organization.")
    notes = st.text_area("Notes (Optional)", help="Any limits, categories, or internal tags for staff clarity.")

    submitted = st.form_submit_button("Save Grant Code")

    if submitted and grant_code:
        new_entry = {
            "Grant Code": grant_code,
            "Funding Source": funding_source,
            "Start Date": start_date,
            "End Date": end_date,
            "Amount": amount,
            "Notes": notes
        }
        df = df[df["Grant Code"] != grant_code]
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_csv(csv_path, index=False)
        st.success(f"✅ Grant code '{grant_code}' saved.")

# Viewer
if not df.empty:
    st.subheader("📋 Existing Grant Codes")
    st.dataframe(df.sort_values("Grant Code"))
else:
    st.info("No grant codes added yet.")
