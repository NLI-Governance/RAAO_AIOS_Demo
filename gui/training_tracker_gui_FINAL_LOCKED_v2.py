# training_tracker_gui.py
# Final: Grant Code dropdown + safe employee ID lookup

import streamlit as st
import pandas as pd
import os
import sys
from datetime import date, timedelta
import openai

# Load GPT key securely
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "secrets")))
from openai_key import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY

st.set_page_config(page_title="Training Tracker", layout="centered")
st.image("logo.png", width=120)
st.title("Employee Training & Certification Tracker")

# File paths
base = os.path.dirname(__file__)
training_csv = os.path.abspath(os.path.join(base, "..", "data", "employee_training_log.csv"))
catalog_csv = os.path.abspath(os.path.join(base, "..", "data", "training_catalog.csv"))
employee_csv = os.path.abspath(os.path.join(base, "..", "data", "employee_records.csv"))
grant_csv = os.path.abspath(os.path.join(base, "..", "data", "grant_codes.csv"))
os.makedirs(os.path.dirname(training_csv), exist_ok=True)

# Load employees safely
if os.path.exists(employee_csv):
    emp_df = pd.read_csv(employee_csv)
    names = emp_df["Full Name"].dropna().tolist() if "Full Name" in emp_df.columns else []
    ids = dict(zip(emp_df["Full Name"], emp_df["Employee ID"])) if "Employee ID" in emp_df.columns else {}
    depts = dict(zip(emp_df["Full Name"], emp_df["Department"])) if "Department" in emp_df.columns else {}
else:
    names = ["Alice Johnson", "Marcus Lee"]
    ids = {"Alice Johnson": "EMP001", "Marcus Lee": "EMP002"}
    depts = {"Alice Johnson": "Outreach", "Marcus Lee": "HR"}

# Load training catalog
if os.path.exists(catalog_csv):
    catalog_df = pd.read_csv(catalog_csv)
    training_titles = catalog_df["Training Title"].dropna().tolist()
    type_lookup = dict(zip(catalog_df["Training Title"], catalog_df["Training Type"]))
    days_valid_lookup = dict(zip(catalog_df["Training Title"], catalog_df["Valid Days"]))
else:
    training_titles = ["HIPAA", "OSHA"]
    type_lookup = {"HIPAA": "Compliance", "OSHA": "Safety"}
    days_valid_lookup = {"HIPAA": 730, "OSHA": 365}

# Load grant codes
if os.path.exists(grant_csv):
    grant_df = pd.read_csv(grant_csv)
    grant_codes = grant_df["Grant Code"].dropna().tolist()
else:
    grant_codes = []

# Load training records
if os.path.exists(training_csv):
    df = pd.read_csv(training_csv)
else:
    df = pd.DataFrame(columns=[
        "Employee Name", "Employee ID", "Department",
        "Training Title", "Training Type", "Grant Code",
        "Completion Date", "Certification Expiration", "Status"
    ])

statuses = ["Completed", "In Progress", "Expired"]

# Entry form
with st.form("training_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.selectbox("Employee Name 🛈", names)
        emp_id = ids.get(name, "UNKNOWN")
        dept = depts.get(name, "UNKNOWN")
        training_title = st.selectbox("Training Title 🛈", training_titles)
        training_type = type_lookup.get(training_title, "Other")
    with col2:
        grant_code = st.selectbox("Grant Code 🛈", grant_codes)
        completion = st.date_input("Completion Date 🛈", date.today())
        days_valid = int(days_valid_lookup.get(training_title, 0))
        expiration = completion + timedelta(days=days_valid) if days_valid > 0 else None
        status = st.selectbox("Status 🛈", statuses)

    submitted = st.form_submit_button("Save Training Record")

if submitted:
    new_entry = {
        "Employee Name": name,
        "Employee ID": emp_id,
        "Department": dept,
        "Training Title": training_title,
        "Training Type": training_type,
        "Grant Code": grant_code,
        "Completion Date": completion,
        "Certification Expiration": expiration,
        "Status": status
    }
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(training_csv, index=False)
    st.success("Training record saved.")

# GPT Assistant
st.markdown("### 🧠 AI Training Assistant 🛈")
st.caption("Ask questions about certification duration, training requirements, or policy implications.")
ai_prompt = st.text_area("What would you like help with?", placeholder="e.g., Why is OSHA training required for field employees?")

if st.button("Ask Assistant"):
    with st.spinner("Thinking..."):
        try:
            client = openai.OpenAI(api_key=OPENAI_API_KEY)
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You're a training and certification assistant for a nonprofit. Help answer policy, compliance, and credentialing questions."},
                    {"role": "user", "content": ai_prompt}
                ],
                temperature=0.6,
                max_tokens=500
            )
            st.success("Training Guidance:")
            st.markdown(response.choices[0].message.content)
        except Exception as e:
            st.error("AI assistant error:")
            st.exception(e)

# Display records
st.markdown("### Logged Training Records")
if df.empty:
    st.info("No training records found.")
else:
    st.dataframe(df, use_container_width=True)

st.download_button("Download CSV", data=df.to_csv(index=False), file_name="employee_training_log.csv", mime="text/csv")

st.markdown("---")
st.markdown("© 2025 Rising Against All Odds | Training Tracker (Grant-Linked)")
