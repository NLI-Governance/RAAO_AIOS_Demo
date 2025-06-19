# adjustment_entry_gui_FINAL_LOCKED.py
# Purpose: Authorized entry of accounting ledger adjustments with audit trail
# Standards: ABL_Rev2_6_1_25, GAAP, IRS 990, 2 CFR Part 200

import streamlit as st
from datetime import date
from PIL import Image
import os
import csv

st.set_page_config(page_title="Ledger Adjustment Entry", layout="centered")

# Logo
logo_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
if os.path.exists(logo_path):
    st.image(Image.open(logo_path), width=150)

st.title("🧾 Ledger Adjustment Entry")
st.markdown("🔒 _Authorized personnel only_")
st.caption("Use this form to record corrections or adjustments to the accounting ledger. All changes are logged.")

ledger_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/data/financial/accounting.csv")

with st.form("adjustment_form"):
    reference_date = st.date_input("Reference Date", value=date.today(), help="The date the original transaction occurred.")
    amount = st.number_input("Adjustment Amount ($)", step=0.01, help="Enter a negative or positive amount to correct the ledger.")
    category = st.selectbox("Affected Category", ["Travel", "Supplies", "Personnel", "Admin", "Technology", "Facilities"],
                            help="Budget category being adjusted.")
    ledger_tag = st.text_input("Ledger Tag / Subcode (optional)", help="Use for internal ID like VOID-002 or AJ-105 if applicable.")
    justification = st.text_area("Explanation / Justification", help="Required. Clearly explain the reason for this adjustment.")
    approved_by = st.text_input("Approved By", help="Name of the authorized staff reviewing this entry.")

    confirm = st.checkbox("I confirm this adjustment is approved and necessary.")

    submitted = st.form_submit_button("Record Adjustment")

if submitted:
    if not confirm:
        st.error("You must confirm authorization before saving.")
    elif not justification or not approved_by:
        st.error("Justification and approval are required.")
    else:
        headers = ["Date", "Vendor", "Amount", "Account Type", "Category", "Description", "Approved By"]
        entry = [
            reference_date,
            ledger_tag if ledger_tag else "Manual Adjustment",
            f"{amount:.2f}",
            "Adjustment",
            category,
            justification,
            approved_by
        ]
        write_header = not os.path.exists(ledger_path)
        with open(ledger_path, "a", newline="") as f:
            writer = csv.writer(f)
            if write_header:
                writer.writerow(headers)
            writer.writerow(entry)

        st.success("✅ Adjustment recorded and saved to ledger.")
        st.write("**Amount:**", amount)
        st.write("**Explanation:**", justification)
