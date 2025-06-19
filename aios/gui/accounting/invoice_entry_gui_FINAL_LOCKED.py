# invoice_entry_gui_FINAL_LOCKED_0604.py
# Purpose: Invoice submission and AI description tool
# Standards: ABL_Rev2_6_1_25, GAAP, OCR audit-ready

import streamlit as st
from datetime import date
from PIL import Image
import os
import csv

st.set_page_config(page_title="Invoice Entry", layout="centered")

# Logo
logo_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
if os.path.exists(logo_path):
    st.image(Image.open(logo_path), width=150)

st.title("🧾 Invoice Entry")
st.caption("Enter invoice information for processing. Upload optional scan or image.")

ledger_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/data/financial/accounting.csv")

with st.form("invoice_entry_form"):
    invoice_date = st.date_input("Invoice Date", value=date.today(), help="Date shown on the invoice.")
    vendor = st.text_input("Vendor", help="Company or person that issued the invoice.")
    amount = st.number_input("Invoice Amount ($)", min_value=0.01, step=0.01, help="Invoice total due.")
    category = st.selectbox("Expense Category", ["Travel", "Supplies", "Personnel", "Admin", "Technology", "Facilities"],
                            help="Budget category this expense belongs to.")
    approved_by = st.text_input("Approved By", help="Name of staff who approved this expense.")
    description = st.text_area("Description / Purpose", help="Brief description of invoice purpose.")

    uploaded_file = st.file_uploader("Upload Invoice (optional)", type=["jpg", "jpeg", "png", "pdf"])

    submitted = st.form_submit_button("Submit Invoice")

if submitted:
    headers = ["Date", "Vendor", "Amount", "Account Type", "Category", "Description", "Approved By"]
    entry = [
        invoice_date,
        vendor,
        f"{amount:.2f}",
        "Invoice",
        category,
        description,
        approved_by
    ]

    write_header = not os.path.exists(ledger_path)
    with open(ledger_path, "a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(headers)
        writer.writerow(entry)

    st.success("✅ Invoice recorded and saved to ledger.")

    if uploaded_file:
        st.info(f"Uploaded: {uploaded_file.name}")
