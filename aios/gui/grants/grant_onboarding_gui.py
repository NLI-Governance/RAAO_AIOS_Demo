# grant_onboarding_gui.py
# Purpose: Onboard new grants into AIOS with metadata and compliance info
# Standards: 2 CFR Part 200, IRS 990, ISO 9001, ABL_Rev2_6_1_25

import streamlit as st
import pandas as pd
from datetime import date
import os
from PIL import Image

st.set_page_config(page_title="Grant Onboarding", layout="wide")

# -- Logo --
logo_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
if os.path.exists(logo_path):
    st.image(logo_path, width=150)

st.title("🏛️ Grant Onboarding Form")

# -- Grant Info --
st.header("Grant Information")
grantor = st.text_input("Grantor Name")
grant_title = st.text_input("Grant Title")
cfda = st.text_input("CFDA Number (if federal grant)")
amount = st.text_input("Total Award Amount (USD)")
start_date = st.date_input("Grant Start Date")
end_date = st.date_input("Grant End Date")
contact = st.text_input("Grantor Contact Email")

# -- Purpose and Restrictions --
st.header("Use and Restrictions")
purpose = st.text_area("Describe the grant purpose or funded activities")
restricted = st.selectbox("Is this a restricted-use grant?", ["Yes", "No"])
match_required = st.selectbox("Does the grant require cost matching?", ["Yes", "No"])

# -- Reporting and Compliance --
st.header("Compliance and Reporting")
reporting_schedule = st.selectbox("Required Reporting Frequency", [
    "Monthly", "Quarterly", "Biannual", "Annual", "Final Only"
])
deliverables = st.text_area("List required reports or deliverables")

# -- Submit Button --
if st.button("Register Grant"):
    if grantor and grant_title and amount and start_date and end_date:
        record = {
            "Timestamp": date.today().isoformat(),
            "Grantor": grantor,
            "Title": grant_title,
            "CFDA": cfda,
            "Amount": amount,
            "Start Date": start_date,
            "End Date": end_date,
            "Contact": contact,
            "Purpose": purpose,
            "Restricted": restricted,
            "Match Required": match_required,
            "Reporting Frequency": reporting_schedule,
            "Deliverables": deliverables
        }

        df = pd.DataFrame([record])
        csv_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/data/grants/grants.csv")
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)

        if os.path.exists(csv_path):
            df.to_csv(csv_path, mode="a", header=False, index=False)
        else:
            df.to_csv(csv_path, index=False)

        st.success("Grant registered successfully.")
    else:
        st.error("Grantor, Title, Amount, and Dates are required.")
