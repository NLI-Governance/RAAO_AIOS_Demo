# accounting_view_gui_FINAL_LOCKED_0604.py
# Purpose: View and filter accounting ledger with tooltip guidance
# Standards: GAAP, ABL_Rev2_6_1_25, audit-readiness

import streamlit as st
import pandas as pd
import os
from PIL import Image

st.set_page_config(page_title="Accounting Ledger Viewer", layout="centered")

# Logo
logo_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
if os.path.exists(logo_path):
    st.image(Image.open(logo_path), width=150)

st.title("📊 Accounting Ledger Viewer")
st.caption("Use the filters to view and search accounting transactions stored in the AIOS ledger.")

# Ledger path
csv_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/data/financial/accounting.csv")

# Load data
if not os.path.exists(csv_path):
    st.warning("⚠️ No ledger data found.")
else:
    df = pd.read_csv(csv_path)

    with st.expander("🔎 Filter Ledger Entries", expanded=True):
        vendor_filter = st.text_input("Vendor Contains", help="Search by vendor or source name.")
        account_type_filter = st.selectbox("Account Type", ["All", "Expense", "Income", "Adjustment", "Grant", "Other"],
                                           help="Filter by type of accounting entry.")
        approver_filter = st.text_input("Approved By Contains", help="Search by the name of the approving person.")

    # Apply filters
    filtered_df = df.copy()

    if vendor_filter:
        filtered_df = filtered_df[filtered_df["Vendor"].str.contains(vendor_filter, case=False, na=False)]

    if account_type_filter != "All":
        filtered_df = filtered_df[filtered_df["Account Type"] == account_type_filter]

    if approver_filter:
        filtered_df = filtered_df[filtered_df["Approved By"].str.contains(approver_filter, case=False, na=False)]

    st.markdown("### 💼 Filtered Results")
    st.dataframe(filtered_df, use_container_width=True)
