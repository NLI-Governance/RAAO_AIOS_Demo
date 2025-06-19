import streamlit as st
import pandas as pd
import os
import sys

st.set_page_config(page_title="Vendor Payment Log", layout="wide")
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
    header="Accounts Payable staff and finance reviewers",
    purpose="Track and confirm payments made to vendors for approved invoices.",
    usage="Log details of each payment including vendor, invoice number, and payment method. Use hover help for field guidance.",
    routing="Data is stored in vendor_payment_log.csv for reporting and reconciliation."
)

st.title("🏦 Vendor Payment Log")

with st.form("payment_form"):
    vendor = st.text_input("Vendor Name 🛈", help="Enter the full name of the vendor paid.")
    invoice_number = st.text_input("Invoice Number 🛈", help="Invoice number associated with this payment.")
    payment_date = st.date_input("Payment Date 🛈", help="Date the payment was processed.")
    payment_amount = st.number_input("Payment Amount 🛈", min_value=0.0, help="Enter the total paid (USD).", step=0.01)
    payment_method = st.selectbox("Payment Method 🛈", ["ACH", "Check", "Wire", "Card"], help="How was the payment made?")
    confirmation = st.text_input("Confirmation # 🛈", help="Reference or check number for the payment, if available.")
    submitted = st.form_submit_button("Log Payment")

if submitted:
    st.success(f"Payment of ${payment_amount:.2f} logged for invoice {invoice_number}")

# Example table
st.subheader("🗂️ Sample Payment Log")
example = pd.DataFrame({
    "Vendor": ["Office Supply Co", "Fleet Maintenance Inc"],
    "Invoice #": ["INV-1033", "FLE-7781"],
    "Amount Paid": [245.60, 1023.75]
})
st.dataframe(example)

csv = example.to_csv(index=False).encode("utf-8")
st.download_button("📥 Export Payment Log", data=csv, file_name="vendor_payment_log.csv")

# Footer
display_abl_footer()
display_gui_version("vendor_payment_log_gui.py", version="v3.1")
