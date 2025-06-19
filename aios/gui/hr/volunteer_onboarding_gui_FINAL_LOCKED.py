import streamlit as st
import pandas as pd
from datetime import date, datetime
from PIL import Image
import os

st.set_page_config(page_title="Volunteer Onboarding", layout="wide")

# ---- Branding Logo ----
logo_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.image(logo, width=200)

st.title("Volunteer Onboarding Form")

# ---- Helper ----
def circular_info(text):
    st.markdown(f'<span style="border-radius: 50%; background:#ccc; padding: 3px 9px;">i</span> {text}', unsafe_allow_html=True)

# ---- Volunteer Contact Info ----
st.header("Your Contact Information")
col1, col2 = st.columns(2)
first_name = col1.text_input("First Name")
last_name = col2.text_input("Last Name")
phone = col1.text_input("Phone Number")
email = col2.text_input("Email Address")
address = st.text_input("Mailing Address")
dob = st.date_input("Date of Birth")

# ---- Emergency Contact ----
st.header("Emergency Contact")
ec_name = st.text_input("Emergency Contact Name")
ec_relation = st.text_input("Relationship to You")
ec_phone = st.text_input("Emergency Contact Phone")

# ---- Availability and Interests ----
st.header("Availability & Areas of Interest")
days_available = st.multiselect("Which days are you typically available?", [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
])
skills = st.text_area("What skills or experience would you like to share?")
interests = st.text_area("Any particular causes, departments, or roles you're most interested in?")

# ---- Waiver & Certification ----
st.header("Waiver and Certification")
st.markdown("✅ **Check the box below to acknowledge you are volunteering of your own free will and understand this is an unpaid position.**")
acknowledge = st.checkbox("I agree to the terms of volunteer service.")
signed_name = st.text_input("Type your full name to sign")
agree = st.checkbox("I certify the information I've provided is true and complete.")

# ---- Submission Logic ----
if st.button("Submit Volunteer Application"):
    if acknowledge and agree and signed_name:
        record = {
            "Timestamp": datetime.now().isoformat(),
            "First Name": first_name,
            "Last Name": last_name,
            "Phone": phone,
            "Email": email,
            "Address": address,
            "DOB": dob,
            "Emergency Name": ec_name,
            "Emergency Relation": ec_relation,
            "Emergency Phone": ec_phone,
            "Days Available": ", ".join(days_available),
            "Skills": skills,
            "Interests": interests,
            "Signed Name": signed_name,
            "Agreed to Waiver": acknowledge
        }

        df = pd.DataFrame([record])
        csv_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/aios/data/hr/volunteers.csv")
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)

        if os.path.exists(csv_path):
            df.to_csv(csv_path, mode='a', index=False, header=False)
        else:
            df.to_csv(csv_path, index=False)

        st.success("Thank you! Your volunteer application has been submitted.")
    else:
        st.error("You must check the waiver and sign your name to submit.")
