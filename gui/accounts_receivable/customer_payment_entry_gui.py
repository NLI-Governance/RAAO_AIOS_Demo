import streamlit as st
import pandas as pd
import os
import sys

st.set_page_config(page_title="Customer Payment Entry", layout="wide")
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
    header="Accounts Receivable staff",
    purpose="Record incoming payments received from customers, clients, or funders.",
    usage="Be sure to assign each payment to the correct customer and reference number. Use hover help for guidance.",
    routing="Saved data goes to customer_payments_log.csv and supports reconciliation and audit processes."
)

st.title("💰 Customer Payment Entry")

with st.form("payment_form"):
    customer_name = st.text_input("Customer Name 🛈", help="Name of the customer, donor, or entity that submitted the payment.")
    payment_date = st.date_input("Payment Date 🛈", help="Date when the payment was received or posted.")
    amount_received = st.number_input("Amount Received 🛈", min_value=0.0, help="Enter the total amount received in USD.", step=0.01)
    reference_number = st.text_input("Reference Number 🛈", help="Optional internal or customer-facing reference (e.g., invoice or memo number).")
    payment_method = st.selectbox("Payment Method 🛈", ["Check", "ACH", "Wire", "Credit Card", "Cash"], help="Select how the payment was made.")
    notes = st.text_area("Notes 🛈", help="Any relevant notes such as source, reason, or restrictions.")
    submitted = st.form_submit_button("Log Payment")

if submitted:
    st.success(f"Payment of ${amount_received:.2f} logged for {customer_name}")

# Example table
st.subheader("🗂️ Sample Payment Log")
example = pd.DataFrame({
    "Customer": ["Smith Construction", "Greenway Health"],
    "Date": ["2024-05-20", "2024-06-10"],
    "Amount": [1200.00, 5000.00]
})
st.dataframe(example)

csv = example.to_csv(index=False).encode("utf-8")
st.download_button("📥 Export Payments Log", data=csv, file_name="customer_payments_log.csv")

# Footer
display_abl_footer()
display_gui_version("customer_payment_entry_gui.py", version="v3.1")
