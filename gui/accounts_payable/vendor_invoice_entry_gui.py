import streamlit as st
import pandas as pd
import os
import sys

st.set_page_config(page_title="Vendor Invoice Entry", layout="wide")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from tools.shared_ui_components import (
    display_logo,
    display_abl_footer,
    display_gui_version,
    display_about_this_form,
    display_language_toggle_button,
    display_policy_assistant_button
)

# Top layout
cols = st.columns([6, 1, 1])
with cols[0]: display_logo()
with cols[1]: display_language_toggle_button()
with cols[2]: display_policy_assistant_button()

display_about_this_form(
    header="Accounts Payable clerks and finance team",
    purpose="Submit vendor invoice details for tracking, payment scheduling, and audit readiness.",
    usage="Use hover icons for format guidance. Each invoice must include a vendor, amount, and unique invoice number.",
    routing="Records are stored in vendor_invoices_log.csv and routed for approval and batch processing."
)

st.title("💳 Vendor Invoice Entry Form")

with st.form("invoice_form"):
    vendor = st.text_input("Vendor Name 🛈", help="Enter the official name of the vendor as listed on the invoice.")
    invoice_number = st.text_input("Invoice Number 🛈", help="Include the unique invoice number exactly as printed.")
    invoice_date = st.date_input("Invoice Date 🛈", help="Date printed on the vendor invoice.")
    amount = st.number_input("Invoice Amount 🛈", min_value=0.0, help="Enter total invoice value in USD.", step=0.01)
    due_date = st.date_input("Payment Due Date 🛈", help="Deadline for payment as indicated on the invoice.")
    description = st.text_area("Purpose / Description 🛈", help="Describe what goods or services this invoice covers.")
    submitted = st.form_submit_button("Submit Invoice")

if submitted:
    st.success(f"Invoice {invoice_number} submitted for {vendor}")

# Example table
st.subheader("🗂️ Vendor Invoice Log (example)")
example = pd.DataFrame({
    "Vendor": ["Office Supply Co", "Fleet Maintenance Inc"],
    "Invoice #": ["INV-1033", "FLE-7781"],
    "Amount": [245.60, 1023.75]
})
st.dataframe(example)

csv = example.to_csv(index=False).encode("utf-8")
st.download_button("📥 Export Invoice Log", data=csv, file_name="vendor_invoices_log.csv")

# Footer
display_abl_footer()
display_gui_version("vendor_invoice_entry_gui.py", version="v3.1")
