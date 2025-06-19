# accounting_view_gui.py
# Purpose: View and filter accounting.csv entries using Streamlit
# Standards: ABL_Rev2_6_1_25, IRS Recordkeeping, ISO 9001 (accounting records)

import streamlit as st
import pandas as pd
import os
from PIL import Image

st.set_page_config(page_title="Accounts Payable Viewer", layout="wide")

# -- Logo Display --
logo_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.image(logo, width=150)

st.title("📊 Accounting Ledger Viewer")

# -- Load Data --
csv_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/data/financial/accounting.csv")

if not os.path.exists(csv_path):
    st.warning("No accounting.csv file found yet.")
else:
    df = pd.read_csv(csv_path)

    # -- Optional Filters --
    with st.sidebar:
        st.header("🔍 Filter Entries")
        vendor_filter = st.text_input("Vendor Contains")
        account_filter = st.selectbox("Account Type", ["All"] + sorted(df["Account"].unique()))
        reviewer_filter = st.text_input("Approved By Contains")

    filtered_df = df.copy()

    if vendor_filter:
        filtered_df = filtered_df[filtered_df["Vendor"].str.contains(vendor_filter, case=False)]
    if reviewer_filter:
        filtered_df = filtered_df[filtered_df["Approved By"].str.contains(reviewer_filter, case=False)]
    if account_filter != "All":
        filtered_df = filtered_df[filtered_df["Account"] == account_filter]

    st.markdown(f"🔎 Showing {len(filtered_df)} of {len(df)} total entries")

    st.dataframe(filtered_df, use_container_width=True)
