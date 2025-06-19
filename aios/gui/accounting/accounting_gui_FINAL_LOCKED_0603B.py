# accounting_gui_FINAL_LOCKED_0603B.py
# Purpose: Accounting entry GUI with tooltip guidance and AIOS CSV ledger output
# Standards: GAAP, IRS 990, 2 CFR Part 200, ABL_Rev2_6_1_25

import streamlit as st
from datetime import date
from PIL import Image
import os
import csv

st.set_page_config(page_title="Accounting Entry", layout="centered")

# --- Logo ---
logo_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
if os.path.exists(logo_path):
    st.image(Image.open(logo_path), width=150)

st.title("💵 Accounting Entry")
st.caption("Enter a financial transaction to be saved into the AIOS system.")

# Path to ledger
ledger_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/data/financial/accounting.csv")

with st.form("entry_form"):
    trans_date = st.date_input("Transaction Date", value=date.today(), help="Date the expense or deposit occurred.")
    vendor = st.text_input("Vendor / Source", help="Name of company or person this relates to.")
    amount = st.number_input("Amount ($)", min_value=0.01, step=0.01, help="Total dollar value.")
    account_type = st.selectbox("Account Type", ["Expense", "Income", "Reimbursement", "Grant", "Other"],
                                help="Classify the transaction.")
    category = st.selectbox("Category", ["Travel", "Supplies", "Personnel", "Admin", "Technology", "Facilities"],
                            help="Internal budget category.")
    description = st.text_area("Transaction Description", help="Short purpose or explanation.")
    approved_by = st.text_input("Approved By", help="Name of the person who approved it.")
    submitted = st.form_submit_button("Submit Entry")

if submitted:
    # Save to CSV
    headers = ["Date", "Vendor", "Amount", "Account Type", "Category", "Description", "Approved By"]
    entry = [trans_date, vendor, f"{amount:.2f}", account_type, category, description, approved_by]

    write_header = not os.path.exists(ledger_path)
    with open(ledger_path, "a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(headers)
        writer.writerow(entry)

    st.success("✅ Entry recorded and saved to ledger.")
    st.write("**Date:**", trans_date)
    st.write("**Vendor:**", vendor)
    st.write("**Amount:**", amount)
    st.write("**Account Type:**", account_type)
    st.write("**Category:**", category)
    st.write("**Approved By:**", approved_by)
    st.write("**Description:**", description)
