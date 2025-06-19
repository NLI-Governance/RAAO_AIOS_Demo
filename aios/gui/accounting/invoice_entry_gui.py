# invoice_entry_gui.py
# Purpose: HITL review of OCR-extracted invoice metadata + AI summary + invoice preview
# Standards: ISO/IEC 27001, IRS Publication 1075, ABL_Rev2_6_1_25

import streamlit as st
import pandas as pd
from openai import OpenAI
import os
from datetime import datetime
from PIL import Image

st.set_page_config(page_title="Invoice Review", layout="wide")

# -- Logo --
logo_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.image(logo, width=150)

st.title("🧾 Invoice Entry – Human Review")

# -- Invoice Preview --
invoice_img_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/invoices/sample_invoice.jpg")
if os.path.exists(invoice_img_path):
    st.image(invoice_img_path, width=550, caption="Scanned Invoice Preview")
else:
    st.warning("No scanned invoice image found at expected path.")

# -- Simulated OCR Data --
sample_data = {
    "vendor": "Acme Supplies",
    "date": "2025-05-30",
    "amount": "1842.67"
}

vendor = st.text_input("Vendor", value=sample_data.get("vendor", ""))

# -- Date Input With Instruction --
st.markdown("📅 *Use the calendar picker below. Please avoid selecting browser autofill suggestions above.*")
invoice_date_obj = st.date_input("Invoice Date", value=datetime.strptime(sample_data["date"], "%Y-%m-%d"))
invoice_date = invoice_date_obj.strftime("%Y-%m-%d")

amount = st.text_input("Amount", value=sample_data.get("amount", ""))

# -- AI Description Generator --
st.markdown("🧠 **Generate Description Using AI (Optional)**")
if "ai_description" not in st.session_state:
    st.session_state.ai_description = ""

def generate_description(vendor, date, amount):
    prompt = (
        f"Write a professional internal invoice summary for a transaction from {vendor} on {date}, "
        f"totaling ${amount}. The summary should help accounting staff quickly understand the expense."
    )
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

if st.button("Generate Description with AI"):
    try:
        ai_result = generate_description(vendor, invoice_date, amount)
        st.session_state.ai_description = ai_result
        st.success("AI-generated description inserted.")
    except Exception as e:
        st.error(f"Error generating description: {e}")

description = st.text_area("Description or Notes", value=st.session_state.ai_description)

account = st.selectbox("Account Category", [
    "Operations", "Grant-Funded", "Supplies", "Travel", "Utilities",
    "Professional Services", "Equipment", "Office Supplies", "Reimbursements",
    "Marketing", "Training", "Miscellaneous"
])

approved_by = st.text_input("Reviewed and Approved By")

# -- Submit Button --
if st.button("Submit to Accounting"):
    if vendor and invoice_date and amount and approved_by:
        record = {
            "Timestamp": datetime.now().isoformat(),
            "Vendor": vendor,
            "Invoice Date": invoice_date,
            "Amount": amount,
            "Account": account,
            "Description": description,
            "Approved By": approved_by
        }

        df = pd.DataFrame([record])
        csv_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/data/financial/accounting.csv")
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)

        if os.path.exists(csv_path):
            df.to_csv(csv_path, mode="a", header=False, index=False)
        else:
            df.to_csv(csv_path, index=False)

        st.success("Invoice recorded in accounting ledger.")
    else:
        st.error("Vendor, Date, Amount, and Approver are required.")
