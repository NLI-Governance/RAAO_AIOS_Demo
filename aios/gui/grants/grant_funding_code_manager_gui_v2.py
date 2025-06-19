import streamlit as st
import pandas as pd
from pathlib import Path

logo_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png").expanduser()
st.image(str(logo_path), width=120)

st.title("🧾 Grant Code Manager")
st.caption("Define and manage internal grant codes for fiscal tracking and reporting.")

data_path = Path("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/data/grants/grant_codes.csv").expanduser()
data_path.parent.mkdir(parents=True, exist_ok=True)

if data_path.exists():
    df = pd.read_csv(data_path)
else:
    df = pd.DataFrame(columns=["Grant Code", "Funding Source", "Start Date", "End Date", "Amount", "Notes"])

with st.form("grant_code_form"):
    st.subheader("➕ Add or Update Grant Code")

    col1, col2 = st.columns([6,1])
    code = col1.text_input("Grant Code")
    col2.markdown("ⓘ", help="Enter the internal code used to reference this grant across accounting and reporting systems.")

    col1, col2 = st.columns([6,1])
    source = col1.text_input("Funding Source")
    col2.markdown("ⓘ", help="Specify the organization or agency providing this grant.")

    col1, col2 = st.columns([6,1])
    start_date = col1.date_input("Start Date")
    col2.markdown("ⓘ", help="Official grant start date.")

    col1, col2 = st.columns([6,1])
    end_date = col1.date_input("End Date")
    col2.markdown("ⓘ", help="Official grant end date.")

    col1, col2 = st.columns([6,1])
    amount = col1.number_input("Total Funding Amount ($)", min_value=0.00, step=1000.00, format="%.2f")
    col2.markdown("ⓘ", help="Enter the full grant award amount.")

    col1, col2 = st.columns([6,1])
    notes = col1.text_area("Notes")
    col2.markdown("ⓘ", help="Optional notes regarding purpose, constraints, or categories.")

    submitted = st.form_submit_button("Add or Update Code")

    if submitted and code:
        new_row = {
            "Grant Code": code,
            "Funding Source": source,
            "Start Date": start_date,
            "End Date": end_date,
            "Amount": amount,
            "Notes": notes
        }
        df = df[df["Grant Code"] != code]
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(data_path, index=False)
        st.success(f"Grant code '{code}' has been saved.")

if not df.empty:
    st.subheader("📄 Existing Grant Codes")
    st.dataframe(df.sort_values("Grant Code"))
else:
    st.warning("No grant codes available. Use the form above to add one.")
