#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# employee_onboarding_gui_v2.py
# Purpose: Internal HR onboarding GUI for finalized hires
# Standards: I-9 (USCIS), W-4 (IRS), EEOC, ADA, ISO 30414 (HR), ABL_Rev2_6_1_25

import streamlit as st
import datetime
import base64

st.set_page_config(page_title="Employee Onboarding", layout="centered")

st.image("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png", width=120)
st.title("🧾 Employee Onboarding Form")
st.markdown("Complete this form after candidate has accepted the job offer.")

# --- Employee Identity ---
st.header("Employee Identity")
full_name = st.text_input("Full Legal Name")
email = st.text_input("Email Address")
start_date = st.date_input("Planned Start Date", value=datetime.date.today())

# --- Government Compliance ---
st.header("Government Compliance")

with st.expander("ℹ️ What identification is required?"):
    st.markdown("""
    To comply with **federal I-9 requirements**, employees must present either:
    
    **One document from List A:**
    - U.S. Passport or Passport Card
    - Permanent Resident Card (Green Card)
    - Employment Authorization Document (EAD)
    
    **OR one document from List B AND one from List C:**
    - List B: Driver's License, State ID, School ID, Voter Registration Card
    - List C: Social Security Card, Birth Certificate, U.S. Citizen ID Card
    
    Employers must complete Section 2 of the I-9 within 3 business days of start.
    """)

w4_received = st.checkbox("W-4 Form has been completed and received")
i9_verified = st.checkbox("I-9 Verification Complete (per federal guidelines)")
id_upload = st.file_uploader("Upload Copies of Presented ID(s) (PDF or image format)", type=["pdf", "jpg", "png"]) 

# --- Emergency Contact ---
st.header("Emergency Contact")
e_contact_name = st.text_input("Emergency Contact Name")
e_contact_phone = st.text_input("Emergency Contact Phone Number")

# --- Final Confirmation ---
st.header("Final Authorization")
hr_officer = st.text_input("HR Staff Completing This Form")
confirmation = st.checkbox("I confirm all data above is accurate and complete.")

if st.button("Submit Onboarding"):
    if full_name and email and start_date and confirmation:
        st.success("✅ Onboarding form submitted successfully.")
    else:
        st.error("❌ Please complete all required fields before submitting.")

